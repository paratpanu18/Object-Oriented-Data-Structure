def bon(w):
    ans = 0
    previous = None

    for c in w:
        if c == previous:
            break
        
        previous = c

    index_of_repeated_char = (ord(c) - ord('a')) + 1

    ans = index_of_repeated_char * 4

    return ans

secretCode = input("Enter secret code : ")
print(bon(secretCode))