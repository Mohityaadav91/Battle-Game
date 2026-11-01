# battle game - raja wala conquer game
# apni sena banao aur dusre rajaon ke kile jeeto
# chalane ke liye: python3 battle_game.py

import random

print("=" * 40)
print("BATTLE GAME - Raja ka yuddh")
print("=" * 40)
print("Tum Alwar ke raja ho. Aas paas ke 5 kile")
print("jeetne hain. Sare kile jeet gaye to tum")
print("pure Rajasthan ke raja ban jaoge!")
print()

# har jagah ke sipahi aur jeetne par milne wala sona
places = [
    {"name": "Jaipur", "soldiers": 25, "loot": 60, "taken": False},
    {"name": "Jodhpur", "soldiers": 35, "loot": 80, "taken": False},
    {"name": "Udaipur", "soldiers": 45, "loot": 100, "taken": False},
    {"name": "Kota", "soldiers": 55, "loot": 120, "taken": False},
    {"name": "Bikaner", "soldiers": 70, "loot": 150, "taken": False},
]

army = 40
gold = 100


def show_status():
    print()
    print("-" * 40)
    print("Tumhari sena:", army, " Sona:", gold)
    jeete = []
    for p in places:
        if p["taken"]:
            jeete.append(p["name"])
    if jeete:
        print("Jeete hue kile:", ", ".join(jeete))
    else:
        print("Jeete hue kile: koi nahi")
    print("-" * 40)


def battle(place):
    # ladai yahin hoti hai, jeete to kila tumhara
    global army, gold
    enemy = place["soldiers"]
    print()
    print("Hamla! %s ke %d sipahi ladne aaye." % (place["name"], enemy))
    while army > 0 and enemy > 0:
        my_hit = random.randint(4, 10)
        enemy_hit = random.randint(3, 8)
        enemy = enemy - my_hit
        army = army - enemy_hit
        if enemy < 0:
            enemy = 0
        if army < 0:
            army = 0
        print("Tumne %d mare, unhone %d mare. Bache - tumhare: %d, unke: %d"
              % (my_hit, enemy_hit, army, enemy))
    if enemy == 0:
        print("%s jeet liya! Loot me %d sone ke sikke mile." % (place["name"], place["loot"]))
        gold = gold + place["loot"]
        place["taken"] = True
        place["soldiers"] = 0
    else:
        print("Haar gaye... sena khatam ho gayi.")


def attack():
    bache = []
    for p in places:
        if not p["taken"]:
            bache.append(p)
    if not bache:
        print("Koi kila bacha hi nahi, sab jeet liye!")
        return
    print()
    print("Kis par hamla karna hai?")
    for i, p in enumerate(bache):
        print("%d. %s - %d sipahi" % (i + 1, p["name"], p["soldiers"]))
    try:
        num = int(input("Number batao: "))
    except ValueError:
        print("Arey number likho yaar.")
        return
    if num < 1 or num > len(bache):
        print("Galat number hai.")
        return
    place = bache[num - 1]
    if army < place["soldiers"]:
        print("Tumhari sena unse kam hai, haar bhi sakte ho!")
        jawab = input("Phir bhi hamla karna hai? (y/n): ")
        if jawab.lower() != "y":
            print("Theek hai, pehle sena badha lo.")
            return
    battle(place)


def recruit():
    global army, gold
    print()
    print("1 sipahi = 5 sona. Tumhare paas %d sona hai." % gold)
    try:
        num = int(input("Kitne sipahi bharti karne hain? "))
    except ValueError:
        print("Arey number likho yaar.")
        return
    if num <= 0:
        print("0 ya minus wale sipahi nahi aate.")
        return
    price = num * 5
    if price > gold:
        print("Itna sona nahi hai! %d sipahi ke liye %d sona chahiye." % (num, price))
        return
    gold = gold - price
    army = army + num
    print("%d sipahi aa gaye. Ab sena: %d, sona: %d" % (num, army, gold))


def rest():
    # aaram karne par har jeete hue kile se aur rajdhani se sona milta hai
    global gold
    jeete = 0
    for p in places:
        if p["taken"]:
            jeete = jeete + 1
    mila = 20 + jeete * 15
    gold = gold + mila
    print("Aaram kiya. %d sona mila (rajdhani 20 + har kile se 15)." % mila)


while True:
    show_status()

    jeet_gaye = True
    for p in places:
        if not p["taken"]:
            jeet_gaye = False
    if jeet_gaye:
        print()
        print("BADHAI HO! Tumne sare kile jeet liye.")
        print("Ab tum pure Rajasthan ke raja ho!")
        break

    if army <= 0 and gold < 5:
        print()
        print("Sena bhi gayi aur sona bhi khatam. Khel khatam, raja haar gaya.")
        break

    print("1. Hamla karo")
    print("2. Sipahi bharti karo (5 sona = 1 sipahi)")
    print("3. Aaram karo (sona milega)")
    print("4. Khel chhodo")
    try:
        choice = input("Batao kya karna hai (1-4): ")
    except EOFError:
        print()
        print("Khel band ho gaya.")
        break

    if choice == "1":
        attack()
    elif choice == "2":
        recruit()
    elif choice == "3":
        rest()
    elif choice == "4":
        print("Phir milenge, raja!")
        break
    else:
        print("1 se 4 me se kuch chuno.")
