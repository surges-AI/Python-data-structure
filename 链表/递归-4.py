a={0:0,1:1}

def f(n):
    if n in a:
        return a[n]
    else :
        a[n] = f(n-2) + f(n-1)
    return a[n]

if __name__ == '__main__':
    print(f(999))
