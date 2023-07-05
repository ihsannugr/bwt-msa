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

def find_exact(q, r, t, sa, fi, bi):
    f = q[0]
    ind = 0
    loc = []
    leng = 0
    rowfc = 0
    rowbwt = 0
    if f in fi:
        print("\nFirst character (", f, ") found in location", fi[f], "of FC")
        if len(q) == 1:
            loc = [sa[i] for i in fi[f]]
            print("MATCHED")
            print("\nMatched location(s):", sorted(loc))
        else:
            for i in fi[f]:
                print(f+str(ind), ">>>>>")
                rowbwt = ind
                leng = len(q)-1
                for j in q[1:]:
                    leng -= 1
                    rowfc = bi[f][rowbwt]
                    if j not in fi or rowfc not in fi[j]:
                        print("UNMATCHED")
                        break
                    else:
                        print("MATCHED:", j)
                        rowbwt = fi[j].index(rowfc)
                        f = j
                        if leng == 0:
                            loc.append(sa[i])
                ind += 1
                f = q[0]
            print("\n============================")
            print("Matched location(s):", loc)
            print("============================\n")
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
print("\nINDEXES")
print("=======")
print("Suffix Array: ", suffix)

# building bwt_ranks & dictionary of character against its position range in FC
occur = rbwt.rankBwt(ref)[1]
fc_range = rbwt.firstCol(occur)[0]
fc_index = build_fc_index(fc_range)
print("FC Index: ", fc_index)

# building dictionary of character against its position in FC
bwt_index = build_bwt_index(ref)
print("BWT Index: ", bwt_index)

print("\nEXACT-MATCH SEARCHING")
print("=====================")
query = input('Query sequence: ')
find_exact(query, ref, t, suffix, fc_index, bwt_index)