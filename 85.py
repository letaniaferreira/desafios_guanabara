nums = [[], []]
continuar = 's'
while continuar == 's':
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
    continuar = input('quer  continuar? ')
print(sorted(nums[0]), sorted(nums[1]))
