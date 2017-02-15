def ransom_note(magazine, ransom):
    ans = True
    if len(magazine) < len(ransom):
        return False
    dict = {}
    for i in magazine:
        if dict.has_key(i):
            dict[i] += 1
        else:
            dict[i] = 1
    #print dict
    
    for j in ransom:
        if dict.has_key(j):
            #print j, dict[j]
            if dict[j] > 0:
                dict[j] -= 1
                ans = True
            else:
                return False
        else:
            return False
    #print dict
    return ans
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
# print magazine, ransom

answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
