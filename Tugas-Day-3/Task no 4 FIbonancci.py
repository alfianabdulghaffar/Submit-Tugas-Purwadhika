if __name__ == '__main__':
    def fibonacci(i):
        if i == 0 :
            return 0
        elif i == 1:
            return 1
        else:
            return fibonacci (i-2) + fibonacci (i-1)
        
    rangeFib = int (input ('mohon input jumlah angka fibonacci :'))

    for x in range (rangeFib):
        print (fibonacci(x))
