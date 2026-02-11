with open("file_handling_codes/krishna.jpg","rb") as f1:
    img=f1.read()
    
    print(img)
with open("file_handling_codes/copy_krishna.jpg","wb") as f2:
    f2.write(img)
print("img copied successfully")
with open("binary_file","wb+") as f3:
    f3.write(b"hello\n i am nothing.\n")
    f3.seek(0)
    binary_data=f3.read()
    print(binary_data)
with open("binary_file","a+") as f4:
    f4.write("now the ending...")
    f4.seek(0)
    data2=f4.read()
    print(data2)
