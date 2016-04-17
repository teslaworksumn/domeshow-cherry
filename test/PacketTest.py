import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import src.output.SerialOutput as SerialOutput

def test_packet_write():
    data = [i for i in range(144)]
    packet = SerialOutput._create_packet(data)
    with open('packet_test', 'wb') as f:
        f.write(packet.bytes)

test_packet_write()

