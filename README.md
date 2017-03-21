# cherry
The Doooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooome Controller

# What we're doing

This will send various patterns to light the Dome as **some binary protocol** to an Arduino (blossom).
This will run an interactive Python 3 shell to switch between running patterns and running a solid.

Patterns will each run for some period of time and then trigger a callback.
In pattern mode we will run patterns continuously. Patterns will run some
periodic signal internally and on each tick output their current state.

# How to run

```
make run
```

# Patterns

- Solid
- Full random
- Radar
- Sarlacc
- Tsunami
- Beach ball of death
- Counter rotating circles
- Solid fade
- Full random fade
- Spiral
- Sets of 5

# Coordinate system

5 layers vertically. layers 0, 1, 2 have 10 triangles. layers 3 and 4 have 5. 40 triangles total.

Horizontal index on top, Layers on side

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | x | x | x | x | x | x | x | x | x | x |
| 1 | x | x | x | x | x | x | x | x | x | x |
| 2 | x | x | x | x | x | x | x | x | x | x |
| 3 | x |   | x |   | x |   | x |   | x |   |
| 4 | x |   | x |   | x |   | x |   | x |   |

# License
This program uses pieces of https://github.com/teslaworksumn/enttec-usb-dmx-pro, which is under the MIT license. This license can be found in licenses/enttec_usb_dmx_pro
