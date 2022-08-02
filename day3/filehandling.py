f = open("demofile.txt", "r")
print(f.read())
# print(f.read(5))
# print(f.readline())
f.close()

# f = open("demofile.txt", "r")
# for x in f:
#     print(x)


f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
