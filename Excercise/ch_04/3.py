def shift_code(str: str, hint: str) -> str:
    shift_len = ord(str[0]) - ord(hint)
    ans = []
    for c in str:
        ans.append(chr(ord(c) - shift_len))
        print(ans)

str, shift_len = input("Enter code,hint : ").split(",")
shift_code(str, shift_len)