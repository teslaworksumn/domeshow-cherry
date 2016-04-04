import argparse
import os
import src.Output as output

class UserInput:
    def __init__(self):
        args = self._parse()
        self.output = args.output
        #self.output = output.ConsoleOutput()

    # Parse command line arguments
    def _parse(self):
        parser = argparse.ArgumentParser(prog='cherry')
        parser.add_argument(
            '-o',
            '--output',
            default='/tmp/cherrylog',
            type=output.FileOutput)
        return parser.parse_args()


