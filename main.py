
def parallel_processing(n, m, data):
    output = []
    xdr =[(0, i) for i in range (n)]

    for i in range(m):
        start, xdr1= xdr.pop(0)
        output.append((xdr1, start))
        end = start+data[i]
        xdr.append((end, xdr1))
        xdr.sort()

    return output

def main():
    n, m=map(int, input().split())
    data =list(map(int, input().split()))
    result = parallel_processing(n,m,data)

    for xdr1, start in result:
        print(xdr1, start)
    

if __name__ == "__main__":
    main()
