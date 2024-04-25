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

from bitcoin_safe.psbt_util import SimplePSBT

p2wsh_psbt_0_2of3 = bdk.PartiallySignedTransaction(
    "cHNidP8BAIkBAAAAATqahH4QTEKfxm6qlALcWC5h8D9bjKFoW0VRfm4auf4aAAAAAAD9////AvQBAAAAAAAAIgAgsCBsnrRoOkUsY175u3Fa6vNXXwsSNbf4mDWFFvXODJH0AQAAAAAAACIAIPVnTHBKqnziIq5ov/TvQ8nNJYQ1MakbfdY7VMXIJbnpR8EmAAABAH0BAAAAAYMWmPX/X+Jq1QzTenGMmtvdeaMYEKYf7Nli0gzb+7C0AAAAAAD9////AugDAAAAAAAAIgAgHWI4I8UK5PLP+DtAXdlRI8Sts/PIRh1ksMD6iKlk/r6/GgAAAAAAABYAFNiY7EiZrTSaq0ipS+jFKXBQep4ON8EmAAEBK+gDAAAAAAAAIgAgHWI4I8UK5PLP+DtAXdlRI8Sts/PIRh1ksMD6iKlk/r4BBWlSIQIyOXzeZut4A5aUyMNWJy0Opx5iGruvdPBowW71rVQ1piEDDuRS5miVqUzK3RnF0adROAfU5jFNecF4zZ5TPebcRUMhAxU1ObeArGZ6bGPcb/KWg98LPu3Jj5wzMr9mDNI31ta0U64iBgIyOXzeZut4A5aUyMNWJy0Opx5iGruvdPBowW71rVQ1phixB43FVAAAgAEAAIAAAACAAAAAABUAAAAiBgMO5FLmaJWpTMrdGcXRp1E4B9TmMU15wXjNnlM95txFQxjRua98VAAAgAEAAIAAAACAAAAAABUAAAAiBgMVNTm3gKxmemxj3G/yloPfCz7tyY+cMzK/ZgzSN9bWtBiBe43+VAAAgAEAAIAAAACAAAAAABUAAAAAAQFpUiECwFSVDN1wlaOC4Xh3Vz8f1Fe1R3C9BnOEctx14BcM/vAhAvWDA1HgThJW6S0Buq4+ribWkdx/+Mq1qsmRr4XPMC1BIQNmWAeip+z4mEdQsVP1K0vLgB/pAvW5A/Vf5wi3tfahM1OuIgICwFSVDN1wlaOC4Xh3Vz8f1Fe1R3C9BnOEctx14BcM/vAYgXuN/lQAAIABAACAAAAAgAEAAAAVAAAAIgIC9YMDUeBOElbpLQG6rj6uJtaR3H/4yrWqyZGvhc8wLUEYsQeNxVQAAIABAACAAAAAgAEAAAAVAAAAIgIDZlgHoqfs+JhHULFT9StLy4Af6QL1uQP1X+cIt7X2oTMY0bmvfFQAAIABAACAAAAAgAEAAAAVAAAAAAEBaVIhAibQDjOdARwmI9G/ZnarEd23QZ/bskSSk5pzTsSbppqXIQNVWIlGZfiE5uzg9WV4Kkn7P+sdkX4mXCalj4wWRNH1dCED5H+E6OnZns/lomlsiSKclAcFlG7AZROwRk/voGCezotTriICAibQDjOdARwmI9G/ZnarEd23QZ/bskSSk5pzTsSbppqXGLEHjcVUAACAAQAAgAAAAIAAAAAAFAAAACICA1VYiUZl+ITm7OD1ZXgqSfs/6x2RfiZcJqWPjBZE0fV0GNG5r3xUAACAAQAAgAAAAIAAAAAAFAAAACICA+R/hOjp2Z7P5aJpbIkinJQHBZRuwGUTsEZP76Bgns6LGIF7jf5UAACAAQAAgAAAAIAAAAAAFAAAAAA="
)
p2wsh_psbt_1_2of3 = bdk.PartiallySignedTransaction(
    "cHNidP8BAIkBAAAAATqahH4QTEKfxm6qlALcWC5h8D9bjKFoW0VRfm4auf4aAAAAAAD9////AlgCAAAAAAAAIgAgsCBsnrRoOkUsY175u3Fa6vNXXwsSNbf4mDWFFvXODJGQAQAAAAAAACIAIP0Ts8vJczsQLi1FvMD/RkcQMQqvjX5Uyh98yNm5KKhzR8EmAAABAH0BAAAAAYMWmPX/X+Jq1QzTenGMmtvdeaMYEKYf7Nli0gzb+7C0AAAAAAD9////AugDAAAAAAAAIgAgHWI4I8UK5PLP+DtAXdlRI8Sts/PIRh1ksMD6iKlk/r6/GgAAAAAAABYAFNiY7EiZrTSaq0ipS+jFKXBQep4ON8EmAAEBK+gDAAAAAAAAIgAgHWI4I8UK5PLP+DtAXdlRI8Sts/PIRh1ksMD6iKlk/r4iAgIyOXzeZut4A5aUyMNWJy0Opx5iGruvdPBowW71rVQ1pkcwRAIgKXaWbCmWs8FwBTQu67YBM3QShkYLE1Ag3LTyCJYp2FECIERAKtoA3GrLQED0QJn1N6E49FWMsQ+HRlbZ1UShmw9uAQEFaVIhAjI5fN5m63gDlpTIw1YnLQ6nHmIau6908GjBbvWtVDWmIQMO5FLmaJWpTMrdGcXRp1E4B9TmMU15wXjNnlM95txFQyEDFTU5t4CsZnpsY9xv8paD3ws+7cmPnDMyv2YM0jfW1rRTriIGAjI5fN5m63gDlpTIw1YnLQ6nHmIau6908GjBbvWtVDWmGLEHjcVUAACAAQAAgAAAAIAAAAAAFQAAACIGAw7kUuZolalMyt0ZxdGnUTgH1OYxTXnBeM2eUz3m3EVDGNG5r3xUAACAAQAAgAAAAIAAAAAAFQAAACIGAxU1ObeArGZ6bGPcb/KWg98LPu3Jj5wzMr9mDNI31ta0GIF7jf5UAACAAQAAgAAAAIAAAAAAFQAAAAABAWlSIQLAVJUM3XCVo4LheHdXPx/UV7VHcL0Gc4Ry3HXgFwz+8CEC9YMDUeBOElbpLQG6rj6uJtaR3H/4yrWqyZGvhc8wLUEhA2ZYB6Kn7PiYR1CxU/UrS8uAH+kC9bkD9V/nCLe19qEzU64iAgLAVJUM3XCVo4LheHdXPx/UV7VHcL0Gc4Ry3HXgFwz+8BiBe43+VAAAgAEAAIAAAACAAQAAABUAAAAiAgL1gwNR4E4SVuktAbquPq4m1pHcf/jKtarJka+FzzAtQRixB43FVAAAgAEAAIAAAACAAQAAABUAAAAiAgNmWAeip+z4mEdQsVP1K0vLgB/pAvW5A/Vf5wi3tfahMxjRua98VAAAgAEAAIAAAACAAQAAABUAAAAAAQFpUiEDHmZf8lOi367yritD9OBEELdnlxBDQJ8RJ6K4XOLEj4chAzEeI4tAmDMbcRnTWKK8hLiBt0B4SGwxjNipmdepFuElIQM0k/Q5IHXpN2wyoRpv4qs0vvdDu1faStzIJdnmttWKJ1OuIgIDHmZf8lOi367yritD9OBEELdnlxBDQJ8RJ6K4XOLEj4cYsQeNxVQAAIABAACAAAAAgAAAAAASAAAAIgIDMR4ji0CYMxtxGdNYoryEuIG3QHhIbDGM2KmZ16kW4SUYgXuN/lQAAIABAACAAAAAgAAAAAASAAAAIgIDNJP0OSB16TdsMqEab+KrNL73Q7tX2krcyCXZ5rbViicY0bmvfFQAAIABAACAAAAAgAAAAAASAAAAAA=="
)
p2wsh_psbt_0_1of1 = bdk.PartiallySignedTransaction(
    "cHNidP8BAH0BAAAAAaQmHDnvyNh3SMhYOptNUIbCEqkDyPUodsbshbyX6CS0BAAAAAD9////Ag7sSgAAAAAAFgAUgoFgSJlKKMq7iF1ZDLpqI6LlmrNwCAAAAAAAACIAIMXCKrkjoq9gCSacmVRW8+0qcwFyVWLQ3BLW2+NXV2FvScEmAAABAP3JAgIAAAABGju6Rif4mlNuTLV/JJ8FQXSUgrCxyBJqlomo3JzHVQoDAAAAAP3///8VtRExAAAAAAAWABSUfKgf8Gx4DtgCPlIV6SsF+I8FIZ5+QAAAAAAAFgAU7G63L/EV40CsWrmOVQAOV65hBUvMCVgAAAAAABepFMGNsv6av40/TGJOBGcbAjdCre5Gh+vLVQAAAAAAFgAUtwEGAFOlSqg/RCd8YV68tofpCAp+9EoAAAAAABYAFFOV8HAr7QNkAxVeo9K3poeglnA+poFaAAAAAAAWABSdWbWW0ehRFZbmTDHeo4g0P5ir+5S1SQAAAAAAGXapFDSAYPDISc0pYwcDv4jwuVIGhivgiKxfMlsAAAAAABYAFEIk7/vegOj1pmzNuNZAT11h7WuBV15PAAAAAAAXqRQ78S6GgebV361WMM6M/QRcPT1yj4dZZVsAAAAAABYAFKhkrTqxWd91WXwYtGORcNKuFl6QRJtZAAAAAAAWABS5WAprwfREeKtY0GSWEWUH/1fToNp0OQAAAAAAFgAUwy6wUb6UAvQ1qSTOMqZYzQoW0eEm0RazCAAAABYAFA/anu1dQBUKkO9aT8fFgtqOMpdRIRpXAAAAAAAZdqkU8pU2T3qf52tAfiNHPGx3rbJs/lCIrFK6LwAAAAAAFgAUA/DGv8DpP5AFAuCXfnkkxhnqP5GZDDoAAAAAABYAFCWRr8XphrCCO12RgcBKBDeGPDKGUkBQAAAAAAAWABQ74FXbsmiaoQKI20bzjnQwADs4LZiAPQAAAAAAFgAUMPAzgfc+NEQL+pJORoRmTqOLYi8Ccj8AAAAAABl2qRSzACucy7pGjjmIKQcya8TrDbBsj4isjIZSAAAAAAAWABS4SLqL0rXvVQUFqtTwd4b+3SHJQds4TgAAAAAAFgAUb4/333FxheUn7aTLWs8VCpZiLBgMviYAAQEffvRKAAAAAAAWABRTlfBwK+0DZAMVXqPSt6aHoJZwPiIGA4jB53vBV2PnTemvac24lRGSIc3BRfE3+eKvQzuTVdyuGL1fmV1UAACAAQAAgAAAAIAAAAAAFQAAAAAiAgMyP6YEUOBpARAkuF3hRA4AztrQpJbZ02gSnyo9Jivz5Ri9X5ldVAAAgAEAAIAAAACAAQAAABgAAAAAAA=="
)
p2wsh_psbt_1_1of1 = bdk.PartiallySignedTransaction(
    "cHNidP8BAH0BAAAAAaQmHDnvyNh3SMhYOptNUIbCEqkDyPUodsbshbyX6CS0BAAAAAD9////ApbwSgAAAAAAFgAU2JjsSJmtNJqrSKlL6MUpcFB6ng7oAwAAAAAAACIAIB1iOCPFCuTyz/g7QF3ZUSPErbPzyEYdZLDA+oipZP6+KMEmAAABAP3JAgIAAAABGju6Rif4mlNuTLV/JJ8FQXSUgrCxyBJqlomo3JzHVQoDAAAAAP3///8VtRExAAAAAAAWABSUfKgf8Gx4DtgCPlIV6SsF+I8FIZ5+QAAAAAAAFgAU7G63L/EV40CsWrmOVQAOV65hBUvMCVgAAAAAABepFMGNsv6av40/TGJOBGcbAjdCre5Gh+vLVQAAAAAAFgAUtwEGAFOlSqg/RCd8YV68tofpCAp+9EoAAAAAABYAFFOV8HAr7QNkAxVeo9K3poeglnA+poFaAAAAAAAWABSdWbWW0ehRFZbmTDHeo4g0P5ir+5S1SQAAAAAAGXapFDSAYPDISc0pYwcDv4jwuVIGhivgiKxfMlsAAAAAABYAFEIk7/vegOj1pmzNuNZAT11h7WuBV15PAAAAAAAXqRQ78S6GgebV361WMM6M/QRcPT1yj4dZZVsAAAAAABYAFKhkrTqxWd91WXwYtGORcNKuFl6QRJtZAAAAAAAWABS5WAprwfREeKtY0GSWEWUH/1fToNp0OQAAAAAAFgAUwy6wUb6UAvQ1qSTOMqZYzQoW0eEm0RazCAAAABYAFA/anu1dQBUKkO9aT8fFgtqOMpdRIRpXAAAAAAAZdqkU8pU2T3qf52tAfiNHPGx3rbJs/lCIrFK6LwAAAAAAFgAUA/DGv8DpP5AFAuCXfnkkxhnqP5GZDDoAAAAAABYAFCWRr8XphrCCO12RgcBKBDeGPDKGUkBQAAAAAAAWABQ74FXbsmiaoQKI20bzjnQwADs4LZiAPQAAAAAAFgAUMPAzgfc+NEQL+pJORoRmTqOLYi8Ccj8AAAAAABl2qRSzACucy7pGjjmIKQcya8TrDbBsj4isjIZSAAAAAAAWABS4SLqL0rXvVQUFqtTwd4b+3SHJQds4TgAAAAAAFgAUb4/333FxheUn7aTLWs8VCpZiLBgMviYAAQEffvRKAAAAAAAWABRTlfBwK+0DZAMVXqPSt6aHoJZwPiIGA4jB53vBV2PnTemvac24lRGSIc3BRfE3+eKvQzuTVdyuGL1fmV1UAACAAQAAgAAAAIAAAAAAFQAAAAEHAAEIawJHMEQCIES4GSlpjaAzwcOwQcfwXrKUSatQ1EJGqPUfokLrpPOmAiBiQ4hOQWCs3RCYiSJFBrke9cDfOv3MWwfbLpBJTwiFIQEhA4jB53vBV2PnTemvac24lRGSIc3BRfE3+eKvQzuTVdyuACICAkhCjgk5sNSHM7qWEB5GBE1wOgzX8TgsX8WvQ29TKmwmGL1fmV1UAACAAQAAgAAAAIABAAAAFwAAAAAA"
)
p2wsh_psbt_0_2of2 = bdk.PartiallySignedTransaction(
    "cHNidP8BAF4BAAAAAVyII/3MnpvJH/mUDuI5/plvoHrYnDzN3l46GCHDw3jRAQAAAAD9////AeqVmAAAAAAAIgAgb83e3INZvI9rBf6gKdQTL4tuVlpxteYygGLSc5ye/gJyAAAAAAEA9gIAAAAAAQGq9XxjX3p/EmPGaAvQ6eSmb0v+HFDbcPishlCQfexzqAAAAAAA/f///wLbWm0pAQAAACJRIEbZRee2bMwBN832yNf6QSg7KlmQrfCgzWkh8akScJY2gJaYAAAAAAAiACCxLbtsPZ/hUDNT0mxCFTmuIicAVyFHrKpPnAFt8ZPcegJHMEQCICtbM+5oCgo/HJ1cKYMGlKpcpD2vXP7EPVf712zir3cXAiAgEuWrr5aQ7p0Rpk22Pu/Uz1jlMI9d8uW60LpLRPcsawEhAvw/tdT/dxVawrrhag+GZv2Iget2sSDkQWGWukU2j7RacQAAAAEBK4CWmAAAAAAAIgAgsS27bD2f4VAzU9JsQhU5riInAFchR6yqT5wBbfGT3HoBBUdSIQM1xpdsCZwQc5cwloOvFESmFnzIupalCdzU+4ZpiiLLGiEDWVqKM/KzdkrkwmRMGIT5JQLGhJTWxFjhE0Q3Rnws1AFSriIGAzXGl2wJnBBzlzCWg68URKYWfMi6lqUJ3NT7hmmKIssaHCWX5CkwAACAAQAAgAAAAIACAACAAAAAAAAAAAAiBgNZWooz8rN2SuTCZEwYhPklAsaElNbEWOETRDdGfCzUARxbNzD7MAAAgAEAAIAAAACAAgAAgAAAAAAAAAAAAAEBR1IhAnKcTGCT2jP+TCH/UYHolu3ifas7ZNqf5wTR3MNhbdHqIQKQZYWFA77hl8m6W7L183FxzG/jYpI2Ht5KqfMb1zKHiVKuIgICcpxMYJPaM/5MIf9RgeiW7eJ9qztk2p/nBNHcw2Ft0eocWzcw+zAAAIABAACAAAAAgAIAAIAAAAAAAgAAACICApBlhYUDvuGXybpbsvXzcXHMb+NikjYe3kqp8xvXMoeJHCWX5CkwAACAAQAAgAAAAIACAACAAAAAAAIAAAAA"
)


p2sh_0_2of3 = bdk.PartiallySignedTransaction(
    "cHNidP8BAHMBAAAAAXO5Dew7+siJ2ZbUmwYt8qPwrkMh1yF3Brn8BD3avomLAQAAAAD9////AiChBwAAAAAAF6kUAstwBtQji+/6aEjklauNDtnR+0GHrJ8HAAAAAAAXqRT4Sas3geGPcM0NebajO6yYiiQb+4d1AAAAAAEA9wIAAAAAAQFHTtb7A/Z6cMGCWH64mZ/9cGEni1ObXyFkNHCAsH/qqAAAAAAXFgAUF8LkWabVbU1J1xhc16gPjSda4RP9////Akts5ykBAAAAF6kUXNlHny5QV0SRQV07ArvAZJKSNyuHQEIPAAAAAAAXqRTl9Jjc1j6E65hBhAjhOEZhB9gHYIcCRzBEAiAh2GCYtPNPIxaFb34KaE6DtsorSL7CIzKpYk6lF1zYOwIgN7s1YRIkWisq13rH7b/YxmwwYTIi2tS+rfYZv5vdod8BIQPoFG37UHDyoY/jQO7fER0bUIHHBLsCuWRqaWnWj3PTw3QAAAABBGlSIQNZsdQeMRWvnvbpsDXjHDzO2I1oGqOFmjOM2XEq7k4AhiEDgD/B7gYCmN9KT43xIvvy1Ob+ec6GEFvwGuRkki8f1H4hA4xoO95jhKYDRXKV1vbKqpOOCmlFeQBNFa2LNNLlOImbU64iBgNZsdQeMRWvnvbpsDXjHDzO2I1oGqOFmjOM2XEq7k4AhhiylC7zVAAAgAEAAIAAAACAAAAAAAAAAAAiBgOAP8HuBgKY30pPjfEi+/LU5v55zoYQW/Aa5GSSLx/Ufhh5ERhfVAAAgAEAAIAAAACAAAAAAAAAAAAiBgOMaDveY4SmA0Vyldb2yqqTjgppRXkATRWtizTS5TiJmxiScB+cVAAAgAEAAIAAAACAAAAAAAAAAAAAAQBpUiECfGlLBOepJfvgtsMi/R81uw7Auj9fWAJruF5XgiOB+aIhAoMYExsC4fl2aIt+FaopblzHVzYADabsSU/ZSJpl2/+rIQMuyQYgxFCRP7YT5h+7pBVg6z3WQePT2Qq5HwmhHy6dlFOuIgICfGlLBOepJfvgtsMi/R81uw7Auj9fWAJruF5XgiOB+aIYeREYX1QAAIABAACAAAAAgAAAAAABAAAAIgICgxgTGwLh+XZoi34VqiluXMdXNgANpuxJT9lImmXb/6sYknAfnFQAAIABAACAAAAAgAAAAAABAAAAIgIDLskGIMRQkT+2E+Yfu6QVYOs91kHj09kKuR8JoR8unZQYspQu81QAAIABAACAAAAAgAAAAAABAAAAAAEAaVIhAmPKbA+7cgE0w9YFb3dJaPUEmClKtHVNQMwUo2Ta4R0aIQJr79EtpZMB8xP4+DAmya9Eb1m9EtdSAJb4545eX5oC3iEDHN8oRK2JmwevEXC4e7NWTKewZ3rdAUhEPSdo8DX/ildTriICAmPKbA+7cgE0w9YFb3dJaPUEmClKtHVNQMwUo2Ta4R0aGHkRGF9UAACAAQAAgAAAAIAAAAAAAgAAACICAmvv0S2lkwHzE/j4MCbJr0RvWb0S11IAlvjnjl5fmgLeGLKULvNUAACAAQAAgAAAAIAAAAAAAgAAACICAxzfKEStiZsHrxFwuHuzVkynsGd63QFIRD0naPA1/4pXGJJwH5xUAACAAQAAgAAAAIAAAAAAAgAAAAA="
)
p2sh_1_2of3 = bdk.PartiallySignedTransaction(
    "cHNidP8BAHMBAAAAAXO5Dew7+siJ2ZbUmwYt8qPwrkMh1yF3Brn8BD3avomLAQAAAAD9////AiChBwAAAAAAF6kUAstwBtQji+/6aEjklauNDtnR+0GHrJ8HAAAAAAAXqRT4Sas3geGPcM0NebajO6yYiiQb+4d1AAAAAAEA9wIAAAAAAQFHTtb7A/Z6cMGCWH64mZ/9cGEni1ObXyFkNHCAsH/qqAAAAAAXFgAUF8LkWabVbU1J1xhc16gPjSda4RP9////Akts5ykBAAAAF6kUXNlHny5QV0SRQV07ArvAZJKSNyuHQEIPAAAAAAAXqRTl9Jjc1j6E65hBhAjhOEZhB9gHYIcCRzBEAiAh2GCYtPNPIxaFb34KaE6DtsorSL7CIzKpYk6lF1zYOwIgN7s1YRIkWisq13rH7b/YxmwwYTIi2tS+rfYZv5vdod8BIQPoFG37UHDyoY/jQO7fER0bUIHHBLsCuWRqaWnWj3PTw3QAAAABBGlSIQNZsdQeMRWvnvbpsDXjHDzO2I1oGqOFmjOM2XEq7k4AhiEDgD/B7gYCmN9KT43xIvvy1Ob+ec6GEFvwGuRkki8f1H4hA4xoO95jhKYDRXKV1vbKqpOOCmlFeQBNFa2LNNLlOImbU64iBgNZsdQeMRWvnvbpsDXjHDzO2I1oGqOFmjOM2XEq7k4AhhiylC7zVAAAgAEAAIAAAACAAAAAAAAAAAAiBgOAP8HuBgKY30pPjfEi+/LU5v55zoYQW/Aa5GSSLx/Ufhh5ERhfVAAAgAEAAIAAAACAAAAAAAAAAAAiBgOMaDveY4SmA0Vyldb2yqqTjgppRXkATRWtizTS5TiJmxiScB+cVAAAgAEAAIAAAACAAAAAAAAAAAAAAQBpUiECfGlLBOepJfvgtsMi/R81uw7Auj9fWAJruF5XgiOB+aIhAoMYExsC4fl2aIt+FaopblzHVzYADabsSU/ZSJpl2/+rIQMuyQYgxFCRP7YT5h+7pBVg6z3WQePT2Qq5HwmhHy6dlFOuIgICfGlLBOepJfvgtsMi/R81uw7Auj9fWAJruF5XgiOB+aIYeREYX1QAAIABAACAAAAAgAAAAAABAAAAIgICgxgTGwLh+XZoi34VqiluXMdXNgANpuxJT9lImmXb/6sYknAfnFQAAIABAACAAAAAgAAAAAABAAAAIgIDLskGIMRQkT+2E+Yfu6QVYOs91kHj09kKuR8JoR8unZQYspQu81QAAIABAACAAAAAgAAAAAABAAAAAAEAaVIhAmPKbA+7cgE0w9YFb3dJaPUEmClKtHVNQMwUo2Ta4R0aIQJr79EtpZMB8xP4+DAmya9Eb1m9EtdSAJb4545eX5oC3iEDHN8oRK2JmwevEXC4e7NWTKewZ3rdAUhEPSdo8DX/ildTriICAmPKbA+7cgE0w9YFb3dJaPUEmClKtHVNQMwUo2Ta4R0aGHkRGF9UAACAAQAAgAAAAIAAAAAAAgAAACICAmvv0S2lkwHzE/j4MCbJr0RvWb0S11IAlvjnjl5fmgLeGLKULvNUAACAAQAAgAAAAIAAAAAAAgAAACICAxzfKEStiZsHrxFwuHuzVkynsGd63QFIRD0naPA1/4pXGJJwH5xUAACAAQAAgAAAAIAAAAAAAgAAAAA="
)
p2sh_2_2of3 = bdk.PartiallySignedTransaction(
    "cHNidP8BAHMBAAAAAXO5Dew7+siJ2ZbUmwYt8qPwrkMh1yF3Brn8BD3avomLAQAAAAD9////AiChBwAAAAAAF6kUAstwBtQji+/6aEjklauNDtnR+0GHrJ8HAAAAAAAXqRT4Sas3geGPcM0NebajO6yYiiQb+4d1AAAAAAEA9wIAAAAAAQFHTtb7A/Z6cMGCWH64mZ/9cGEni1ObXyFkNHCAsH/qqAAAAAAXFgAUF8LkWabVbU1J1xhc16gPjSda4RP9////Akts5ykBAAAAF6kUXNlHny5QV0SRQV07ArvAZJKSNyuHQEIPAAAAAAAXqRTl9Jjc1j6E65hBhAjhOEZhB9gHYIcCRzBEAiAh2GCYtPNPIxaFb34KaE6DtsorSL7CIzKpYk6lF1zYOwIgN7s1YRIkWisq13rH7b/YxmwwYTIi2tS+rfYZv5vdod8BIQPoFG37UHDyoY/jQO7fER0bUIHHBLsCuWRqaWnWj3PTw3QAAAABBGlSIQNZsdQeMRWvnvbpsDXjHDzO2I1oGqOFmjOM2XEq7k4AhiEDgD/B7gYCmN9KT43xIvvy1Ob+ec6GEFvwGuRkki8f1H4hA4xoO95jhKYDRXKV1vbKqpOOCmlFeQBNFa2LNNLlOImbU64iBgNZsdQeMRWvnvbpsDXjHDzO2I1oGqOFmjOM2XEq7k4AhhiylC7zVAAAgAEAAIAAAACAAAAAAAAAAAAiBgOAP8HuBgKY30pPjfEi+/LU5v55zoYQW/Aa5GSSLx/Ufhh5ERhfVAAAgAEAAIAAAACAAAAAAAAAAAAiBgOMaDveY4SmA0Vyldb2yqqTjgppRXkATRWtizTS5TiJmxiScB+cVAAAgAEAAIAAAACAAAAAAAAAAAAAAQBpUiECfGlLBOepJfvgtsMi/R81uw7Auj9fWAJruF5XgiOB+aIhAoMYExsC4fl2aIt+FaopblzHVzYADabsSU/ZSJpl2/+rIQMuyQYgxFCRP7YT5h+7pBVg6z3WQePT2Qq5HwmhHy6dlFOuIgICfGlLBOepJfvgtsMi/R81uw7Auj9fWAJruF5XgiOB+aIYeREYX1QAAIABAACAAAAAgAAAAAABAAAAIgICgxgTGwLh+XZoi34VqiluXMdXNgANpuxJT9lImmXb/6sYknAfnFQAAIABAACAAAAAgAAAAAABAAAAIgIDLskGIMRQkT+2E+Yfu6QVYOs91kHj09kKuR8JoR8unZQYspQu81QAAIABAACAAAAAgAAAAAABAAAAAAEAaVIhAmPKbA+7cgE0w9YFb3dJaPUEmClKtHVNQMwUo2Ta4R0aIQJr79EtpZMB8xP4+DAmya9Eb1m9EtdSAJb4545eX5oC3iEDHN8oRK2JmwevEXC4e7NWTKewZ3rdAUhEPSdo8DX/ildTriICAmPKbA+7cgE0w9YFb3dJaPUEmClKtHVNQMwUo2Ta4R0aGHkRGF9UAACAAQAAgAAAAIAAAAAAAgAAACICAmvv0S2lkwHzE/j4MCbJr0RvWb0S11IAlvjnjl5fmgLeGLKULvNUAACAAQAAgAAAAIAAAAAAAgAAACICAxzfKEStiZsHrxFwuHuzVkynsGd63QFIRD0naPA1/4pXGJJwH5xUAACAAQAAgAAAAIAAAAAAAgAAAAA="
)


# Test function for psbt_0_1of1
def test_psbt_0_1of1():
    psbt = SimplePSBT.from_psbt(p2wsh_psbt_0_1of1)
    input_ = psbt.inputs[0]
    assert len(input_.partial_sigs) == 0, "psbt_0_1of1 should have 0 signatures"
    assert not input_.is_fully_signed(), "psbt_0_1of1 should not be fully signed"


# Test function for psbt_1_1of1
def test_psbt_1_1of1():
    psbt = SimplePSBT.from_psbt(p2wsh_psbt_1_1of1)
    input_ = psbt.inputs[0]
    assert input_.final_script_witness, "psbt_1_1of1 should have 1 signature"
    assert input_.is_fully_signed(), "psbt_1_1of1 should be fully signed"


# Test function for psbt_1_2of3
def test_psbt_1_2of3():
    psbt = SimplePSBT.from_psbt(p2wsh_psbt_1_2of3)
    input_ = psbt.inputs[0]
    assert len(input_.partial_sigs) == 1, "psbt_1_2of3 should have 1 signature"
    assert (
        not input_.is_fully_signed()
    ), "psbt_1_2of3 should not be fully signed considering it's a 2 of 3 multisig"


# Test function for psbt_0_2of3
def test_psbt_0_2of3():
    psbt = SimplePSBT.from_psbt(p2wsh_psbt_0_2of3)
    input_ = psbt.inputs[0]
    assert len(input_.partial_sigs) == 0, "psbt_0_2of3 should have 0 signatures"
    assert (
        not input_.is_fully_signed()
    ), "psbt_0_2of3 should not be fully signed considering it's a 2 of 3 multisig"


def test_psbt_optional_fields():
    psbt = SimplePSBT.from_psbt(p2wsh_psbt_0_2of2)
    assert psbt.inputs[0].non_witness_utxo
    psbt.inputs[0].non_witness_utxo.get("input", {}) == [
        {
            "previous_output": "a873ec7d905086acf870db501cfe4b6fa6e4e9d00b68c663127f7a5f637cf5aa:0",
            "script_sig": "",
            "sequence": 4294967293,
            "witness": [
                "304402202b5b33ee680a0a3f1c9d5c29830694aa5ca43daf5cfec43d57fbd76ce2af771702202012e5abaf9690ee9d11a64db63eefd4cf58e5308f5df2e5bad0ba4b44f72c6b01",
                "02fc3fb5d4ff77155ac2bae16a0f8666fd8881eb76b120e4416196ba45368fb45a",
            ],
        }
    ]

    psbt.outputs[0].value == 9999850
    psbt.outputs[0].script_pubkey == "00206fcddedc8359bc8f6b05fea029d4132f8b6e565a71b5e6328062d2739c9efe02"
    psbt.outputs[
        0
    ].witness_script == "522102729c4c6093da33fe4c21ff5181e896ede27dab3b64da9fe704d1dcc3616dd1ea21029065858503bee197c9ba5bb2f5f37171cc6fe36292361ede4aa9f31bd732878952ae"

    psbt.outputs[0].bip32_derivation[0].__dict__ == {
        "fingerprint": "5B3730FB",
        "pubkey": "02729c4c6093da33fe4c21ff5181e896ede27dab3b64da9fe704d1dcc3616dd1ea",
        "derivation_path": "m/48'/1'/0'/2'/0/2",
        "label": "",
    }
    psbt.outputs[0].bip32_derivation[1].__dict__ == {
        "fingerprint": "2597E429",
        "pubkey": "029065858503bee197c9ba5bb2f5f37171cc6fe36292361ede4aa9f31bd7328789",
        "derivation_path": "m/48'/1'/0'/2'/0/2",
        "label": "",
    }


def test_p2sh():
    psbt = SimplePSBT.from_psbt(p2sh_0_2of3)
    psbt
