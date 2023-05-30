# List

print ("These are the shoe brands we manage: ")
shoes = ["Nike, Adidas, Converse, Puma,Under Armour"]
all_shoes = shoes[0:4]
print(all_shoes)
newshoe =(input("What brand would you like to add?: "))
shoes.append(newshoe)

for shoe in shoes:
    print(shoe)
