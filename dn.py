print "Welcome to the fizzbuzz generator!"


while True:
    exit_prog = False
    n = int(raw_input("Pick a number from 1 to 100: "))
    if n > 100 or n < 1:
        while True:
            print "Are you high right now? (yes, no)"
            answer = raw_input()
            if answer == "yes":
                print "THIS IS ALL AN ILLUSION"
                exit_prog = True
                break
            elif answer == "no":
                print "Try to get it right this time!"
                break

    else:
        for n in range(1, (n + 1)):
            if n % 5 == 0 and n % 3 == 0:
                print "FizzBuzz"
            elif n % 3 == 0:
               print "Fizz"
            elif n % 5 == 0:
                print "Buzz"
            else:
                print n

    if exit_prog:
        break
