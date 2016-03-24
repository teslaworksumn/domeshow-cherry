# cherry
The Doooooooooooooooooome Controller

# What the fuck we're doing

This will send various patterns to light the Dome as **some binary protocol** to an Arduino (blossom).
This will run an interactive Python 3 shell to switch between running patterns and running a solid.

Patterns will each run for some period of time and then trigger a callback.
In pattern mode we will run patterns continuously. Patterns will run some
periodic signal internally and on each tick output their current state.
Patterns should not take more than 5 sec, so they don't delay any switch to
solid/off state.

# CLI

```
cherry output=<device>
```

# Patterns

- Solid
- Full random
- Target
- Reverse target
- Rotatable horizontal wave
- Rotatable horizontal continuous wave
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

