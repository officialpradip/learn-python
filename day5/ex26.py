#  if else

book = 50
copy = 12
pen = 14

if book < copy:
    print("Book is less than copy")
else:
    print("No, copy is less than book")

if book < pen:
    print("Pen is less than Book")
elif book < copy:
    print("Book is more than copy")
else:
    print("Pen and Copy are less than book")

if pen == book:
    print("There are equal numbe rof pen and book")

pen += 50

if book > pen:
    print("Book is more than pen")
else:
    print("Now the number of pen is more than book")
