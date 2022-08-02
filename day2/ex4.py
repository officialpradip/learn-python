#Variables and Names

books = 20
books_price_each = 100

copies = 12
copies_price_each = 50.55

print("Total amount for books is", books*books_price_each)
print("Total amount for copies is", copies*copies_price_each)
print("Total amount spent for books and copies=",
      books*books_price_each + copies*copies_price_each)

print("There are", books, "books and ", copies, "copies were bought")
print("The average of", books, "books and ",
      copies, "copies is:", int((books + copies)/2))
