fin = open('input.txt', 'r')
fout=open('output.txt', 'w')
s=fin.readline().replace('\n','')
s1=fin.readline().replace('\n','')
k=int(s1)
m = []
for line in fin.readlines():
    ts=(line.replace('\n','').split(' '))
    m.append(ts)
maxscore=0
maxscorepattern=''
for e in range(len(s)-k+1):
    pattern=s[e:e+k]
    score=1
    for i in range(k):
        if pattern[i]=='A':
            score*=float(m[0][i])
        if pattern[i]=='C':
            score*=float(m[1][i])
        if pattern[i]=='G':
            score*=float(m[2][i])
        if pattern[i]=='T':
            score*=float(m[3][i])
    if maxscore<score:
        maxscore=score
        maxscorepattern=pattern
print score
fout.write(str(maxscorepattern))
fin.close()
fout.close()