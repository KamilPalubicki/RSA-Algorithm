    def NWD(e, r):
        while r != 0:
            e, r = r, e % r
        return e

    if __name__ == '__main__':

        p = 13
        q = 97

        n = p * q
        print("N = ", n)

        r = (p - 1) * (q - 1)
        print("tocjent liczby N = ", r)

        for i in range(q, 150):
            if (NWD(i, r) == 1):
                e = i
                if e > q:
                    print("e = ", e)
                    break
