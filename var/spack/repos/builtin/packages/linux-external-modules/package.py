# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from shutil import copy2

from spack.package import *


class LinuxExternalModules(MakefilePackage):
    """The Linux kernel provides services to start and stop programs,
    handles the file system and other common "low-level" tasks that most
    programs share, and schedules access to avoid conflicts when programs
    try to access the same resource or device simultaneously. The kernel
    has a modular design such that modules can be integrated as software
    components. In this package, Linux has been configured to build out-of-tree
    kernel modules."""

    homepage = "https://github.com/torvalds/linux"
    url = "https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.10.2.tar.xz"
    # See section 2.1 for how to build out-of-tree kernel modules using linux-external-modules.
    # Specifically, <path_to_kernel_src> should point to the install directory of
    # linux-external-modules.
    how_to = "https://docs.kernel.org/kbuild/modules.html"

    maintainers("kyotsukete", "rountree")

    license("GPL-2.0-only", checked_by="kyotsukete")

    version("6.10.3", sha256="fa5f22fd67dd05812d39dca579320c493048e26c4a556048a12385e7ae6fc698")
    version("6.10.2", sha256="73d8520dd9cba5acfc5e7208e76b35d9740b8aae38210a9224e32ec4c0d29b70")
    version("6.10.1", sha256="70109dfd1cd1c5f8a58eb1cb37122b9bf93f9c6a6280bf91019263c7339cf76b")
    version("6.10", sha256="774698422ee54c5f1e704456f37c65c06b51b4e9a8b0866f34580d86fef8e226")
    version("6.9.12", sha256="5ae7cc4e0e2f6b9ba630f643985ba0522c7d5e5b9571ba478a3cb513edd4cf22")
    version("6.9.11", sha256="dedf84e0832c3e912024e0c04347e9e48a2b2676d5c5cd869b3eb0ce92f513e1")
    version("6.9.10", sha256="efd12e335fa67d13a3eae30e4b7b7546e74b8ccc90682e4c3fffab0b22654da1")
    version("6.9.9", sha256="2be05b487eb239a3bf687d628a8f104177d09c310f00bcc2a5e50f1733421eb9")
    version("6.9.8", sha256="f048267b7b88316c9ca708c68d15a9ae802dcfc943c3188c1273eb958c433281")
    version("6.9.7", sha256="e4f588cd91eef9d461e5e14fdf9415feff8a72fbcc274089a0f768a58de001f8")
    version("6.9.6", sha256="5d4366e2b89998f274abe03557ef3bc78b58e47fc62c102d51e6f49e5ed96b4b")
    version("6.9.5", sha256="a51fb4ab5003a6149bd9bf4c18c9b1f0f4945c272549095ab154b9d1052f95b1")
    version("6.9.4", sha256="272800e0d1a7d01a78bce95a3aaf5c80816f50eb15c517d7003e58355760ecc2")
    version("6.9.3", sha256="c321c46401368774fc236f57095b205a5da57415f9a6008018902f9fd5eddfae")
    version("6.9.2", sha256="d46c5bdf2c5961cc2a4dedefe0434d456865e95e4a7cd9f93fff054f9090e5f9")
    version("6.9.1", sha256="01b414ba98fd189ecd544435caf3860ae2a790e3ec48f5aa70fdf42dc4c5c04a")
    version("6.9", sha256="24fa01fb989c7a3e28453f117799168713766e119c5381dac30115f18f268149")
    version("6.8.12", sha256="19b31956d229b5b9ca5671fa1c74320179682a3d8d00fc86794114b21da86039")
    version("6.8.11", sha256="b78dcd09f6b725872a2c0c87a70a064b0fbbcccfe5ce60aa46c669934a9e28b6")
    version("6.8.10", sha256="b0bb92d982f88380e5b2059349c3a862e0afa712e0646eb0e082b9c2c5cb5176")
    version("6.8.9", sha256="f905f1238ea7a8e85314bacf283302e8097006010d25fcea726d0de0ea5bc9b6")
    version("6.8.8", sha256="1c4cdcb9d560fad1fb95db2cb8afbedc922f9ead848371fe40363b13f9f631ba")
    version("6.8.7", sha256="291d1a1faf4e87b3b0ea9729080db887aafd1ff2fac1430ceca921e46bc22fae")
    version("6.8.6", sha256="9e723232d603ab45ebf043c34714c48f277ab195c29abcb8472f2a4c3a5a1995")
    version("6.8.5", sha256="138923e5d73748b4bdbe9b5a0b8f36dfac9fcc16753a9222928dc6c963effa89")
    version("6.8.4", sha256="d5dec495fc00605fa9e04114df547fbc92b33d9ea7a4a2b7073c589590e79e63")
    version("6.8.3", sha256="db7eb56d5014ee9a7fac0c715053155d92798d98d9197a2173eef1f0a496c986")
    version("6.8.2", sha256="9ac322d85bcf98a04667d929f5c2666b15bd58c6c2d68dd512c72acbced07d04")
    version("6.8.1", sha256="8d0c8936e3140a0fbdf511ad7a9f21121598f3656743898f47bb9052d37cff68")
    version("6.8", sha256="c969dea4e8bb6be991bbf7c010ba0e0a5643a3a8d8fb0a2aaa053406f1e965f3")
    version("6.7.12", sha256="6c2979e3948806a0dbacba193f8453ea42c179c1eb9f6136e3c35d87e5707984")
    version("6.7.11", sha256="2c6497c971632fd9d056941a8a31369d36ef07baa755e4c1cdcc326acb090b4a")
    version("6.7.10", sha256="a9b99fb376f9fcd699c7c252aeef3bb5ba26280eb049711ac091b2eb2b487c03")
    version("6.7.9", sha256="0fd733fc0778f8da1fdf66df1698d394248807de71eef83a4d1218bcb3dfd346")
    version("6.7.8", sha256="469ff46b98685df13b56c98417c64ba7a30f8a45baf34aa99f07935e1bf65c18")
    version("6.7.7", sha256="256b8b44570ddbe266eb3ad0c2cba2616f1609b4a3de5014a3da5512907b14d9")
    version("6.7.6", sha256="e489ec0e1370d089b446d565aded7a698093d2b7c4122a18f21edb6ef93d37d3")
    version("6.7.5", sha256="29f6464061b8179cbb77fc5591e06a2199324e018c9ed730ca3e6dfb145539ff")
    version("6.7.4", sha256="f68d9f5ffc0a24f850699b86c8aea8b8687de7384158d5ed3bede37de098d60c")
    version("6.7.3", sha256="b7f08c652747574a3aa26e317d7a8f23ffab3fb645e1b1533b215dcfd5742b44")
    version("6.7.2", sha256="c34de41baa29c475c0834e88a3171e255ff86cd32d83c6bffc2b797e60bfa671")
    version("6.7.1", sha256="1ecffa568e86a2202ba5533ad9034bc263a9aa14e189597a94f09b3854ad68c3")
    version("6.7", sha256="ef31144a2576d080d8c31698e83ec9f66bf97c677fa2aaf0d5bbb9f3345b1069")
    version("6.6.44", sha256="93218296934915636fe6ba08e125948424cc270fd8948502c0ab91087a9fccd8")
    version("6.6.43", sha256="0ad83b1a1a780a1aad948d55aa55ee63c50c626f2d46910b9d2180028d100a5e")
    version("6.6.42", sha256="8801c8c297d774e76044977ec3d0684399dc4e7cce347d730874ec78b774e683")
    version("6.6.41", sha256="9ec99c578158ab85d99b37791a76643d2ea4c3f72ecbef7b5eb6d60f3de032ef")
    version("6.6.40", sha256="5c3a3c03c055b8d601a6d7f80d1465ada6b83a12299f6ace2027b47f0baff538")
    version("6.6.39", sha256="2783d42112095f95c510e1b421f056df8cbfa845f9040c6115080434a77a776b")
    version("6.6.38", sha256="4ed403ffb550565d03485aeca9a52c128cdde43f4a373a1a9ee3a590524fe743")
    version("6.6.37", sha256="f3976e77708694fe4a1f8d1307c315c8a36cbc58f038a38e006b91e29a1f3214")
    version("6.6.36", sha256="b9676828b737e8fb8eaa5198303d35d35e8df019550be153c8a42c99afe0cdd5")
    version("6.6.35", sha256="fce3ee728712ed063aa8c14a8756c8ff8c7a46ba3827f61d2b04a73c7cf5dd9e")
    version("6.6.34", sha256="c4e0ec8f593aa3717e85abad940466e7d7cbc362989426eb37f499330a461ba0")
    version("6.6.33", sha256="a13ebc20dc2a75722699949af74aa86a4ce5d544d6daaa6a7de4e8c81b40de97")
    version("6.6.32", sha256="aaa824eaf07f61911d22b75ff090a403c3dd0bd73e23933e0bba8b5971436ce1")
    version("6.6.31", sha256="d6ecff966f8c95ec4cb3bb303904f757b7de6a6bcfef0d0771cb852158e61c20")
    version("6.6.30", sha256="b66a5b863b0f8669448b74ca83bd641a856f164b29956e539bbcb5fdeeab9cc6")
    version("6.6.29", sha256="7f26f74c08082c86b1daf866e4d49c5d8276cc1906a89d0e367e457ec167cbd0")
    version("6.6.28", sha256="818716ed13e7dba6aaeae24e3073993e260812ed128d10272e94b922ee6d3394")
    version("6.6.27", sha256="639e50060e3c8f23ed017cb10cfeacc6ba88ff5583812bb76859b4cc6a128291")
    version("6.6.26", sha256="af54b449f4fb93b8e8daa346144a7309e8e95174bd962c4b5917cf56120456d9")
    version("6.6.25", sha256="99d210be87908233a55b0fadc0dccd3b95926c0651b6b82e37350b2029de1f44")
    version("6.6.24", sha256="3e9ef879dae8319338eb0dc2d2c2025c13257fdeddf6245c000cb5a85a8af6f5")
    version("6.6.23", sha256="200fd119cb9ef06bcedcdb52be00ba443163eab154295c5831fed9a12211a8b9")
    version("6.6.22", sha256="23e3e7b56407250f5411bdab95763d0bc4e3a19dfa431d951df7eacabd61a2f4")
    version("6.6.21", sha256="ee0b430148da94d2b13608b8d80b007b7d281dc90e3f19b63cf9a9943810e457")
    version("6.6.20", sha256="e2f6c7f39b304248193370f8c5755553ab73ad5672e92dae994a344084d8dd22")
    version("6.6.19", sha256="b5637e6b72c2b4b12e7db790bc155d141a9c2fe4b25f7b215410107e8747139a")
    version("6.6.18", sha256="4e43d8c5fba14f7c82597838011648056487b7550fd83276ad534559e8499b1d")
    version("6.6.17", sha256="ee7650996ba75aa29fe66f309b413097f249a03e7001f2a41128c7c95205226a")
    version("6.6.16", sha256="b21d5795a3bead4f112916423222faa8a0f519e4201df343e3eb88dc9e4aaa30")
    version("6.6.15", sha256="ab290c7f8687f2f8af96e14abd0700ba8b282426151873690f51621d8d5f5faa")
    version("6.6.14", sha256="fbe96b2db3f962cd2a96a849d554300e7a4555995160082d4f323c2a1dfa1584")
    version("6.6.13", sha256="88b89e7dd41ead4e3ab1e411c8bb8d592575acf815cf1df3c0dc57e2e882c0bc")
    version("6.6.12", sha256="1fd7ec8c3d9c4e4b3a41d11e2c6d151e5fbf875dd08b3577f73afd6ee6674605")
    version("6.6.11", sha256="afe2e5a661bb886d762684ebea71607d1ee8cb9dd100279d2810ba20d9671e52")
    version("6.6.10", sha256="9ee627e4c109aec7fca3eda5898e81d201af2c7eb2f7d9d7d94c1f0e1205546c")
    version("6.6.9", sha256="8ebc65af0cfc891ba63dce0546583da728434db0f5f6a54d979f25ec47f548b3")
    version("6.6.8", sha256="5036c434e11e4b36d8da3f489851f7f829cf785fa7f7887468537a9ea4572416")
    version("6.6.7", sha256="0ce68ec6019019140043263520955ecd04839e55a1baab2fa9155b42bb6fd841")
    version("6.6.6", sha256="ebf70a917934b13169e1be5b95c3b6c2fea5bc14e6dc144f1efb8a0016b224c8")
    version("6.6.5", sha256="7c92795854a68d218c576097d50611f8eea86fd55810e0bc27724f020753b19e")
    version("6.6.4", sha256="49e49660c93d8d6d58f118360d3ca8131695ec34669263ca8f041c876da93e45")
    version("6.6.3", sha256="28edfc3d4f90cd738f2a20f5a2d68510268176d6111f6278d8f495edfd9495a7")
    version("6.6.2", sha256="73d4f6ad8dd6ac2a41ed52c2928898b7c3f2519ed5dbdb11920209a36999b77e")
    version("6.6.1", sha256="da1ed7d47c97ed72c9354091628740aa3c40a3c9cd7382871f3cedbd60588234")
    version("6.6", sha256="d926a06c63dd8ac7df3f86ee1ffc2ce2a3b81a2d168484e76b5b389aba8e56d0")
    version("6.5.13", sha256="78fbd43822f4c56bc16e89e8874767f592532e1a0ffcd1af4dd279559b5fcbb5")
    version("6.5.12", sha256="4a69c1d32c974e125ad723145d31683a3b078667ad56d17f7852dcaffb9f359f")
    version("6.5.11", sha256="2ee24af9282b80923b2da56b70aad7df2e8ee4e3f076452e05ba66be2059b519")
    version("6.5.10", sha256="a15f498604adf8f6ac842f1733a694083f23e578b48c8e97d94b6d8968e55a8b")
    version("6.5.9", sha256="c6662f64713f56bf30e009c32eac15536fad5fd1c02e8a3daf62a0dc2f058fd5")
    version("6.5.8", sha256="299cca897d90deaa176eebec42f0a80eeb7516afed330a45c14da9de086cf717")
    version("6.5.7", sha256="0d09ea448005c9cfe5383e4c72a872b39188b928f8c44e146b03b1b7851fbb8c")
    version("6.5.6", sha256="78e36d4214547051c24df2140f4ce09428d6c515ad9a71b38b28e8094a95d2f6")
    version("6.5.5", sha256="8cf10379f7df8ea731e09bff3d0827414e4b643dd41dc99d0af339669646ef95")
    version("6.5.4", sha256="bdf76c15229b241e578046b8486106f09534d754ea4cbf105e0660e551fb1669")
    version("6.5.3", sha256="4cac13f7b17bd8dcf9032ad68f9123ab5313d698c9f59416043165150763eb4f")
    version("6.5.2", sha256="2027e14057d568ad3ddc100dadf4c8853a49b031270478a61d88f6011572650f")
    version("6.5.1", sha256="23765dd44425462cd92adbee52670608fd7f3fd183a83b25ba7a7b4883d0451b")
    version("6.5", sha256="7a574bbc20802ea76b52ca7faf07267f72045e861b18915c5272a98c27abf884")
    version("6.4.16", sha256="9626ec84a39ecb009bf11a271dd520941159c165d4e62f82e3a77b79d20ff27d")
    version("6.4.15", sha256="23f9e7c8d2a583e432ed203cab88fbd7ecc6920015cb5d38d5b7585acee814de")
    version("6.4.14", sha256="75eae323747ae37b05086c5a51326a744eb611b0e890e7ebe77de362b30450e6")
    version("6.4.13", sha256="5e5511b50bc9fd358bb5d7746fab3c5ea396d42c6bd7a54b2555ede0de5ac8e5")
    version("6.4.12", sha256="cca91be956fe081f8f6da72034cded96fe35a50be4bfb7e103e354aa2159a674")
    version("6.4.11", sha256="546b68b5097d3c0d74722de62aae217729d98e45fbb6bd458b490ac21ea40918")
    version("6.4.10", sha256="980b3fb2a97788fd885cbd85ba4520980f76c7ae1d62bfc2e7477ee04df5f239")
    version("6.4.9", sha256="b8b8a29852b999f337c4e93eff6c91fb7fd2d49a6614cbcbeb6fa171ba55cc9f")
    version("6.4.8", sha256="c59f34e19e84db30206b9373041abf893f9d8a08765d163586570a5238c458b6")
    version("6.4.7", sha256="de143cb61dcaa756c05f56ff35144316d810615819518a33e34754f064c4a7d8")
    version("6.4.6", sha256="e1ecc496efc48aaf25a6607a4b8e52d574d6f67a2b0aa1664087d301d3515ea4")
    version("6.4.5", sha256="374e2c07463c51dfd71204b7fac3b73c7f973550ae019b74e9f2b815b28de9b7")
    version("6.4.4", sha256="9cbc4a2be714a4d154e1312c9f33ded91174907c8b15ee936ad27002ac75ff2a")
    version("6.4.3", sha256="7134ed29360df6f37a26410630283f0592c91a6d2178a9648226d30ddf8c88a1")
    version("6.4.2", sha256="a326ab224176c5b17c73c9ccad85f32e49b6e4e764861d57595727b7ef10062c")
    version("6.4.1", sha256="0d9daa9f1c176fb13b9447f6e3d80e82b49043f0d344c247bbf09b4e625beef3")
    version("6.4", sha256="8fa0588f0c2ceca44cac77a0e39ba48c9f00a6b9dc69761c02a5d3efac8da7f3")
    version("6.3.13", sha256="ea460560e2898022c5f3c4649908694dcd75a094ffde726e8c6ca5e0a09491fb")
    version("6.3.12", sha256="cb7fdefc207dd4e8ef947fccd687126425edce0138ca11191bc0590c678e6cd7")
    version("6.3.11", sha256="1d5a3fbd4d4265b6c9605d5c605d947673e7643af2890e4ad5c946940f123e16")
    version("6.3.10", sha256="e0a9ad8692b2191cbd33db371a780a3fe375de90123a307ecd874c0860cd46e3")
    version("6.3.9", sha256="41ecf21399b17ab85163750ba22347d09b54fa099b80b63d0e2ef0066129b13e")
    version("6.3.8", sha256="4323d421250e2e444c35d36f4aa8ddb56591dedc25c68d359d19c4ef9dd20955")
    version("6.3.7", sha256="fe369743996c522a7b473e99dcf8f88847bd5cc88546fd3b7a41d9fe5a5b97a9")
    version("6.3.6", sha256="7a6a1f0dfa0bf7f45f9d4a7b409315cf32267850adab4db033a17de0320a24ef")
    version("6.3.5", sha256="f5cd478c3d8b908ab606afd1e95a4f8f77e7186b4a82829251d6e6aaafff825e")
    version("6.3.4", sha256="d8627528ed6b3ae607d00b1ef5a46e0e7051ae40b285fd4e82f4ff0bb72b68e8")
    version("6.3.3", sha256="8975216a6cee827390586758ed69d19743367098d1fc5dd5694987bb529e44e5")
    version("6.3.2", sha256="b612ecf282ca3f7989ff6d9f39082833b7dc2d522cb969a05334d3614e9c5328")
    version("6.3.1", sha256="78620fb4a7d5e0db1d4eb8d5b1c6e207ba5d19564efa63967a59b6daf89b3f2a")
    version("6.3", sha256="ba3491f5ed6bd270a370c440434e3d69085fcdd528922fa01e73d7657db73b1e")
    version("6.2.16", sha256="06ff0d780a6934b46140f6d8c1a15792c78aa337d8b2411bf90747371d358713")
    version("6.2.15", sha256="9ffa34921044660c6adb3eb5fd996192e322b15bbf532fe4e4e7a47079ed8fc1")
    version("6.2.14", sha256="0ebc9fa309d496d474b06682578c5f7b42f0cf330365102b2feaab65ba296729")
    version("6.2.13", sha256="c7dded14e368834b18bb2ad64af65560d8bcb9d2d6597e0f6ef151fded01e577")
    version("6.2.12", sha256="c7e146b52737adfa4c724bfa41bf4721c5ee3cf220c074fbc60eb3ea62b0ccc8")
    version("6.2.11", sha256="0d236784e60b87c7953535aeb148dd9e773b26495dfa9c6d69615f54fe00dd47")
    version("6.2.10", sha256="57c562c3cd2753f232549cab05c8ad770ed848ae86401619c7581bdffaeea4fe")
    version("6.2.9", sha256="903449c164c03f0e742aacc920e18563585e07a28c6cb79e0fd6c36695fd43f5")
    version("6.2.8", sha256="fed0ad87d42f83a70ce019ff2800bc30a855e672e72bf6d54a014d98d344f665")
    version("6.2.7", sha256="4303105201fb0c0b17155fff87df0a022a32a41eb1ce94a264ae648c64bd0d8d")
    version("6.2.6", sha256="1fe2f1d7ceb7129c111159d8efd361971dbf212206f81e7078b98df8b00b3d9d")
    version("6.2.5", sha256="65ab0192cf6e5808a075588944de8febf9e61f1a85147e479ffd440708cee5b9")
    version("6.2.4", sha256="8275806bad41e9f67b60b00a9460a7912aeab93913681ae0b13fa0e4d54032c5")
    version("6.2.3", sha256="b36d0b54fc13770802aff37d8f8d6fec7b950e4f099884e30445ad2265063924")
    version("6.2.2", sha256="c12755a2bb0e19e83457727e949ee1020cc268f44222488256223da8eeecbfb0")
    version("6.2.1", sha256="2fcc07e1c90ea4ce148f50f9beeb0dca0b6e4b379a768de8abc7a4a26f252534")
    version("6.2", sha256="74862fa8ab40edae85bb3385c0b71fe103288bce518526d63197800b3cbdecb1")
    version("6.1.103", sha256="5eb4706f898f50881552ff5146d892132d3ffc5298033bffe27087d3a44c4573")
    version("6.1.102", sha256="1ba5f93b411ead7587fe48b2eec6c656f6796d31f5e406d236913c77512497ec")
    version("6.1.101", sha256="f1459faa68429fa6607ae18b869fd02ed685bb33c72289f175aca163c592b34c")
    version("6.1.100", sha256="b9aa6ec1a00f234d6c6f2d428fbb0a6bf459606c259263df978f86685b65a8b9")
    version("6.1.99", sha256="c086ee9ce2b1eeba6e085d569bc97ae764a5d15f6322847f0ebc9f787ae34dd3")
    version("6.1.98", sha256="97cdc9127c7700556ea0891267a0c24cf372f4b81636fb8203a914f3a69f3406")
    version("6.1.97", sha256="890b845f36452328716e62dd893b634584f607cdd44b4e685392d302d3be41af")
    version("6.1.96", sha256="3e77c9069de5e7ab02ff9c2dcfe77dab193613fc1de21071901b4153374862a9")
    version("6.1.95", sha256="2960f0aa1d75665f39114ad3c272a999c54796e553a2355d0379f5188d14dfbd")
    version("6.1.94", sha256="38ea71ad22ae0187fd8ee5ff879b33b0d9bd58161ac9a3e868ae0b4c66b95369")
    version("6.1.93", sha256="df31af2ef5923d61fadd68bfd991f50f2e42a913895eb4b03214ee78f8720bcf")
    version("6.1.92", sha256="9019f427bfdc9ced5bc954d760d37ac08c0cdffb45ad28087fc45a73e64336c9")
    version("6.1.91", sha256="880ace63ca2291b8b639e9bd862cc828649d3e1e00ccfee5861473debd2e4dec")
    version("6.1.90", sha256="83a3d72e764fceda2c1fc68a4ea6b91253a28da56a688a2b61776b0d19788e1d")
    version("6.1.89", sha256="12bab8e092618d1d4eeaf4201e6e70054c94896198956bd84ff0e908b0264719")
    version("6.1.88", sha256="696902fd45c543168b638370464c44ffbfdf5f20003ae32b6145bbce3665f8d1")
    version("6.1.87", sha256="fc7af16a72e8aee4790b796f1bf5003cb0de6095ea1ffd7d7c7c9a5678d95124")
    version("6.1.86", sha256="d3d3c8c44f0f0a870a95bd2823f9d91979d1aa6f266da5d8cccd0c4b15e3115b")
    version("6.1.85", sha256="33fe9bcc597c60021a2b2abacd4e0f6f546200ab99594c9a07ad600258b86274")
    version("6.1.84", sha256="af97d2ebe14765d0db3af6560309daf08535da25bfad36e5fb3e436f22a1707a")
    version("6.1.83", sha256="88b69611093613ce4494527685f833af0c31b986dcbeda7086f69f18f9e0b190")
    version("6.1.82", sha256="d150d2d9d416877668d8b56f75759f166168d192419eefaa942ed67225cbec06")
    version("6.1.81", sha256="0ebd861c6fd47bb0a9d3a09664d704833d1a54750c7bf9c4ad8b5e9cbd49342b")
    version("6.1.80", sha256="568ecaaebb8b87c7c8246bba67bc83402972bf34f5811651a2d3cd548ff7b671")
    version("6.1.79", sha256="faa49ca22fb55ed4d5ca2a55e07dd10e4e171cfc3b92568a631453cd2068b39b")
    version("6.1.78", sha256="65206b969831236849c9906eba267e715734a93808e9909fd9b4f12eea10d689")
    version("6.1.77", sha256="3b54ec567716cdfb3618caf38c58a8aab1372cc41c16430633febe9ccdb3f91d")
    version("6.1.76", sha256="0580cc0e81ff9aee245f79531d8c1c5c7d711eee227cd4cf52d1ff335727b1fd")
    version("6.1.75", sha256="6cd19410330c13ec4c18fd28a83d3e40fc12a152815fb7c3e1b0764329093a56")
    version("6.1.74", sha256="b7fbd1d79faed2ce3570ef79dc1223e4e19c868b86326b14a435db56ebbb2022")
    version("6.1.73", sha256="6cad48706bf1cde342613dca2a2cd6dd4f79f88f9e4d356263564e4b2a5d7e87")
    version("6.1.72", sha256="98dce69077c35cffca799dcdbbd32a02242aad6b0950eb931936bb2ef69f0926")
    version("6.1.71", sha256="2df774dd53f9ffd4e57ebf804cf597709295df6a304fe261d25220a134b7f041")
    version("6.1.70", sha256="ed1365266456c07696a7499581aec5d851ca2296f4f6f90f23d189ea5a56afef")
    version("6.1.69", sha256="7e3d2694d18ce502068cc88a430da809abbd17d0773268524ebece442612b541")
    version("6.1.68", sha256="365ff26a30e206de9b18489f45d38582a0a61b7c5919f8ab89295a47316784e1")
    version("6.1.67", sha256="7537db7289ca4854a126bc1237c47c5b21784bcbf27b4e571d389e3528c59285")
    version("6.1.66", sha256="419e62cd6c4239e6950b688db9e8753eb1e99c216dc3204f7932398a3fef1a0c")
    version("6.1.65", sha256="407229936802a44b1e484c2e9ac3bbe53a65d825cc468ccdbd76281b491ab20a")
    version("6.1.64", sha256="629daa38f3ea67f29610bfbd53f9f38f46834d3654451e9474100490c66dc7e7")
    version("6.1.63", sha256="c29d043b01dd4fcc61a24fd027c5c7912b15b1f10d8e3c83a0cb935885f0758d")
    version("6.1.62", sha256="b9fd616facd6becfceef88b9be718d0f16625cab3fe81d11384802a7091e85ec")
    version("6.1.61", sha256="ad2c9d12fc36e2dde4796a3eec8f4ddca2e278098f4e555b6e6f5f03ef6964ce")
    version("6.1.60", sha256="58520e7ae5a6af254ddf7ddbfc42e4373b0d36c67d467f6e35a3bd1672f5fb0a")
    version("6.1.59", sha256="627f7724c675036639290fb5c39e3fdeb3d566b80b192c45f4a808ab54c8c0a0")
    version("6.1.58", sha256="ce987ed3d2f640b3a2a62a0a8573d538a36dfd3cc31e2d7a239ce5a16c1c21ad")
    version("6.1.57", sha256="f9ebfe3ddc5152d87b37e33be30e31875d137433be10a57ce29d2eae7b6e91b1")
    version("6.1.56", sha256="9edefdde32c2298389dcd19566402332b3c2016f5ada17e5820f500b908d478c")
    version("6.1.55", sha256="a87e241ec15d53452c4efe219713a3769d88cc436b5b98cf6efb262c4aff15c0")
    version("6.1.54", sha256="a3181e46d407cd6ab15f412402e8220684ff9659b0262b7a3de7384405ce4e27")
    version("6.1.53", sha256="5f57e0a04810d24f2b1a8fc95451241f80530e678717eda0f45104c6dc78ed7e")
    version("6.1.52", sha256="567737990dbc9265966a0786392821a9fa559fd346494fd1eff050dbeb383a52")
    version("6.1.51", sha256="58b0446d8ea4bc0b26a35e2e3509bd53efcdeb295c9e4f48d33a23b1cdaa103b")
    version("6.1.50", sha256="b27ac1443eea563bc546ee1f67d9802bc8d6c0f6f18707407fba01f9f78c488c")
    version("6.1.49", sha256="c9ea14231ca4ca6e3882a9339a8c3c414e4c91519d3e50af6822f47e99057a0f")
    version("6.1.48", sha256="c606cbd0353e677df6fae73cc16ba3c9244b98372ed7771d551024016f55ac31")
    version("6.1.47", sha256="93d58b6af007a5f44dd26831ff310707deb1ab9380c5136a534287eb3fddfcab")
    version("6.1.46", sha256="f5f67bcfccd47f8d9db2d5ba24e33af7778f40a777577d1fba424f4a1712a296")
    version("6.1.45", sha256="bd2343396e7ddad8974f3689a5a067ec931f4ade793e72b1070a85cd19f1f192")
    version("6.1.44", sha256="2e51d41fe11d082ae167cee05772bb07ca7f19448d2b46772d8ca2db7673a1a5")
    version("6.1.43", sha256="245248470a62d4e94b46f753afc01e19e45b9e6f3a0fa06e7f5da21fe845a808")
    version("6.1.42", sha256="aaf8261b551c8b76b81eab8780b446e88cea4d551ae517ac3a9b2dbdbd381ed3")
    version("6.1.41", sha256="312809a78eea052a08a6580f47b2ed8dd28e5633461d6731febaf3cb1e570bb7")
    version("6.1.40", sha256="43eafc2197a07dcdcff7a7ef79ac7502061f7c564744e51626bf5fa2e22587f0")
    version("6.1.39", sha256="4cddee22fdf657138a06af653492f67cd3a4762c04a34725534bd200d99085b8")
    version("6.1.38", sha256="f9a4f91b609f7d332a5f2be01ab86336fa00149fae6bdc19f16fa19f78802d43")
    version("6.1.37", sha256="46cad712d261a23c8e483a3b79b6a84b9a5f731a8921c9127df35ae35cef1e80")
    version("6.1.36", sha256="d8ca0e300f30b9ff70c6e1497c638a1dac1407f45d3655e9c62c6e45a08afe6b")
    version("6.1.35", sha256="be368143bc5d0dc73dd3e8c6191630c1620520379baf6f47c16116b2c0bc26ac")
    version("6.1.34", sha256="b26f7cbcbf8031efc49f11f236f372fc34a4fd5fc6ad3151b893d1aa038ed603")
    version("6.1.33", sha256="b87d6ba8ea7328e8007a7ea9171d1aa0d540d95eacfcab09578e0a3b623dd2cd")
    version("6.1.32", sha256="7c88b7a09ba2b9e47b78eba2b32b1db6a4d89636f7ddd586545f9671a2521a6c")
    version("6.1.31", sha256="e86917bba1990e967943645484182a64ba325f98b114a1906cc1d50992e073c1")
    version("6.1.30", sha256="1bf254c4ca9ebccb25328296584fb5e87ad635ae0c1cc1deb0b5bb37a4608813")
    version("6.1.29", sha256="1e736cc9bd6036379a1d915e518abd4c2c94ad0fd1ea0da961c3489308b8fcfb")
    version("6.1.28", sha256="7a094c1428b20fef0b5429e4effcc6ed962a674ac6f04e606d63be1ddcc3a6f0")
    version("6.1.27", sha256="c2b74b96dd3d0cc9f300914ef7c4eef76d5fac9de6047961f49e69447ce9f905")
    version("6.1.26", sha256="dfdcc143a879d64a5ee99213b2b4b05b5dccd566c144df93bca1e204df64c110")
    version("6.1.25", sha256="cb72436ceb15086ae3df65e590592030692a9237a37d64105478eb5a72493091")
    version("6.1.24", sha256="aae6a7e38e33589011f5a5c0d7e087c8a26e3daf8d434432ee975ead90546504")
    version("6.1.23", sha256="7458372e8750afe37fd1ac3e7ab3c22f2c6018f760f8134055a03f54aba3ebeb")
    version("6.1.22", sha256="2be89141cef74d0e5a55540d203eb8010dfddb3c82d617e66b058f20b19cfda8")
    version("6.1.21", sha256="b33cb1b86ae13441db36f7e8099ff9edb10494bfd141b4efb41bc44bf815d93a")
    version("6.1.20", sha256="76322de8c01a3c63b42c4d1e9b9e7d1897ddb91276e10d73d1f9df3562f031f0")
    version("6.1.19", sha256="9e991c6e5f6c1ca45eea98c55e82ef6ae3dccc73b3e8a655c8665e585f5a8647")
    version("6.1.18", sha256="842ac15eff0e6fb0c150fdf83f4f6aaf6b4c1239dcf8c14e2227620ec0ae141e")
    version("6.1.17", sha256="a9bc8d0329304e36777d4cbfaa3f8784d7f915640442ca7c5c025b96818f2199")
    version("6.1.16", sha256="a6849c55580b5515a07b6ad21861c450fa20345c66624eecb89e8873816da3c5")
    version("6.1.15", sha256="2c16dfe2168a2e64ac0d55a12d625ebfb963818bb48b60c1868c7c460644c4fd")
    version("6.1.14", sha256="a27076011efec7ad11e9ed0644f512c34cab4c5ed5ba42cfe71c83fabebe810d")
    version("6.1.13", sha256="48841319f4b0077da15e4176e624032d8332d961ee660e1b85e1ce73ded17a67")
    version("6.1.12", sha256="d47aa675170904dcc93eeaa7c96db54d476a11c5d3e8cf3d3b96e364e2a0edea")
    version("6.1.11", sha256="581b0560077863c5116512c0b5fd93b97814092c80e6ebebabe88101949af7a1")
    version("6.1.10", sha256="0be2919ba91cf5873a4cb4d429de78aad0469120d624e333a43b4b011d74d19d")
    version("6.1.9", sha256="d60cf185693c386e7acd9f3eb3a94ae30ffbfee0a9447a20e83711e0bdf5922b")
    version("6.1.8", sha256="b60bb53ab8ba370a270454b11e93d41af29126fc72bd6ede517673e2e57b816d")
    version("6.1.7", sha256="4ab048bad2e7380d3b827f1fad5ad2d2fc4f2e80e1c604d85d1f8781debe600f")
    version("6.1.6", sha256="3e4d8e561da5703a205ae8d7b2bed6c5c64fc4299eebcbfd20481e63b57d5ee3")
    version("6.1.5", sha256="bc7f6d9a8a8bbe9a723e82346bba94b58d926f78bfba106b21e041e0290076fc")
    version("6.1.4", sha256="8aa8f64fa60bb13381a9608d1fefbdd0555e2a70c40b2c7d0671b0d64aa4559e")
    version("6.1.3", sha256="6dc89ae7a7513e433c597c7346ed7ff4bfd115ea43a3b5e27a6bdb38c5580317")
    version("6.1.2", sha256="ee41f3c4f599b2f46f08aae428c9243db403e7292eb2c9f04ee34909b038d1ae")
    version("6.1.1", sha256="a3e61377cf4435a9e2966b409a37a1056f6aaa59e561add9125a88e3c0971dfb")
    version("6.1", sha256="2ca1f17051a430f6fed1196e4952717507171acfd97d96577212502703b25deb")
    version("6.0.19", sha256="abe37eb0e2e331bdc7c4110115664e180e7d43b7336de6b4cd2bd1b123d30207")
    version("6.0.18", sha256="9ab661699211518d8d32f6c7f646230549e8c5b424df6f685a323bc320949459")
    version("6.0.17", sha256="a7ee92092a5459bb46abf0b5449a4e57e8b792591ac4e7ac04ed2542d2ce1d08")
    version("6.0.16", sha256="842071bca611c1f080cbc39c7ab3a6b58d7951f4f41e553b3db4fbe3e0705ce4")
    version("6.0.15", sha256="d484eb3d4f88be14b42507a85ad4b0932e92e7a742acbce74e8be007124a6820")
    version("6.0.14", sha256="5ef18f7e7fcffa2571431fccb3bc26a4e975492208e8490867148a2a5b78c220")
    version("6.0.13", sha256="08d3118d6b755769f166de6babed54964393a7c0928029bef11bf55559a72da4")
    version("6.0.12", sha256="89b730edf8942b49e02f9894244205886c9a214d629b35b88c4ff06ee9304f01")
    version("6.0.11", sha256="2bae6131e64971e1e34ff395fa542971134c857bdb0b29069ab847c7c9a9c762")
    version("6.0.10", sha256="39e57fcd84cd70bfa3e1a4185d3aa0ed7f1432f24c6548d16326b0c3c9541dd0")
    version("6.0.9", sha256="6114a208e82739b4a1ab059ace35262be2a83be34cd1ae23cb8a09337db831c7")
    version("6.0.8", sha256="0de4f83996951c6faf9b2225db4f645882c47b1a09198190f97bd46e5f5fa257")
    version("6.0.7", sha256="67dacc2b78605a56e997f4c08d009be87c98ec66f1870220226c8b3cc676590f")
    version("6.0.6", sha256="864b05af2d869ba73d61a9c5959e4531a141ab2bd7b217483671f625f9747faa")
    version("6.0.5", sha256="61332ef22b53c50c10faabfb965896a7d1ad4f3381f0f89643c820f28a60418e")
    version("6.0.4", sha256="c8f103d0da604e61f898dd729e738abd55261823db42f2826d647b53b4a41ed8")
    version("6.0.3", sha256="b0d522241805794d8af3a67d331ba063a16496c6fb6d365d48f7ed78ee1c3dcf")
    version("6.0.2", sha256="a13c26388cacccb684cd9f51109596a280c8186b7e95174d31ee7c5718e95c9d")
    version("6.0.1", sha256="8ede745a69351ea0f27fe0c48780d4efa37ff086135e129358ce09694957e8f9")
    version("6.0", sha256="5c2443a5538de52688efb55c27ab0539c1f5eb58c0cfd16a2b9fbb08fd81788e")

    requires("platform=linux")
    requires("%gcc@5.1:", when="@6.0:")

    depends_on("bash@4.2:", when="@6.0:")
    depends_on("flex@2.5.35:", when="@6.0:")
    depends_on("bison@2.0:", when="@6.0:")
    depends_on("util-linux@2.10o:", when="@6.0:")
    depends_on("kmod@13:", when="@6.0:")
    depends_on("e2fsprogs@1.41.4:", when="@6.0:")
    depends_on("procps@3.2.0:", when="@6.0:")
    depends_on("openssl@1.0.0:", when="@6.0:")
    depends_on("bc@1.06.95:", when="@6.0:")
    depends_on("cpio")
    depends_on("tar@1.28:", when="@6.5:")

    depends_on("gmake@3.82:", when="@6.1:")
    depends_on("gmake@3.81:", when="@6.0")

    depends_on("binutils@2.25:", when="@6.2:")
    depends_on("binutils@2.23:", when="@6.0:6.2")

    def setup_build_environment(self, env):
        env.set("KBUILD_OUTPUT", self.prefix)

    @run_before("build")
    def copy_kconfig(self):
        name = "kconfig_allconfig"
        copy2(f"{self.package_dir}/{name}", f"{self.build_directory}/{name}")

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            make("KCONFIG_ALLCONFIG=kconfig_allconfig", "allnoconfig")
            make("modules")

    def install(self, spec, prefix):
        install_tree(self.build_directory, self.prefix)
