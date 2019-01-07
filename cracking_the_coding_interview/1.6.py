String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def strCompression(string):
    newstr = ''
    i = 1
    count = 1
    while i < len(string):
        if string[i-1] != string[i]:
            newstr += string[i-1]
            newstr += str(count)
            count = 1
            i += 1
        else:
            count += 1
            i += 1

    newstr += string[-1]
    newstr += str(count)

    return string if len(newstr) > len(string) else newstr
