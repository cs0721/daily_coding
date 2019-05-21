while 1:
    decision = input('Do you want to play a number multiply game? "yes" or "no"')

    if decision == 'yes': 
        for i in range(2, 10):
            for j in range(1,10):
                print('{} X {} = {}'.format(i, j, i*j))
    elif decision == 'no':
        print('Good bye!')
        break
    else:
	    print('Please choose between "yes" or "no"')


