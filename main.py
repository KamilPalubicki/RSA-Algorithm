def NWD(e, et):
    while et != 0:
        e, et = et, e % et
    return e


def privateKey(e, et):
    for d in range(1, 5000):
        if ((d * e) % et == 1):
            return d

if __name__ == '__main__':

    p = 13
    q = 97

    n = p * q
    print("N = ", n)

    et = (p - 1) * (q - 1)
    print("euler's tocent of N = ", et)

    for i in range(q, 150):
        if (NWD(i, et) == 1):
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

