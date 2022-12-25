def countdown(number: int):
    for v in reversed(range(number + 1)):
        print(v)


def countdownRecurse(number):
    print(number)
    if number == 0:
        return
    else:
        countdownRecurse(number - 1)


# print(countdown(10), '\n')
print(countdownRecurse(10))
