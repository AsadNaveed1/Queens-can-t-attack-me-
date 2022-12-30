# Queens-can-t-attack-me-Python

# Q3: Queens can’t attack me!
Weight: 35%

Last update: 14 Nov, 10:00pm

Consider a square chessboard with N × N cells and M queens on the chessboard (Note: there are no other chess pieces besides the queens). A queen can move vertically, horizontally or diagonally.

As an example, consider the chessboard with N=6 and M=1.

```
| | |o| | |o|
|o| |o| |o| |
| |o|o|o| | |
|o|o|Q|o|o|o|
| |o|o|o| | |
|o| |o| |o| |

```
The cells that can be reached by the queen are marked with o. Note that there are 16 cells that cannot be reached by the queen.

Here is another example with N=6 and M=2.
```
| | |o|o| |o|
|o| |o|o|o| |
|o|o|o|o| | |
|o|o|Q|o|o|o|
| |o|o|o|o| |
|o|o|o|Q|o|o|
```
In this example, there are 9 cells that cannot be reached by any queens.

Your task is to calculate the number of cells that are NOT reachable by any queens.

Input specification:

The first line contains two integers, N and M. (1 <= N <= 100, 1 <= M <= 10). 

Following are M lines. Each line contains two integers x and y, representing the location of a queen, i.e., the queen is at x-th row and y-th column (1 <= x, y <= N).

Output specification: 

The number of cells that are not reachable by any queens.
```
Testcase 1 (first two lines are user input)

6 1
4 3
16
Testcase 2 (for three lines are use input)

6 2
4 3
6 4
9
```
