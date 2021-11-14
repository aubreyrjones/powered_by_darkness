import random

with open('npc_names.txt') as f:
    l = f.readlines()

random.shuffle(l)

outl = [x.split(' ')[0] + ' ' + x.split(' ')[2] for x in l]

print("".join(outl))

