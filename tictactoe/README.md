# Unbeatable tic tac toe

## Approach
* In the following numbered order, the conditions are checked. When one of them is `true`, the square under which the `true` condition occurs is returned as the computer's move.
1. Offensive: check if computer can win in one
2. Defensive: check if human can win in one
3. Offensive: check if computer can set up a fork
4. Defensive: check if the human can fork
    - If it can set up 1 fork or the human has control of the center square
        - move to the sole blocking square that blocks
    - If it can set up 2 or more forks
        - choose a random side to move to
5. Neutral: check if center is free
6. Neutral: check for a random empty square

### Example Fork
```
|x|o|o|
| |o| |
| |x| |
```
Above, each player has moved twice. First, 'o' moved to the topc enter, 'x' chose top left, 'o' did center to try and get 3 in a row, 'x' blocks at bottom center, 'o' trues to win a gain with top right. 
'x' can now move to bottom left, setting up two unblocked 2 in a rows at once, guarenteeing a win on its next move.

### Notes
* Board is represented as a list
* deepcopy is used to try out different moves
