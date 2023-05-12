if __name__ == '__main__':
    while True:
        number_input = int(input("masukan angka kamu : "))
        for i in range(1, number_input+1):
            if i%3 == 0 and i%5 == 0:
                print('FizzBuzz', end=' ')
                continue
            if i%3 == 0:
                print('Fizz', end=' ')
                continue
            if i%5 == 0:
                print('Buzz', end=' ')
                continue
            print(i, end= ' ')
        q1 = input('\n\nKamu ingin bermain lagi? (y/n): ')
        if q1 == 'y':
            print('\nselamat bersenang-senang ^^')
        else:
            print('Sampai jumpa kembali ^^')
            break