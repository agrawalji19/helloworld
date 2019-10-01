string="Computer Science"
vowels=('a','e','i','o','u')
for x in string.lower():
    if x in vowels:
        y=ord(x)+1
        string=string.replace(x,chr(y))
print(string)
