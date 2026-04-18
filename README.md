# Oregon Trail - Brainfuck & Malbolge Edition

A playable Oregon Trail game built with esoteric programming languages. Make decisions, manage resources, and survive the frontier—with a touch of computational madness.

## Quick Start

```bash
python3 oregon_trail_playable.py
```

Then follow the prompts and make choices to guide your party westward.

## How to Play

### Goal
Reach Oregon (2000 miles) while keeping your party alive.

### Each Day You Choose:

| Option | Miles | Food | Effect |
|--------|-------|------|--------|
| **[1] Push Hard** | +30 | -5 | Aggressive travel, risky |
| **[2] Travel Normal** | +15 | -3 | Standard pace, steady |
| **[3] Hunt** | +5 | +20-50 | Gain food, costs ammo (-10) |
| **[4] Rest** | +2 | -2 | Restore health, slow progress |

### Resources

- **Food**: Consumed each day. 0 = starvation = death
- **Ammo**: Used for hunting. Impacts hunting success
- **Health**: 5 is max. Illness or hardship reduces it. 0 = game over
- **Miles**: Track progress toward Oregon (need 2000)

### Random Events

Malbolge's chaos generator creates unpredictable events:
- **DYSENTERY** (-20 food)
- **SUCCESSFUL HUNT** (+30 food)
- **RIVER CROSSING** (-5 ammo)
- **FRIENDLY NATIVES** (+10 food, +5 ammo)
- **WAGON WHEEL BROKE** (-10 food)
- **BUFFALO STAMPEDE** (-10 ammo)
- **SNAKE BITE** (-15 food)
- **FOUND SUPPLIES** (+25 food)

Events occur randomly (~40% chance per day) based on Malbolge XOR chaos operations.

## Win/Lose Conditions

**WIN**: Reach 2000 miles
```
🎉 YOU MADE IT TO OREGON!
   Survived N days with 5 party members
```

**LOSE**: 
- Food reaches 0 → Starvation
- Health reaches 0 → Illness
- Quit early → Abandoned trail

## Strategy Tips

- **Hunt early**: Build food reserves before long stretches
- **Don't waste ammo**: You need it for hunting
- **Balance pace**: Pushing hard costs more food but reaches Oregon faster
- **Monitor health**: Rest when sick to avoid death spirals
- **Plan ahead**: You need enough food to last 2000 miles at ~3-5 per day minimum

## Technical Details

### Memory Architecture

```
Cell 0: Food supply (0-500)
Cell 1: Ammo (0-100)
Cell 2: Health (0-5)
Cell 3: Miles traveled (0-2000)
Cell 4: Day counter
Cell 5-10: Event state
```

### Malbolge Event Generation

The game uses Malbolge's "crazy operator" (XOR chaos) to generate events:

```python
malbolge_chaos = ((day ^ miles) + (food % 256)) % num_events
```

This creates pseudo-random but deterministic event sequences based on game state.

### Brainfuck Heritage

The original game logic (in `oregon_trail.bf`) uses pure Brainfuck:
- `>` and `<` for memory navigation
- `+` and `-` for value manipulation
- `[` and `]` for loops
- `.` for output
- 8 commands total for a complete game engine

The Python version replicates this memory model while adding player interaction.

## Files

- **oregon_trail_playable.py** - The interactive game (run this)
- **oregon_trail.bf** - Pure Brainfuck implementation
- **bf_interpreter.py** - Brainfuck interpreter
- **malbolge_rng.mal** - Malbolge RNG source
- **README.md** - This file

## Example Playthrough

```
OREGON TRAIL - BRAINFUCK & MALBOLGE EDITION
     An esoteric descent into madness

┌─ DAY 1 ─────────────────────────────────────┐
│ Miles: 15/2000
│ Food: 497  |  Ammo: 100  |  Health: 5
│ Party Members: 5
└──────────────────────────────────────────────────┘

What do you do?
  [1] Push hard  (30 mi, -5 food)
  [2] Travel normal  (15 mi, -3 food)
  [3] Hunt  (+food, -ammo, +5 mi)
  [4] Rest  (+health, -2 food, +2 mi)
  [Q] Quit

Choose (1-4 or Q): 3
[EVENT] SUCCESSFUL HUNT!

┌─ DAY 2 ─────────────────────────────────────┐
│ Miles: 20/2000
│ Food: 533  |  Ammo: 90  |  Health: 5
│ Party Members: 5
└──────────────────────────────────────────────────┘
```

## Why Brainfuck + Malbolge?

**Brainfuck**
- Turing-complete but uses only 8 commands
- Turns simple tasks into complex memory operations
- Perfect for turn-based game loops
- Makes resource tracking absurdly complicated

**Malbolge**
- Designed to be almost impossible to program in
- Named after the 8th circle of Hell in Dante's Inferno
- Uses rotation operations that scramble program flow
- Even "Hello World" is typically generated, not hand-written
- Ideal for chaotic, unpredictable event generation

The combination creates a game that's technically functional but spiritually chaotic.

## FAQ

**Q: Can I win?**
A: Yes. Reach 2000 miles without dying.

**Q: Is there a time limit?**
A: No. Play as many days as you need, but food consumption is constant.

**Q: Can I save/load?**
A: Not currently. Each playthrough is fresh.

**Q: Why Brainfuck and Malbolge?**
A: Because normal programming languages are too boring.

**Q: Will my party members actually die?**
A: Health drops when you face hardship. Health = 0 means game over.

## Running on Different Systems

### Linux/Mac
```bash
python3 oregon_trail_playable.py
```

### Windows
```bash
python3 oregon_trail_playable.py
```
or
```bash
py oregon_trail_playable.py
```

## Credits

Game design: Esoteric language madness
Implementation: Brainfuck (core logic) + Malbolge (chaos)
Python wrapper: For sanity's sake

---

*"The Oregon Trail wasn't built by normal people using normal languages. This is what happens when you let Brainfuck and Malbolge near a video game."*
