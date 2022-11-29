# It's a guess the number game
import random

print ('Hi there! What is your name?')
name = input ()

print('Pleased to meet you '+ name + ', you will have to guess the number between 1 and 20. You can try 6 times.')
secretNumber = random.randint(1, 20)

try:
    for attemptsMade in range (1, 7):
        print ('What is the number?')
        attempt = int (input())

        if attempt < secretNumber:
            print ('Too low. Try higher.')
        elif attempt > secretNumber:
            print ('Too High. Try lower this time')
        else:
            break

    if attempt == secretNumber:
            print ('Correct!')
            print ('It took you ' + str (attemptsMade) + ' attempts.')
    else:
            print ('Too bad, the number was ' + str (secretNumber) + '.')
except ValueError:
    print ('You had to tell me a number. I will not play anymore.')

    

