"""

A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase 
is a palindrome by reversing it and then checking if the reversed version is equal to the original. 
Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
"""




p_phrase = "was it a car or a cat I saw"
p_phrase_rep = p_phrase.replace(" ", "")
p_phrase_rep_lower = p_phrase_rep.lower()
r_phrase = p_phrase_rep_lower[::-1]
is_true = True
for i in range(len(p_phrase_rep_lower)):
    if (p_phrase_rep_lower[i]) != r_phrase[i]:
        is_true=False
print(is_true)
   
