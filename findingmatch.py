import bwt
import rbwt

def build_fc_index(fr):
    fc_index = dict()
    for c, r in fr.items():
        fc_index[c] = []
        for i in range(r[0], r[1]):
            fc_index[c].append(i)
    return fc_index

def build_bwt_index(bw):
    bwti = dict()
    i = 0
    for char in bw:
        if char not in bwti: bwti[char] = []
        bwti[char].append(i)
        i += 1
    return bwti     

def find_char_from_fi(i):
    char = [ key for key, list_of_index 
            in fc_index.items()
            if i in list_of_index]
    return char[0]

def find_exact(q, r, t, sa, fi, bi, br):
    f = q[0]
    loc = []
    ind = 0
    rowfi = 0
    rowbwt = 0
    if f in fi:
        print("First character (", f, ") found in location", fi[f], "of FC")
        if len(q) == 1:
            loc = [sa[i] for i in fi[f]]
            print("MATCHED")
            print("\nMatched location(s):", sorted(loc))
        else:
            for i in fi[f]:
                print(f+str(ind), ">>>>>")
                for j in q[1:]:
                    rowfi = bi[f][rowbwt]
                    # print(len(fi[j]))
                    # if rowbwt >= len(fi[j]) or rowfi != fi[j][rowbwt]:
                    # if rowbwt >= len(fi[j]) or rowfi not in fi[j]:
                    if rowfi not in fi[j]:
                        print("UNMATCHED")
                        rowbwt += 1
                        break
                    else:
                        print("MATCHED:", j)
                        loc.append(sa[i])
                        f = j
                        rowbwt += 1
                ind += 1
                f = q[0]
            print("\nMatched location(s):", loc)
    else: print("There is no match found")

# read BWT(T)    
file1 = open("string-transformed.txt",'r')
ref = file1.read()
file1.close()

# read T
file2 = open("string.txt",'r')
t = file2.read()
file1.close()

# building Suffix Array of sorted rotation list
srl = bwt.bwm(t)
suffix = bwt.suffixArray(srl)
print("Suffix Array: ", suffix)

# building bwt_ranks & dictionary of character against its position range in FC
occur = rbwt.rankBwt(ref)[1]
fc_range = rbwt.firstCol(occur)[0]
fc_index = build_fc_index(fc_range)
print("FC Index: ", fc_index)

# building dictionary of character against its position in FC
bwt_index = build_bwt_index(ref)
bwt_ranks = rbwt.rankBwt(ref)[0]
print("BWT Index: ", bwt_index)
print("BWT Ranks: ", bwt_ranks)

query = input('Query sequence: ')
find_exact(query, ref, t, suffix, fc_index, bwt_index, bwt_ranks)