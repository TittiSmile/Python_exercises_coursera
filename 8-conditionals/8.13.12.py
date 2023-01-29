"""
Get the user to enter some text and print out True if it’s a palindrome, False otherwise. 
(Hint: Start by reversing the input string, and then use the == operator to compare two values to see if they are the same)


"""
word=str(input("Write a string"))
cont = 0
is_pal = False
for i in word:
    if word == word[::-1]:
        print("1")
        is_pal=True
    else:
        print("2")
        is_pal=False
    cont+=1
print(is_pal)