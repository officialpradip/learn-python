import re
# \w [a-zA-Z0-9]
# \w [^a-zA-Z0-9]

mobileno = "+977-9818979696"


if re.search("\w{3}-\w{10}", mobileno):
    print("Thiss is np number")
