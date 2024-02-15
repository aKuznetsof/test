def main():

    num = int(input())
    max_sum = 0
    num_max_sum = 0
    while num != 0:
        temp_num = num
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        if sum > max_sum:
            max_sum = sum
            num_max_sum = temp_num
        num = int(input())

    print('Число', num_max_sum, 'имеет максимальную сумму цифр:', max_sum)

    print('\nНажмите Enter для выхода.')

    exit = input()

if __name__ == '__main__':
    main()