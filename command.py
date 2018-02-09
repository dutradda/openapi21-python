import os.path

from setuptools import Command
from six import iteritems

root_dir = os.path.dirname(os.path.abspath(__file__))


class Jinja2ProcessorCmd(Command):

    user_options = []
    path = root_dir
    files_to_process = {}
    auto_escape = []

    def run(self):
        import jinja2

        jinja2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.path),
            autoescape=jinja2.select_autoescape(self.auto_escape)
        )

        for jinja_file, output_file in iteritems(self.files_to_process):
            output_file = self._normalize_output_file(output_file, jinja_file)

    def _normalize_output_file(self, output_file, jinja_file):
        if not output_file:
            if not jinja_file.endswith('.j2'):
                raise ValueError("The 'files_to_process' property without"
                                 " an output file is only valid with a"
                                 " jinja file with a '.j2' extension")
            else:
                output_file = jinja_file[:-3]

        return output_file

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class ReadMeGeneratorCmd(Jinja2ProcessorCmd):

    files_to_process = {'README.md.j2': ''}
    auto_escape = []
