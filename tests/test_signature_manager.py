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

import logging
import tempfile
from pathlib import Path

from bitcoin_safe.signature_manager import KnownGPGKeys, SignatureVerifyer

logger = logging.getLogger(__name__)


def test_download_manifest_and_verify():
    manager = SignatureVerifyer(list_of_known_keys=KnownGPGKeys.all())

    with tempfile.TemporaryDirectory() as tempdir:
        logger.debug(f"tempdir {tempdir}")
        sig_filename = manager.get_signature_from_web(Path(tempdir) / "Sparrow-1.8.4-x86_64.dmg")
        logger.debug(f"sig_filename {sig_filename}")
        assert sig_filename == Path(tempdir) / "sparrow-1.8.4-manifest.txt.asc"
        assert manager.is_signature_file_available(Path(tempdir) / "sparrow-1.8.4-manifest.txt")
        assert manager._verify_file(Path(tempdir) / "sparrow-1.8.4-manifest.txt", signature_file=sig_filename)
