class ConsoleOutput:
    def close(self, message):
        print('Closing ConsoleOutput: {0}'.format(message))

    # Data is a dictionary of length 9 * 16 = 144
    # where each element is the 8-bit value for that channel
    def send(self, data):
        print('ConsoleOutput', len(data), data)