import time

def rotations(t):
    #return list of rotations from input string
    tt = t * 2
    return [ tt[i:i+len(t)] for i in range(0, len(t)) ]

def bwm(t):
    #bw matrix, return lexicographically sorted list of t's rotations
    return sorted(rotations(t))

def bwtViaBwm(t):
    #return last column as BWT(T)
    return ''.join(map(lambda x: x[-1], bwm(t)))

def suffixArray(t):
    sa = [ (len(i)-1-i.index('$')) for i in t ]
    return sa

st = time.time()

file = open("string.txt",'r')
t = file.read()

print("\nSequence: ")
print("======================")
print(t)

print("\nBurrow-Wheeler Matrix:")
print("======================")
for i in bwm(t):
    print(i)

print("\nBWT(T) or last column:")
print("======================")
print(bwtViaBwm(t))

file.close()

# print("\nSuffix Array:")
# print("======================")
# print(suffixArray(bwm(t)))

# et = time.time()
# elapsed_time = et - st

file = open("string-transformed.txt",'w')
file.write(bwtViaBwm(t))
file.close()

# print('\nExecution time:', elapsed_time, 'seconds')

