import sys


class UserInput:

    def __init__(self):
        self._outputdevice = '/dev/null'
        self._parse_args(sys.argv)

    def get_output_device(self):
        return self._outputdevice

    def _parse_args(self, args):
        if len(args) != 2 or args[1][:7] != 'output=':
            print("Error: Invalid output specified:")
            self._print_usage()
        else:
            # TODO check if device is valid and/or exists
            self._outputdevice = args[7:]

    def _print_usage(self):
        usage = \
"""
Usage:

$ ./Cherry.py output=<location>

where <location> is the location of the output device (e.g. /dev/USB0)
"""
        print(usage)
