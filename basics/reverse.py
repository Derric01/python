class solution:
    def revnum(self,n):
        rev=0
        while n>0:
           digit=n%10
           rev=rev*10+digit
           n//=10
        return rev 

sol=solution()
print(sol.revnum(132142))
        