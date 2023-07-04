import time

def rankBwt(bw):
    #return character ranks and map from character to # times appear
    toca = dict()
    ranks = []
    for c in bw:
        if c not in toca: toca[c] = 0
        ranks.append(toca[c])
        toca[c] += 1
    return ranks, toca

def firstCol(toca):
    #return map from character to the range of rows prefixed by the character
    first = {}
    first_ = ""
    totc = 0
    for c, count in sorted(toca.items()):
        first[c] = (totc, totc + count)
        totc += count
    for c, rnge in first.items():
        count = rnge[1] - rnge[0]
        t = c * count
        first_ = first_ + t
    return first, first_

def reverseBwt(bw):
    ranks, toca = rankBwt(bw)
    first = firstCol(toca)[0]
    rowi = 0
    t = '$'
    while bw[rowi] != '$':
        c = bw[rowi]
        t = c + t 
        rowi = first[c][0] + ranks[rowi]
    return t       

# st = time.time()

file = open("string-transformed.txt",'r')
bw = file.read()

# print("\nBWT(T) + ranking: ")
# print("======================")
# print(bw)
# print("BWT-ranks: ", rankBwt(bw)[0])
# print("Character occurence: ", rankBwt(bw)[1])

# print("\nFirst column: ")
# print("======================")
# print("FC-dict: ", firstCol(rankBwt(bw)[1])[0])
# print("FC-string: ", firstCol(rankBwt(bw)[1])[1])

# print("\nReverse BWT(T): ")
# print("======================")
# print(reverseBwt(bw))

# et = time.time()
# elapsed_time = et - st

file = open("string-reversed.txt",'w')
file.write(reverseBwt(bw))

# print('\nExecution time:', elapsed_time, 'seconds')