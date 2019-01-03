The deletion distance between two strings is the minimum sum of ASCII values of
characters that you need to delete in the two strings in order to have the same
string. The deletion distance between cat and at is 99, because you can just
delete the first character of cat and the ASCII value of 'c' is 99. The
deletion distance between cat and bat is 98 + 99, because you need to delete
the first character of both words. Of course, the deletion distance between two
strings can't be greater than the sum of their total ASCII values, because you
can always just delete both of the strings entirely. Implement an efficient
function to find the deletion distance between two strings. You can refer to
the Wikipedia article on the algorithm for edit distance if you want to. The
algorithm there is not quite the same as the algorithm required here, but it's similar.


def ascii_deletion_distance(str1, str2):
    list1 = helper(str1, str2)
    list2 = helper(str2, str1)
    return sum(list1+list2)

def helper(str1, str2):
    count = 0
    res = []
    while len(str1) > 0 and len(str2) > 0:
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[0] == str2[j]:
                    str1 = str1[:0] + str1[1:]
                    str2 = str2[:j] + str2[j + 1:]
                    count += 1
                    break

        if not str1[:1] == "": res.append(ord(str1[:1]))
        str1 = str1[:0] + str1[1:]
    return res
