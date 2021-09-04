num = int(input("Enter a Number to check whether the Number is Prime or Not: "))

if num > 1:

    for i in range(2, num):

        if (num % i) == 0:
            print("The Number", num, "is not a Prime Number.")
            break
    else:
        print("The Number", num, "is a Prime Number.")

else:
    print("The Number", num, "is not a Prime Number.")