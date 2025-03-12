# win-> C:\user\data\...
# mac-> /Users/Desktop/...

# r -> read , w -> overwrite , a -> append(write) ， r+ -> read and write(cant create file when its not exists
# file = open("D:\\tmp\\file.txt", "r", encoding="utf-8")
def read_test():
    print("read_test")

    with open("D:\\tmp\\file.txt", "r", encoding="utf-8") as file:  # 文件在退出 with 块时自动关闭
        line = file.readline()
        lines = file.readlines()

        # do not use read when file is huge
        print("use read() to open a file...")
        print(file.read())  # read all the content in the file
        print(file.read())  # read null string

        print("use readline() to open a file...")
        # re-set index to head of file
        file.seek(0)
        # line = file.readline()
        while line != "":
            print(line)  # read a line
            line = file.readline()

        print("use readlines() to open a file...")
        file.seek(0)
        for readline in lines:  # save every single line in a list
            print(readline)

    # file.close() # 不适用with的时候，需要手动关闭文件
    with open("./data.txt") as data:
        for readline in data.readlines():
            print(readline)


def write_test():
    print("write_test")

    # 写文件模式，如果路径下文件不存在，会自动创建。如果存在，会清空文件内容后再写入！！--> OVERWRITE
    # 写的时候不能进行读取操作
    with open("./data_overwrite.txt","w",encoding="utf-8") as fw:
        fw.write("hello") # 不会默认换行
        fw.write("have to append \\n to the end of line to change line manually\n")
        fw.write("world")

    with open("./data.txt", "a", encoding="utf-8") as fa:
        fa.write("this line append to file contents\n")

    with open("./data.txt", "r+", encoding="utf-8") as frw: # read and write works all fine,and its append write
        for line in frw.readlines():
            print(f"reading from file :{line}")

        frw.write("write after read\n")

def mission_of_file():
    with open("./poem.txt","w",encoding="utf-8") as f1:
        f1.write("我欲乘风归去，\n")
        f1.write("惟恐琼楼玉宇，\n")

    with open("./poem.txt","a",encoding="utf-8") as f2:
        f2.write("起舞弄清影\n")
        f2.write("何似在人间\n")




if __name__ == '__main__':
    # write_test()
    mission_of_file()
    # read_test()
