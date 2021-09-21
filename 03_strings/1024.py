import string

n = int(input())
alphabet = string.ascii_lowercase

for i in range(n):

    text = list(input())

    # chr(97): Convert int to atring value in ascii table
    # ord('a'): Convert string to the ascii value

    # Step 1
    for j in range(len(text)):
        if text[j].lower() in alphabet:
            text[j] = chr(ord(text[j])+3)

    # Step 2:
    text = list(reversed(text))

    # Step 3: for loop starting from the middle to the end of the string
    for j in range(len(text) // 2, len(text)):
        text[j] = chr(ord(text[j])-1)

    # Converting list to string
    text = "".join(text)
    print(text)
