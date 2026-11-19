# tiny-chess-4bill

4KB Python chess engine for [make.fun tiny-chess-01](https://make.fun/bounty/tiny-chess-01).

## Engine

Alpha-beta search with material evaluation. Depth-limited minimax with alpha-beta pruning. Evaluates piece values: pawn=100, knight=320, bishop=330, rook=500, queen=900.

## Run

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 main.py
```

## License

MIT