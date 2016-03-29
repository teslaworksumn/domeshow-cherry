

class Output:
    def __init__(self, device):
        self.device = device

    # Data is a dictionary of length 120 (40 lights * 3 channels)
    # where each element is the 8-bit value for that channel
    def send(self, data):
        pass