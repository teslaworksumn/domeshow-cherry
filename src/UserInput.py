import argparse
import os


class UserInput:
    def __init__(self):
        args = self._parse()
        self._output = args.output

    def get_output(self):
        return self._output

    def _valid_device(self, dev):
        if os.path.isfile(dev):
            return dev
        else:
            raise TypeError(dev + ' is not a regular file.')

    # Parse command line arguments
    def _parse(self):
        parser = argparse.ArgumentParser(prog='./Cherry.py')
        parser.add_argument('-o', '--output', default='/dev/null', type=self._valid_device)
        return parser.parse_args()


