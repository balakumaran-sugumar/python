def promt_user(userResponse, retries=4, reminder='Please try again !!'):
    while 1:
        ans = input(userResponse)

        if ans == 'Y':
            print("OK")
            return 1

        if ans == 'N':
            print("Alright !")
            return 0

        retries = retries - 1

        if retries < 0:
            raise ValueError("Incorrect Input !")
            return 0

        print(reminder)


promt_user("Do you wish to continue!")

