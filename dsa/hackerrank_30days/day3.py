# Day 3 solution
N = int(input().strip())
if N % 2 != 0:
    print('Weird')
elif N % 2 == 0 and N in range(2, 6):
    print('Not weird')
elif N % 2 == 0 and N in range(6, 20):
    print('Weird')
elif N % 2 == 0 and N > 20:
    print('Not weird')

# for i in range(6, 21):
#     print(i)
#
# for y in range(2, 6):
#     print(y)

# for i in range(1, 11):
#     if i % 2 != 0:
#         print(f"Odd number: {i}")
