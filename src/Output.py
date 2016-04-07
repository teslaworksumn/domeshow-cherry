
class ConsoleOutput:
    def close(self, message):
        print('Closing ConsoleOutput: {0}'.format(message))

    # Data is a dictionary of length 9 * 16 = 144
    # where each element is the 8-bit value for that channel
    def send(self, data):
        print('ConsoleOutput', len(data), data)

class FileOutput:
    def __init__(self, filename):
        self._filename = filename
        self._f = open(filename, 'a', 1)

    def close(self, message):
        print('Closing FileOutput {0}: {1}'.format(self._filename, message))
        self._f.close()

    # Data is a dictionary of length 9 * 16 = 144
    # where each element is the 8-bit value for that channel
    def send(self, data):
        output = ''
        for d in data:
            output += str(d) + ', '
        
        self._f.write(output + '\n')


