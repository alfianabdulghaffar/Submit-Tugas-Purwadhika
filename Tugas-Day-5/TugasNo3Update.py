if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]

    l1.reverse()
    l2.reverse()

    Varl1 = ((l1[0]*100) + (l1[1]*10) + l1[2])
    Varl2 = ((l2[0]*100) + (l2[1]*10) + l2[2])

    def tambah (urutan1, urutan2):
        changeList = []
        result = urutan1 + urutan2
        strResult = str(result)
        changeList = [strResult[0],strResult[1],strResult[2]]
        changeList.reverse()
        #for i in range (len(result)):
        #   changeList.append 
        #result.reverse ()
        print (changeList)
                 
tambah (Varl1,Varl2)