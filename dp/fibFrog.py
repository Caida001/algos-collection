The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially
located at one bank of the river (position −1) and wants to get to the other bank
(position N). The frog can jump over any distance F(K), where F(K) is the K-th
Fibonacci number. Luckily, there are many leaves on the river, and the frog can
jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers.
Consecutive elements of array A represent consecutive positions from 0 to N − 1
on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to
the other side of the river (from position −1 to position N). The frog can jump
between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of
jumps by which the frog can get to the other side of the river. If the frog
cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.


def F_upto_A(L):
    # Fibonacci sequence up to the
    # length of A (include starting and destination position)
    F = []
    F.append(0)
    F.append(1)
    while F[-1] <= L:
        F.append(F[-1]+F[-2])
    return F[1:-1]

def solution(A):
    # add starting position to A
    A.insert(0, 1)
    # add destination position to A
    A.append(1)#[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    n = len(A)#13
    # store available fibonacci jumps
    F = F_upto_A(n)#[1, 1, 2, 3, 5, 8, 13]
    # S mapping A in position
    # and storing the minimum step count to every "1" position
    S = [n] * n
    S[0] = 0 #[0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
    for i in range(1, n):
        # check if the position is 1 in A
        if A[i] == 1 :
            #loop the Fibonacci sequence
            for x in F:
                # previous position
                prev = i - x
                if prev >= 0:
                    # (the minimum step count of the previous position)
                    # plus
                    # (one more step to the existing position)
                    # if less than the step count of the existing position
                    # update the step count of the existing position
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                else:
                    break
    # return the last position of S, if S[-1]==n ,
    # means destination can'tbe reached
    # S:[0, 13, 13, 13, 13, 1, 13, 2, 13, 13, 13, 13, 3]
    return S[-1] if S[-1] < n else -1
