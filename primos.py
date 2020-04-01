#Esquivel Macias Erick Xavier
#Gomez Olvera Jacob Misael
#Primos  <generadores>  30 pts

def primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True            

def gprimo(N):
    i = 0
    while i <= N:
        if primo(i):
            yield i
            i = i + 1
        else:
            i = i + 1
    
a = gprimo(10)
z = [e for e in a]
print(z)