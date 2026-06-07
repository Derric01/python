def anagram(s:str,t:str)->bool:
   return sorted(s)==sorted(t)

anagram("anagram","panagram")