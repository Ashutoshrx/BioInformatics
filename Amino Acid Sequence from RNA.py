
def main(arr):

    table= {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    }

    list=[arr[i:i+3] for i in range(len(arr)) if i%3==0 ]
    print(list)
    protein=""
    for i in list:
        for keys in table:
            if keys==i:
                protein+=table[keys]
                #print(table[keys],end=",")
    return protein



if __name__=="__main__":
    n=int(input("Enter the length of the string:"))
    x = [str(input("Enter the RNA string(IN CAPITALS):")) for j in range(n)]
    #x="AUGUGCAAGUCCGGAU"
    print("RNA Sequence:",str(x))
    print("The length is:",len(x))
    print("Amino Acid Sequence:",main(x))





