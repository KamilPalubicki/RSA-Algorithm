def egcd(e, et):
    while et != 0:
        e, et = et, e % et
    return e

def findE(q, et):
    for i in range(q, 150):
        if (egcd(i, et) == 1):
            e = i
            if e > q:
                return e
def privateKey(e, et):
    for d in range(1, 5000):
        if ((d * e) % et == 1):
            return d

def checkIfPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def inputPrime():
    n = int(input())
    while (checkIfPrime(n) == False):
        n = int(input("Enter prime number!"))
    return n

def encrypt(e, n, text):
    message = []
    m = 0
    for i in text:
        if (i.isupper()):
            m = ord(i)
            code = (m ** e) % n
            message.append(code)
        elif (i.islower()):
            m = ord(i)
            code = (m ** e) % n
            message.append(code)
        elif (i.isspace()):
            space = 400
            message.append(space)
    return message

def decrypt(d, n, text):
    text = text.split(',')
    message = ''
    for i in text:
        m = 0
        if i != '400' and i != ' 400':
            m = (int(i) ** d) % n
            code = chr(m)
            message += code
        else:
            message += ' '
    return message

def menuMessage(e, d, n):
    choose = input("Type 1 - for encryption an message, 2 - for decryption encrypted message or 3 - to exit")
    while (choose != '3'):
        if (choose == '1'):
            message = input("Type message you want to encrypt")
            enc_msg = encrypt(e, n, message)
            print("Your encrypted message is:", enc_msg)
        elif (choose == '2'):
            message = input("Type message you want to decrypt")
            print("Your decrypted message is:", decrypt(d, n, message))
        else:
            print("You entered the wrong option. Try again")
        choose = input("Type 1 - for encryption an message, 2 - for decryption encrypted message or 3 - exit")

if __name__ == '__main__':

    print("Enter p (prime number)")
    p = inputPrime()
    print("Enter q (prime number)")
    q = inputPrime()

    n = p * q
    print("N = ", n)

    et = (p - 1) * (q - 1)
    print("Euler's tocent of N = ", et)

    e = findE(q, et)
    print("e = ", e)

    d = privateKey(e, et)
    print("d = ", d)
    print("Public key is", (e, n))
    print("Private key is:", (d, n))
    menuMessage(e, d, n)