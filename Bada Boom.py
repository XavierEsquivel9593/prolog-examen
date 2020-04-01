#Esquivel Macias Erick Xavier
#Gomez Olvera Jacob Misael
#Bada Boom!!! <generadores> 20 pts

def generador(N):
    if N > 0:
        i = 1
        while i <= N:
            if( i%3 == 0 and i%5 == 0 ):
                yield "Bada Boom"
            elif( i%3 == 0 ):
                yield "Bada"
            elif( i%5 == 0 ):
                yield "Boom!!"
            else:
                yield i
            i = i + 1
a = generador(10)
z = [e for e in a]
print(z)