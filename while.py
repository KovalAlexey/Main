running = True
number = 25

while running:
    guess = int(input('enter your number '))
    
    if guess == number:
        print('you are right')
        running = False
    elif guess < number:
        print('your number is smaller')
    else:
        print('your number is bigger')    
 
print('the end')