#A-T
#G-C


def main(arr):
    for i in arr:
        if i=='A':
            i='T'
        elif i=='a':
            i='t'
        elif i=='G':
            i='C'
        elif i=='g':
            i='c'
        elif i=='T':
            i='A'
        elif i=='t':
            i='a'
        elif i=='C':
            i='G'
        elif i=='c':
            i='g'
        print(i,end="")

if __name__=="__main__":
    n=int(input("Enter the length of the string:"))
    x = [str(input("Enter the string:")) for j in range(n)]
    print("Original String:",str(x))
    y = x[::-1]
    print("Final output:")
    main(y)