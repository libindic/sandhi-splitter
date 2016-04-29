import codecs, sys

def distance(W, V):
    w, v = len(W), len(V)
    table = [[0 for i in range(v+1)] for j in range(w+1)]
    for i in range(1,w+1):
        for j in range(1,v+1):
            #substitute
            table[i][j] = 1+min([table[i-1][j-1], table[i-1][j], table[i][j-1]])
                               
                             
            if W[i-1] == V[j-1]:
                table[i][j] = min(table[i][j], table[i-1][j-1])
    #print table
    return table[w][v]


def extract(line):
    word, left = line.split("=")
    ssplit, sloc = left.split('|')
    splits = ssplit.split("+")
    locs = map(int, sloc.split(','))
    return (word, splits, locs)

if __name__ == '__main__':
    data = codecs.open(sys.argv[1], "r", 'utf-8')
    out = codecs.open(sys.argv[2], "w", 'utf-8')
    d = {}

    k = 1

    """
    for line in data:
        try:
            w, ss, ls = extract(line)
            counter = 0
            for l in ls:
                fw, sw = ss[counter], ss[counter+1]
                kp = k+1
                fws, swp = fw[-kp:], sw[:kp]
                fp, sp = w[l-k:l+1], w[l:l+k+1]
                outstring = "(%s, %s) - (%s, %s)\n"%(fws, swp, fp, sp)
                out.write(outstring)
                counter += 1
        except (ValueError, IndexError):
            pass
        
    """
    for line in data:
        try:
            w, ss, ls = extract(line)
            counter = 0
            for l in ls:
                fw, sw = ss[counter], ss[counter+1]
                kp = k+1
                fws, swp = fw[-kp:], sw[:kp]
                normal =fws + swp
                txd = w[l-k:l+k+1]
                outstring = "(%s, %s) %s - %s | %d\n"%(
                        fw, sw, normal, txd, distance(normal, txd))
                out.write(outstring);
                counter += 1


        except (ValueError, IndexError):
            pass
