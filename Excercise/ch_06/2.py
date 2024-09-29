i = 0

def length(txt: str) -> int:
    global i
    if txt == "": return 0
    
    print(f'{txt[0]}{'*' if i % 2 == 0 else '~'}', end='')

    i += 1
    return 1 + length(txt[1::])

print("\n",length(input("Enter Input : ")),sep="")