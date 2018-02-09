import os.path
import sys.path

PKG_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
sys.path.insert(0, PKG_ROOT)

from command import ReadMeGeneratorCmd


def test_if_the_readme_was_generated():
    class _ReadMeGeneratorCmd(ReadMeGeneratorCmd):
        files_to_process = {
        
        }

    new_content_f = NamedTemporaryFile()
    current_content = open(os.path.join(PKG_ROOT, 'README.md')).read()
    new_content = open()
