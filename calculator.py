import math

while True:

    try:
        num = int(input("enter your number\n"))

        sin = input("enter your sign:[+, -, *, /, ^, sq(square root), l(LCM),  h(HCF) ]\n")

        if (sin == 'sq'):
            pass
        else:
            num2 = int(input("enter your number \n"))

        # ___________________________________________
        if sin == "+":

            ans = num + num2

        elif sin == "-":

            ans = num - num2

        elif sin == "*":

            ans = num * num2

        elif sin == "/":

            ans = num / num2

        elif sin == "^":
            ans = num ** num2
            pass

        elif sin == "l":
            maxNum = max(num, num2)

            while True:
                if (maxNum % num == 0 and maxNum % num2 == 0):
                    break
                maxNum = maxNum + 1
                pass
            
            ans = maxNum
            pass


        elif sin == 'h':
            if num2>num:
                mn = num
            
            else:
                mn = num2
                pass

            for i  in range(1,mn+1):
                if num%i == 0 and num2%i == 0 :
                    ans = i 
                    pass
                pass
            pass


        elif sin == "sq":
            ans = math.sqrt(num)
            pass
        else:
            pass

        # _____________________________________________

        print("answer is ", ans)

    except Exception as e:
        print(f"your value error ({e})")

    ask = input('do you use me  ?(y/n)')

    if ask == 'y':
        continue
    else:
        break
    pass
pass

