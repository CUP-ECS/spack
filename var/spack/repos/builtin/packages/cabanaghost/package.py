# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cabanaghost(CMakePackage, CudaPackage, ROCmPackage):
    """Halo Exchange Benchmark for Exploring Fine-grain Communication APIs and Performance in the Cabana/Cajita performance portability framework."""


    homepage = "https://github.com/CUP-ECS/CabanaGhost"
    git = "https://github.com/CUP-ECS/CabanaGhost.git"

    maintainers("patrickb314", "EvanDrakeSuggs")

    license("BSD-3-Clause")

    version("develop", branch="develop")
    version("main", branch="main")

    # Variants are primarily backends to build on GPU systems and pass the right
    # informtion to the packages we depend on
    variant("cuda", default=False, description="Use CUDA support from subpackages")
    variant("openmp", default=False, description="Use OpenMP support from subpackages")

    # Dependencies for all CabanaGhost versions
    depends_on("mpi")
    with when("+cuda"):
        depends_on("mpich +cuda", when="^[virtuals=mpi] mpich")
        depends_on("mvapich +cuda", when="^[virtuals=mpi] mvapich")
        depends_on("mvapich2 +cuda", when="^[virtuals=mpi] mvapich2")
        depends_on("mvapich2-gdr +cuda", when="^[virtuals=mpi] mvapich2-gdr")
        depends_on("openmpi +cuda", when="^[virtuals=mpi] openmpi")

    with when("+rocm"):
        depends_on("mpich +rocm", when="^[virtuals=mpi] mpich")
        depends_on("mvapich2-gdr +rocm", when="^[virtuals=mpi] mvapich2-gdr")

    # Kokkos dependencies
    depends_on("kokkos @4:")
    depends_on("kokkos +cuda +cuda_lambda +cuda_constexpr", when="+cuda")
    depends_on("kokkos +rocm", when="+rocm")
    depends_on("kokkos +wrapper", when="%gcc+cuda")

    # Cabana dependencies
    depends_on("cabana @0.6.0: +grid +silo +hdf5 +mpi")
    depends_on("cabana +cuda", when="+cuda")
    depends_on("cabana +rocm", when="+rocm")

    # Silo dependencies
    depends_on("silo @4.11:")
    depends_on("silo @4.11.1:", when="%cce")  # Eariler silo versions have trouble cce

    # If we're using CUDA or ROCM, require MPIs be GPU-aware
    conflicts("mpich ~cuda", when="+cuda")
    conflicts("mpich ~rocm", when="+rocm")
    conflicts("openmpi ~cuda", when="+cuda")
    conflicts("^intel-mpi")  # Heffte won't build with intel MPI because of needed C++ MPI support
    conflicts("^spectrum-mpi", when="^cuda@11.3:")  # cuda-aware spectrum is broken with cuda 11.3:

    # Propagate CUDA and AMD GPU targets to cabana
    for cuda_arch in CudaPackage.cuda_arch_values:
        depends_on("cabana cuda_arch=%s" % cuda_arch, when="+cuda cuda_arch=%s" % cuda_arch)
    for amdgpu_value in ROCmPackage.amdgpu_targets:
        depends_on(
            "cabana +rocm amdgpu_target=%s" % amdgpu_value,
            when="+rocm amdgpu_target=%s" % amdgpu_value,
        )

    # CMake specific build functions
    def cmake_args(self):
        args = []

        # Use hipcc as the c compiler if we are compiling for rocm. Doing it this way
        # keeps the wrapper insted of changing CMAKE_CXX_COMPILER keeps the spack wrapper
        # and the rpaths it sets for us from the underlying spec.
        if "+rocm" in self.spec:
            env["SPACK_CXX"] = self.spec["hip"].hipcc

        # If we're building with cray mpich, we need to make sure we get the GTL library for
        # gpu-aware MPI, since cabana requires it
        if self.spec.satisfies("+rocm ^cray-mpich"):
            gtl_dir = join_path(self.spec["cray-mpich"].prefix, "..", "..", "..", "gtl", "lib")
            args.append(
                "-DCMAKE_EXE_LINKER_FLAGS=-Wl,-rpath={0} -L{0} -lmpi_gtl_hsa".format(gtl_dir)
            )
        elif self.spec.satisfies("+cuda ^cray-mpich"):
            gtl_dir = join_path(self.spec["cray-mpich"].prefix, "..", "..", "..", "gtl", "lib")
            args.append(
                "-DCMAKE_EXE_LINKER_FLAGS=-Wl,-rpath={0} -L{0} -lmpi_gtl_cuda".format(gtl_dir)
            )
        return args
