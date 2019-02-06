Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.


def triple_step(n):
    lst = [0] * (n+1)
    lst[0] = 1
    lst[1] = 1
    lst[2] = 2 

    for i in range(3, n+1):
        lst[i] = lst[i-3] + lst[i-2] + lst[i-1]

    return lst[-1] 
