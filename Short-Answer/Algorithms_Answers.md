#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n); Linear function where the size of N does not matter. It will only run once. 


b) O(n log n); So the outer loop runs n times. The value of j doubles each iteration so its not linear. If you calculate their run times..
O(n * (log n)) = O(n log n)


c) O(n); recursive cases call themselves one time. The bigger the input however the long it will take so a cache is helpful here. Assuming bunnies is an int, it will execute x number of times aka linear time. 

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

I guess the best solution for this would be binary search. We would start by dropping the egg from the middle/median (between floor 0 and floor n). 
If the egg breaks that means the floor we're on is too high. So then you would find the median floor between the floor you were just on and the floor 0, and check to see if the egg breaks again.
This would keep repeating until the eggs stop breaking. If however the first iteration doesn't break the egg, that means you weren't high enough, so you would do the opposite of what I previously said.
For binary search the run time is O(log n)
