# largePolyFFT

1) Write a random number generator that given n (a power of 2) returns a list of ints, each a random value between 0 and 2**11-1 
- Generator came with starter code

2) Run your FFT code on some smaller problems and compare the solutions to the school algorithm to verify correctness. (5 points)
- small problems checked and commented out

3) Repeat the timing experiment that we did for the two previous methods (school book and 3subproblem) for the FFT method. Plot a graph showing all three methods, where each method's results line goes up to a maximum run time per problem (say around 20 minutes of CPU time). At this run time limit, what are the problem sizes that can be solved by the three methods? (15 points)
-  

4) Perform an accuracy study comparing the native Python multiply algorithm with the your implementation using FFT. Here for each multiply, use the function convertBack(digits, base) to convert N0 and N1 (a list of digits) into a standard Python long int (with base set to 2**11), then multiply the numbers and check that the solution is the same. See the code snippet below. You may find that at a certain size of number, the FFT starts to get different (and wrong) answers back. This is due to limited floating point mathematical operations. Does the FFT make errors? If so, at what size? (15 points)


5) Perform a timing study with increasing powers of 2 (see code snippet below). You will see that the built in Python code is faster than the FFT. What is the slope of the two methods? Based on this, what algorithm do you think Python is using? (15 points)


6) Document and submit your code (20 points)
