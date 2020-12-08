from Post import Post

def main():
    while(True):
        print("Program Bloger")
        print("""
        1. Insert Blog
        2. Lihat Blog
        """)
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            inserBlog()
        else:
            showAllData()
        finish = input("Selesai? (Y/N)")
        if finish == 'Y':
            break

def inserBlog():
    print("INSERT DATA BLOG")
    title = input("Masukan Judul : ")
    body = input("Masukan Body : ")
    model = Post()
    model.insert([title,body])


def showAllData():
    model = Post()
    data = model.getTableName()
    print(data)
    


main()







