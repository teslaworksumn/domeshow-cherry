import threading
import time


class CtsThread:

    def __init__(self, output):
        self._output = output
        self._cts_magic = [0xef, 0xbe, 0xad, 0xde]
        self._count = 0
        self.cts_state = False
        self._cts_thread = threading.Thread(target=self._check_cts, name="CtsThread")
        self._cts_thread.start()

    def set_cts(self, c):
        self.cts_state = c

    def _check_cts(self):
        while True:
            byte = self._output.read()
            if byte == self._cts_magic[self._count].to_bytes(1, byteorder='big'):
                self._count += 1
            if self._count >= len(self._cts_magic):
                self._count = 0
                self.cts_state = True
            time.sleep(0.02)


