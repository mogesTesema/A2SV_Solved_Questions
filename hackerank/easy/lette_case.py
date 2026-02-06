def swap_case(s):
    s = list(s)
    for i,letter in enumerate(s):
        if letter.isupper():
            s[i] = letter.lower()
        else:
            s[i] = letter.upper()
    return "".join(s)
            

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)