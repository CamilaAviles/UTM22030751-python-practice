# List
print("LIST")
print ("These are the shoe brands we manage: ")
shoes = ["Nike, Adidas, Converse, Puma,Under Armour"]
all_shoes = shoes[0:4]
print(all_shoes)
newshoe =(input("What brand would you like to add?: "))
shoes.append(newshoe)
for shoe in shoes:
    print(shoe)
print("THIS IS ALL FOR LIST")


# Tuple
print("TUPLE")
print ("These are the members of my family: ")
family = ("Concepcion", "Carlos", "Michelle", "Muñeca", "Senchi", "Guadalupe", "Camila")
indice = 0

while indice < len(family):
    print(family[indice])
    indice += 1
print("THIS IS ALL FOR TUPLE")
