
# https://www.learner.org/series/learning-math-patterns-functions-and-algebra/patterns-in-context/part-d-counting-stairs-60-minutes/#:~:text=A%20way%20to%20build%20a,1)%20%2F%202%20for%201.
def staircase_finder(lst):
    # It would be a waste of time of making all the subsets and then find out that it doesn’t make a staircase. Can we make the function more efficient in that regard?
    # We could add a check that returns false by using the relationship between the number of blocks in a staircase and the height of a staircase.
    # quadratic formula for the equation n^2 + n - len(lst) * 2 = 0
    # a= 1, b = 1, c = - len(lst) * 2
    n = (-1 + (1 - 4 * 1 * -len(lst)* 2) **0.5)/2
    if int(n) != n:
        return False
    subsets = []
    indx = 0
    size = 1
    while indx < len(lst):
        subsets.append(lst[indx : indx +size])
        indx += size
        size += 1
    return subsets

print(staircase_finder([1,2])) #false
print(staircase_finder([1,2,3]))
print(staircase_finder([1,2,3,4,5,6]))
print(staircase_finder([1,2,3,4,5,6, 7])) #false