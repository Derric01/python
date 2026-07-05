def is_anagram(strs):
    visited=[False]*len(strs)
    result=[]
    for i in range (len(strs)):
        if visited[i]:
            continue
        group=[]
        group.append(strs[i])
        visited[i]=True
        for j in range(i+1,len(strs)):
            if not visited[j] and sorted(strs[i])==sorted(strs[j]):
                group.append(strs[j])
                visited[j]=True
            
        result.append(group)


    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(is_anagram(strs))

