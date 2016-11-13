# Ten-Ping Bowling

## The Bowling Problem: 

Technical part of the interview for a internship with MustWin on Summer 2017

This is an application that takes in the number of pins knocked down on each roll, and outputs a scorecard as would be seen at a bowling alley. Including the strikes, spares, and extra frames at the end.

For example, if my application were called "bowling-scoreboard", I would run it as so:

python bowling-scoreboard 8 1 10 5 5 8 0 10 10 9 1 8 1 9 1 10 7 2

The output should resemble a scoreboard for the game**, something like so:

| FR | R1 | R2 | R3 | Score |
|----|----|----|----|-------|
| **1**  | 8  | 1  |    | 9     |
| **2**  | X  |    |    | 29    |
| **3**  | 5  | 5  |    | 47    |
| **4**  | 8  | 0  |    | 55    |
| **5**  | X  |    |    | 84    |
| **6**  | X  |    |    | 104   | 
| **7**  | 9  | /  |    | 122   |
| **8**  | 8  | 1  |    | 131   |
| **9**  | 9  | /  |    | 151   |
| **10** | X  | 7  | 2  | 170   |

** This could be run when the game isn't over yet.

## [Bowling](https://en.wikipedia.org/wiki/Ten-pin_bowling):

Ten-pin bowling is a sport in which a "bowler" rolls a bowling ball down a wood-structure or synthetic (polyurethane) lane and towards ten pins positioned at the end of the lane. The objective is to score points by knocking down as many pins as possible. Three finger holes are drilled into a traditional bowling ball, and weights vary considerably to make the sport playable for all ages. The pins are arranged in a triangular position by an automated machine. While professional ten-pin bowling tournaments are held in numerous countries, the sport is commonly played as a hobby by millions of people around the world.


## [Scoring](http://slocums.homestead.com/gamescore.html):

There are several symbols used when keeping score: an "X" signifies a "strike" in which all ten pins have been knocked down by the first roll of the ball in a frame; a "/" signifies a "spare" in which the remainder of the pins left standing after the first roll are knocked down on the second roll in a frame; a "-" indicates that no pins were knocked down on that roll, called a "miss"; an"F" indicates a "foul" where a part of the bowler's body went past the foul line, which marks the boundry of the approach (the part of the lane where we walk and release the ball) and the lane itself, where the oil is placed and the ball rolls towards the pins; and a "O" around a number indicates that the pins left standing after the first roll are in a formation known as a "split."  Some scorers, such as ours, use an "S" in front of the number to indicate a split.  Splits occur when the headpin (the foremost pin) is knocked down, and there is a gap of at least one pin between all the others left standing.  The terms "wide" and "washout" are used to define this situation except that the headpin was left standing. Sometimes, a "W" is used to indicate this situation, but that has generally gone out of use.

### Special Bonuses:

For the most part, you keep score by adding the number of pins knocked down in each frame.  Special bonuses are awarded for strikes and spares.  When a strike is bowled, the bowler is awarded the score of 10 (for knocking down all ten pins), plus he gets to add the total of his next two rolls to that frame.  For a spare, the bowler gets the 10, plus the total number of pins knocked down on the next roll only. 

## Online Bowling Game:

[https://www.miniclip.com/games/kingpin-bowling/en/](https://www.miniclip.com/games/kingpin-bowling/en/)


