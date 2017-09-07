for ii in range(1, 21):
    if ii % 3 == 0:
        print('Fizz')
    elif ii % 5 == 0:
        print('Buzz')
    elif ii % 15 == 0:
        print('FizzBuzz')
    else:
        print(ii)
