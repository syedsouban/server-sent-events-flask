import random
lines = open('./data/crypto.csv').readlines()
random.shuffle(lines)
open('crypto.txt', 'w').writelines(lines)