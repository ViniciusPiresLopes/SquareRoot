# Square Root
## This program calculates square roots based on a average method
Let's suppose we want to calculate a square root of 2 (x). We know that:
```
0 < x < 2
average = (2 + 0) / 2 = 1
```
So we test the average 1 in the equation:
```
x = sqrt(2)
x^2 = 2
x.x = 2
x = 2/x
```
Testing the value 1:
```
1 = 2/1 = 2
```
That's false, 1 is minor than 2, in this case x needs to be higher.
Now we have:
```
1 < x < 2
```
Do the average between 1 and 2, which is 1.5. Then test again:
```
1.5 = 2/1.5 = 1.33...
```
That's false again, but this time 1.5 is major than 1.33, it means that the x needs to be lower. So:
```
1 < x < 1.5
```
The program do that again and again, each time a better aproximation and stops when it gets the accuracy given (decimals places).