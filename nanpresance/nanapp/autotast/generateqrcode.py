import hashlib
m = hashlib.sha224("hello".encode()).hexdigest()
print(m)