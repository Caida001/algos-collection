Palindrome: Implement a function to check if a linked list is a palindrome.

def isPalindrome(l):
    lis = []
    pointer = l
    while pointer:
        lis.append(pointer.val)
        pointer = pointer.next

    while l:
        if l.val != lis.pop(): return False
    return True 
