import hashlib

words = []

with open ('Letters.txt', 'r') as f:
    for line in f:
        for word in line.split():
            words += [word]

print(words)

for word in words:
    password = str(word)

    ha1=hashlib.md5()
    codeToHash = ("5613076:Mordor:" + password).encode('utf-8')
    ha1.update(codeToHash)
    ha1.digest()
    ha1 = ha1.hexdigest()
    print(ha1)

    ha2 = hashlib.md5()
    codeToHash2 = ("GET:/Public/CS/Home.png").encode('utf-8')
    ha2.update(codeToHash2)
    ha2.digest()
    ha2 = ha2.hexdigest()
    print(ha2)

    nonce = "03e2abb8a924e966bee59d41cef32851"
    response = hashlib.md5()
    codeToHash3 = (ha1 + ":" + nonce + ":" + ha2).encode("utf-8")
    response.update(codeToHash3)
    response.digest()
    response = response.hexdigest()
    print(response)

    if (response == "ef9d6fc92fb1ddb032b9b72a2c110e9b"):
        break

print(password)
