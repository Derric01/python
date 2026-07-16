def valid( s: str)->bool:
    stack=[]
    pairs={
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1]!=pairs[ch]:
                return False
            stack.pop()
    return not stack

s="()[]{}"
print(valid(s))