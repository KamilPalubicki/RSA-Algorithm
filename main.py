def egcd(e, et):
    while et != 0:
        e, et = et, e % et
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

if __name__ == '__main__':

    print("Enter p (prime number)")
    p = inputPrime()
    print("Enter q (prime number)")
    q = inputPrime()

    n = p * q
    print("N = ", n)

    et = (p - 1) * (q - 1)
    print("Euler's tocent of N = ", et)

    for i in range(q, 150):
        if (egcd(i, et) == 1):
            e = i
            if e > q:
                print("e = ", e)
                break
    d = privateKey(e, et)
    print("d = ", d)

    public = (e, n)
    private = (d, n)
    print("Public key is", public)
    print("Private key is:", private)
