# bowlingProblem
Technical part of the interview for a internship with MustWin on Summer 2017

This is an application that takes in the number of pins knocked down on each roll, and outputs a scorecard as would be seen at a bowling alley. Including the strikes, spares, and extra frames at the end.

For example, if my application were called "bowling-scoreboard", I would run it as so:

python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

The output should resemble a scoreboard for the game**, something like so:

| FR | R1 | R2 | R3 | Score |
|----|----|----|----|-------|
| 1  | 8  | 1  |    | 9     |
| 2  | X  |    |    | 29    |
| 3  | 5  |    |    | 27    |
| 4  | 8  | 0  |    | 55    |
| 5  | X  |    |    | 84    |
| 6  | X  |    |    | 104   | 
| 7  | 9  | /  |    | 122   |
| 8  | 8  | 1  |    | 131   |
| 9  | 9  | /  |    | 151   |
| 10 | X  | 7  | 2  | 170   |

** This could be run when the game isn't over yet.