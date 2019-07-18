import string

def reverse(text):
    return text[::-1]

def polindrome(text):
    return text == reverse(text)

something_ref = input('Enter your text here: ')
something = something_ref.lower()

forbidden = ['!', '?',',', ' ', ':', ';', '-', '/', '.']

something = "".join(x for x in something if x not in forbidden)

print(something)

if polindrome(something):
    print('yes')
else:
    print('no')    