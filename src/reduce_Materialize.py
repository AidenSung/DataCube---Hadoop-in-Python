#!/usr/bin/env python

import sys

uidset = {}
lastkey = [0,0,0,0,0,0,0,0,0]
batch_len = 0
lastbatch_len = 0
flag = 0
for line in sys.stdin:
    line = line.strip()
    s = line.split('\t')
    rvalue = s[0]
    uid = s[1].split()
    ids = uid[0]
    batch_len = int(uid[1])
    if lastbatch_len == 0:
        lastbatch_len = batch_len
    if lastbatch_len != batch_len:
        for i in range(1,lastbatch_len+1):
            uidstr = ' '.join(uidset[lastkey[i]])
            print "%s\t%s" % (lastkey[i], uidstr)
        flag = 1
        lastbatch_len = batch_len
    rvalue = rvalue.split('|')
    temp = rvalue[0].split('.')
    region = temp[1].split() 
    group  = rvalue[1].split()
    r_len = len(region)
    while batch_len != 0:
        s = ' '.join(region[0:r_len]) + '|' + ' '.join(group[0:r_len])
        if uidset.get(s,'none') == 'none':
            uidset[s] = set()
        uidset[s].add(ids)
        if lastkey[batch_len] == 0:
            lastkey[batch_len] = s
        if lastkey[batch_len] != s:
            uidstr = ' '.join(uidset[lastkey[batch_len]])
            if flag == 0:
                print "%s\t%s" % (lastkey[batch_len], uidstr)
            else:
                pass
            uidset.pop(lastkey[batch_len])
            lastkey[batch_len] = s
        batch_len = batch_len - 1
        r_len = r_len - 1
    flag = 0
for i in range(1,lastbatch_len+1):
    uidstr = ' '.join(uidset[lastkey[i]])
    print "%s\t%s" % (lastkey[i], uidstr)
