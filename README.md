# tiny-chess

4KB Python chess engine with alpha-beta search, built for [make.fun tiny-chess-01](https://make.fun/bounty/tiny-chess-01).

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/4bill/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/4bill/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

## Engine

Alpha-beta search with material evaluation. Depth-limited minimax with alpha-beta pruning. Piece values: pawn=100, knight=320, bishop=330, rook=500, queen=900.

## Run

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 main.py
```

## License

MIT
