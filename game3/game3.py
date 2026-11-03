hp = 10
gold = 0
print("You wake up in a dark dungeon.")
print("There are two doors: left and right.")
door = input("Which door? (left/right) ").lower().strip()
if door == "left":
 print("A rat bites you!")
 hp = hp - 2
elif door == "right":
 print("You find a small bag of gold!")
 gold = gold + 3
else:
 print("You stand still. Nothing happens.")
print(f"Health: {hp} | Gold: {gold}")
