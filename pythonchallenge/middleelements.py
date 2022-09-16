# Find the middle value from an array

demo = "pradipa"
# check whether the elements are odd or even
if len(demo) % 2 == 1:
    if len(demo) == 1:
        print("The first letter is", demo)
    else:
        x = int((len(demo)-1)/2)
        result = demo[x]
        print(result)
else:
    print("Can't find middle elements")
