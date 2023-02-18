import os
import random
import time

from barbarian import Barbarian
from cleric import Cleric
from elf import Elf
from hero import Hero

a = Cleric('lamer')
b = Barbarian('Chel')
for item in range(0, 10000):
    ran = random.randint(1, 3)
    # if ran == 1:
    #     a.attack(b)
    # elif ran == 2:
    #     b.attack(a)
    a.set_dp()
    b.set_dp()
#     os.system('cls')
    print(a)
    print(b)
    time.sleep(1)
# print(a)
# print(b)
# b.attack(a)


print(a)
print(b)