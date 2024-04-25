#
# Bitcoin Safe
# Copyright (C) 2024 Andreas Griffin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of version 3 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.html
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import bdkpython as bdk

from bitcoin_safe.util import serialized_to_hex

##### regtest
segwit_no_signature = serialized_to_hex(
    bdk.PartiallySignedTransaction(
        "cHNidP8BAIkBAAAAATqahH4QTEKfxm6qlALcWC5h8D9bjKFoW0VRfm4auf4aAAAAAAD9////AvQBAAAAAAAAIgAgsCBsnrRoOkUsY175u3Fa6vNXXwsSNbf4mDWFFvXODJH0AQAAAAAAACIAIPVnTHBKqnziIq5ov/TvQ8nNJYQ1MakbfdY7VMXIJbnpR8EmAAABAH0BAAAAAYMWmPX/X+Jq1QzTenGMmtvdeaMYEKYf7Nli0gzb+7C0AAAAAAD9////AugDAAAAAAAAIgAgHWI4I8UK5PLP+DtAXdlRI8Sts/PIRh1ksMD6iKlk/r6/GgAAAAAAABYAFNiY7EiZrTSaq0ipS+jFKXBQep4ON8EmAAEBK+gDAAAAAAAAIgAgHWI4I8UK5PLP+DtAXdlRI8Sts/PIRh1ksMD6iKlk/r4BBWlSIQIyOXzeZut4A5aUyMNWJy0Opx5iGruvdPBowW71rVQ1piEDDuRS5miVqUzK3RnF0adROAfU5jFNecF4zZ5TPebcRUMhAxU1ObeArGZ6bGPcb/KWg98LPu3Jj5wzMr9mDNI31ta0U64iBgIyOXzeZut4A5aUyMNWJy0Opx5iGruvdPBowW71rVQ1phixB43FVAAAgAEAAIAAAACAAAAAABUAAAAiBgMO5FLmaJWpTMrdGcXRp1E4B9TmMU15wXjNnlM95txFQxjRua98VAAAgAEAAIAAAACAAAAAABUAAAAiBgMVNTm3gKxmemxj3G/yloPfCz7tyY+cMzK/ZgzSN9bWtBiBe43+VAAAgAEAAIAAAACAAAAAABUAAAAAAQFpUiECwFSVDN1wlaOC4Xh3Vz8f1Fe1R3C9BnOEctx14BcM/vAhAvWDA1HgThJW6S0Buq4+ribWkdx/+Mq1qsmRr4XPMC1BIQNmWAeip+z4mEdQsVP1K0vLgB/pAvW5A/Vf5wi3tfahM1OuIgICwFSVDN1wlaOC4Xh3Vz8f1Fe1R3C9BnOEctx14BcM/vAYgXuN/lQAAIABAACAAAAAgAEAAAAVAAAAIgIC9YMDUeBOElbpLQG6rj6uJtaR3H/4yrWqyZGvhc8wLUEYsQeNxVQAAIABAACAAAAAgAEAAAAVAAAAIgIDZlgHoqfs+JhHULFT9StLy4Af6QL1uQP1X+cIt7X2oTMY0bmvfFQAAIABAACAAAAAgAEAAAAVAAAAAAEBaVIhAibQDjOdARwmI9G/ZnarEd23QZ/bskSSk5pzTsSbppqXIQNVWIlGZfiE5uzg9WV4Kkn7P+sdkX4mXCalj4wWRNH1dCED5H+E6OnZns/lomlsiSKclAcFlG7AZROwRk/voGCezotTriICAibQDjOdARwmI9G/ZnarEd23QZ/bskSSk5pzTsSbppqXGLEHjcVUAACAAQAAgAAAAIAAAAAAFAAAACICA1VYiUZl+ITm7OD1ZXgqSfs/6x2RfiZcJqWPjBZE0fV0GNG5r3xUAACAAQAAgAAAAIAAAAAAFAAAACICA+R/hOjp2Z7P5aJpbIkinJQHBZRuwGUTsEZP76Bgns6LGIF7jf5UAACAAQAAgAAAAIAAAAAAFAAAAAA="
    )
    .extract_tx()
    .serialize()
)
segwit_single_sig = "010000000001019cb676a43cae8e1da6747562701a035b8aceee75cc6347c57de0f4d0fa254a820000000000fdffffff0164410f00000000001600149aa1ed769e1762adfc764d2ef38567889201d0690247304402207ae957b6d062f718e6dbc30dacd40d63d2250e2443aaeea8f86fd81e59b5103a022048744dc57b57eaaad569d29fb26461ee6b711d003aa441c3d014d85ed86d1e6301210392357823bbe92638002d95e1c38bcdc9a0b5ab76985e5251805ea4e0771738716d000000"
segwit_multi_2_of_2 = "010000000001015c8823fdcc9e9bc91ff9940ee239fe996fa07ad89c3ccdde5e3a1821c3c378d10100000000fdffffff01ea959800000000002200206fcddedc8359bc8f6b05fea029d4132f8b6e565a71b5e6328062d2739c9efe02040047304402201e03594523d9c05d36b9fb3f08ec32bcaa326e911a46e9f0952820260cfa597f022056ffe39bb178123afe6df787adcb313e85bf5f6fd45b8c281313c8b38bc26f2901473044022013b4848619037ab19343ca2da4cbc051667eea3bcdbcaccd5a23c5a974709ecc02201e10190df7988667166e521ec6e6f105f81c469ae66810dce1c99915692cf120014752210335c6976c099c107397309683af1444a6167cc8ba96a509dcd4fb86698a22cb1a2103595a8a33f2b3764ae4c2644c1884f92502c68494d6c458e1134437467c2cd40152ae72000000"
segwit_multi_2_of_3 = "01000000000101dc01881f86b2736a00068dc99ca0782a0c7d7aa6b94129133ea767605a3cffc00000000000fdffffff01a1410f00000000002200202d07edfdff3fa6e48970f84b8414a3a06a10e45e40d188fe45077cc63a2ebc4e040047304402207e899bd4f26bbeb4a3c06d2784eb333ce20ac40f6e79173d38dea447437cdaf1022078a7991834759269850caee77acc57db78f64e6ac2288626d6f5dd40c0bed0750147304402201ee299aa46e305e3224f79656d1df18faf85ac6ef1faa3c4aed51cc83677105002200b83f00a8fbce256ac53edcc7a56100c9931fc692ab1d34477a052ba2c61e61b0169522103a560f5f719e215a2d38599a199f525b26ee00c29df4371d3198e6894a887ed712103b39b571343d300bebd5c0b2362ee188c38b300458eab69d2879e3aa29f5984302103e202e78f738fcb99c373ed449ca04b3e13e2db21b006e97036c42b44c958de2653ae6f000000"


p2sh_p2wsh_multi_2_of_2 = "010000000001014602a418f68753e91eee86a36dd385d40277df1b04ab1792a7e52565732019da0100000023220020f90e4756840cadca2ef0f13e57b967c972a8872b129bd05c553fb0c80a8a49fdffffffff02131000000000000017a9142fa4a9f13843446329aa3aeefbf27cf203c1fb2387391a01000000000017a914e167afacd0e15c0454a7149f9b5c22fdc74e3197870400473044022079572a24d29777c2c808de31e733b22b9833bcca261271f11d9b83a04171041402201fee49659698abc89e0d535da5b6bf1f33b80f7abf1d94a5853d0c72c1748d020147304402200571bf6fd455fe3d6883d48af86b9d4e66ab3c841a36e83515e54d60879e7b5602204d7ec8be700d31faf1e2e0f3deab102f714a72b9f8d881a031b70b16b6d248db01475221029f0789157b59d4740fc7f0908b3e9942151582f12e6c93d7ea744a7dee79618d2103e2e77bc3667310ed98e4e4cea3daa235340cebe00973ad82483ecc9bf106d19152ae00000000"
p2sh_p2wsh_multi_2_of_3 = "0100000000010220e1ce804e66d9f97f89e2bd938f5a0c55b57c8fe373e27cc14d9cdff28f94cf0000000023220020a99fb5ba91bd98919f5615485dae16297429a001befca07c6f14d7d073272096fdffffff20e1ce804e66d9f97f89e2bd938f5a0c55b57c8fe373e27cc14d9cdff28f94cf01000000232200201dd6b43a326dbfd5d8ff57d3952820653c8f19e2fe79e98f24105119f02ce808fdffffff028c9c07000000000017a9149cabbe62698d78a43c52cc3978ec82080d35ea6e87ee9d07000000000017a914107b5644f7739753c8af90e27cdb13f0b0d51d368704004730440220200d17ba000d2c0a6da34ad9d5c180bd997dae8aa5117c9439911f051ed6a3b802207357d82cc2c550669df223441b546430c6f713141e4bcbf31ad4a536b164173a0147304402201e79369a20aadb11d027e1d3875ca2e07ff8585218969b03535a1d1d434598c802203bd0ff754c651ceee209bf478ad522561c87f89c2a7992ff19cebb54a8d43d7901695221029d2929a3a1622c7407a0b53cbe6d0dae9d67642ad21511ea1fc8d08e1d6760b321037d3ddddb64656880d4eb6a6c47a745e93dc32e26e043410459b0a7d8d2218dd22103f42eb2d08ac833f9c87f99783fb4921b000456408612b54b2beff7647ac0d2df53ae040047304402207667570458d9b77fae71f3fbe40eb0b5e15f6771de9876a36708e8f4b16523f302200f88cfc82509858e6143a91815159b0f851bc10649b056f237ff1174d849cb5e0147304402200f458cc79d16d9e17297d011a4d32475fdd3e0352ad7a442481b93dc7d235e5d022003b05398b0cadb96cc24329dafd6a94f678a594c37f5165a788910843790ba080169522102c97dda0dc9aec44624240c7455710e239131315548728fd81a869f5cec24154421033533ad8c9af676ef85a0a8a28498db811f9b5f1469e311caa1dc374920be91d821038145aebe6db1cb4bc2c155701bf1b95ed639c066bd7999006afc3948fd4c6fed53ae74000000"

##### testnet

# 41f9ab73501b499fba50d02d42df6764ba0732e1775460a7c8f33543ad6736ef
testnet_P2PKH = "01000000019a61a3be3339c73b4b09918cc6780da91b063e46b2959f31108d9aa923198761000000006a47304402207fe1c21b75f354b0318f01363d59a6b3ca552c35374679cde352c82988c15b5802204d9c01468c78803feec60a0c1ecc63ceda0d32b8ca9372fed1dfd7b02552349f012102d7dbfde9b4c72c321c94ee8dbdd3fb901f5db5de93848fb6e8234be2dfe64308ffffffff02b11f1200000000001976a914f5693e59d064b7d4a37153eb7af25ecd9dcf68ee88ace8030000000000001976a9145756f1cbe64539627f6acb1f3187b72d9ba5e95688ac00000000"
# e9b3c180c23293e49f98668d8e960d9b79b66742aa8c70dfbf0757678a86a375
testnet_V0_P2WPKH = "02000000000101b510088211a0ce4f2a11ad3e2dd3bc58eb1546e82f2dca796c3440eae1fa63560000000000ffffffff0141df0000000000002251208106e6e5872ab0a55af23b350082177ee87cbee8e7a70143ac326aea8069bbe30247304402200267ab41d3f5e3820312ad8bcec6f9811d134be25d2097e91fd4fd45e02f3fcf02200fd2d96d1f27cdc2b62e80660c6da4c1b72f7880b8c1ee67c759e9abafd54cc1012102db1c507361a42f345ada94d250ff2c436d1231724494143ca759f0373bd4af8f00000000"
# d30b4f85d8852cdefe9ed3dc0b7a557fc5e8087e3db8bcacc20c5ceec0a91b8f
testnet_single_sig = "01000000012bdef9b8c5accc612b9a224ea10ed41766c81e9f5843cd307890c772e5a8c940030000006a4730440220727bd733c14c4acdce4d540ab7322f1d8cb2a7dfd52b01478a7e6b1f0bcdc133022061740b54a0391c16c1dcfa271fda36e8cd64c2edacc02135d6b149b91fd3e8370121037435c194e9b01b3d7f7a2802d6684a3af68d05bbf4ec8f17021980d777691f1dfdffffff040000000000000000536a4c5054325b4eafb44dafd23822773389a2ef237622d8d4301fce3ae4efc225d9d60178028d36b669d3ef162372c84d2f42af1a6db00930e0c15ad0353d9ede775024eb68c500276110000300276028001d4a10270000000000001976a914000000000000000000000000000000000000000088ac10270000000000001976a914000000000000000000000000000000000000000088ac85416c32000000001976a914ba27f99e007c7f605a8305e318c1abde3cd220ac88ac00000000"
# bb44e92d86bb93e0c07b12bb25fa22a140555acdf5c962ce842545bc71fc280b
testnet_tr_single = "02000000000101ca811846625fca3ea3128bb604865b7849d94e907d68a4d987f38c32b2e6ac3f0100000000ffffffff02400d03000000000022512071bf4399511a0483e9cfb4c9f730a74e89473009035c23527695d2e425f01275fcf3020000000000225120d96a99b93e0bf0318e780556f1ff51992e16d3a9c1587dc75552c52053fb6ad0014042a596571709ab7f769964bb90d519929c50e16fbcc320c54d4e247522e0bcf08a99482897b2a6a8d63b1256cdeb131bb1f4b781e90bbf30dc6f3284b8fad08d00000000"
