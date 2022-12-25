number_of_input = int(input())
for index in range(number_of_input):
    string_input = input().split()
    for i in range(len(string_input)):
        print(string_input[i][::2], string_input[i][1::2])
        break

# s[::2] - start from the O index and step 2
# s[1::2] - start from the 1st index and step 2
# if s = "012345" ... s[::2] = "024" ... s[1::2] = "135"
