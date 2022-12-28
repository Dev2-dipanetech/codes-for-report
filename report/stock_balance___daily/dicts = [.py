dicts = [
    {"name": "hank", "age": 12,"gen":"m"},
    {"name": "tom", "age": 14,"gen":"m"},
    {"name": "trish", "age": 16,"gen":"f"},
    {"name": "hank", "age": 13,"gen":"m"}
]
print(dicts)

if (any(12 in d for d in dicts)):
    print ("FOund")
else:
    print("Not Found")