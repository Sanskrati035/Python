def fizzBuzz(r):
    for i in range(1,51):
        if(i%5==0 and i%7==0):
            print(str(i)+" = fizzbuzz")
        else:
            if(i%5==0):
                print(str(i)+" = fizz")
            else:
                if(i%7==0):
                    print(str(i)+" = buzz")
                else:
                    print(str(i))
fizzBuzz(51)