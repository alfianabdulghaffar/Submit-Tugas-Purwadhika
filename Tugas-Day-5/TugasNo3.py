if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]

    l1.reverse()
    l2.reverse()

    def tambah (urutan1, urutan2):
        result = []
        result = [urutan1[i]+urutan2[i] for i in range(len(urutan1))]
        result.reverse ()
        print (result)
                 
tambah (l1,l2)


    
