name = input ('Hello, what is your name ? \n')
print (" Welcome " + (name))
print (' I have a number in my mind, take a guess')
rand = random.randint(1,100)
for  chances in range(7):
    try:
        guess = int(input())
        if isinstance(guess,int) == True:
            if chances >= 0 and guess != rand :
                print (str(7-(chances+1)) + 'chances left')
            if guess == rand:
                print ('oh.. great.. correct..')
                break
            elif guess > rand and chances !=6:
                print ('too high.. try again..')
            elif guess < rand and chances !=6:
                print ('not that low.. try again')
            if chances == 6:    # this if statement is seperate, bcs, last elif and this if have to work together.
                print ('better luck next time')
             
    except:
        if chances != 6:
            if chances >= 0 :
                 print (str(7-(chances+1)) + 'chances left')
            print (' Enter a number..')
        else:
            print('wrong input, end game.')