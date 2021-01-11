# AlgorithmsToLiveByBook
Testing algorithms in the book Algorithms to Live By

## Algorithms

### Page 107: Jackson's Rule on scheduling tasks with 2 machines

The problem can be thought about with laundry machines. A load can have different wash and dry times, ie. 20 minutes to wash and 50 minutes to dry. 

Jackson's rule says to take the single step that takes the least amount of time. If it is a wash time, then do it next, if it is a dry time, plan to do it last.

The greedy solution (picking the greatest wash time that is less than the previous dry time) beats Jackson's Rule ~95+% of the time
