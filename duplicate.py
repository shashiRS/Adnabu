import pdb 
a = "aaabbbaaabbabddccc"
def remove_dups(st,ind):
    print st, ind
    st = st.replace(st[ind], "")
    print st, "in dups"
    find_dups(st)

def find_dups(text):
    s=text
    print s, "in find"
    ln = len(s)
    print ln
    fg = 0
    ind = 0
    if ln==1:
        print s, 'len'
        return s
    for i in range(0,ln-1):
        if(s[i]==s[i+1]):
            ind = i
            remove_dups(s,ind)
            # s = remove_dups(s, ind)
            # pdb.set_trace()      

    print s, 'check'  
    
    return s

ans = find_dups(a)

print 'answer', ans