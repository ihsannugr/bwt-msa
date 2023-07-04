import random

char = ['A', 'C', 'G', 'T']

def genseq(n):
    open("string.txt", 'w').close()
    file = open("string.txt",'a')
    for i in range(n):
        file.write(random.choice(char))
    file.write("$")
    file.close()

genseq(20)
