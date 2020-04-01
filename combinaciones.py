#Esquivel Macias Erick Xavier
#Gomez Olvera Jacob Misael
#Combinaciones <Comprensión de listas> 30pts

Camisa = ["roja","negra","azul","morada","cafe"]
Pantalon = ["negro", "azul", "cafe obscuro", "crema"]
Accesorio = ["cinturon", "tirantes", "lentes", "fedora"]
combinaciones = [(p, c, a) for c in Camisa for p in Pantalon for a in Accesorio]
print(combinaciones, "Total de combinaciones: ", len(combinaciones))