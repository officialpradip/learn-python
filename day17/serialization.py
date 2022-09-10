import pickle
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
# load JSON back to a data structure, use the "loads" method.
# loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
print(json.loads(json_string))


pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
# To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String:
# dump() method is used when the Python objects have to be stored in a file
print(pickle.loads(pickled_string))
