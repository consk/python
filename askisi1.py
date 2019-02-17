import sys
x=int(input("Dwse ton arithmo listwn: "))
def sumIntervals(x):
    lista=[]
    for y in range(x):
        pra3i=[]
        a=int(input("Dwse to proto arithmo tis " + str(y+1) +"lista: "))
        b=int(input("Dwse to deftero arithmo tis " + str(y+1) +"lista: "))
        if a>b:
            sys.exit("Provlima: Lathos parametros!")
        pra3i.append(a)
        pra3i.append(b)
        lista.append(pra3i)
    l=len(lista)
    for q in range(l):
        if lista[0][0]>lista[q][0]:
            lista[0][0]=lista[q][0]
        elif lista[0][1]<lista[q][1]:
            lista[0][1]=lista[q][1]
        elif lista[0][0]<=lista[q][0] and lista[0][1]>=lista[q][1]:
            pass
    length=lista[0][1]-lista[0][0]
    print("i teliki lista einai " + str(lista[0]))
    print("to oliko mikos einai: " + str(length))
sumIntervals(x)
