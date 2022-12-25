S = input().strip()
try:
    number = int(S)
except ValueError:
    print("Bad String")
else:
    print(number)
