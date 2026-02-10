def is_palindrome(s: int) -> bool:

    if s < 0:
        return False
    
    s_str = str(s)
    if s_str == s_str[::-1]:
        return True
    else:
        return False
    
print ("enter you number:")
x = int(input())
print(is_palindrome(x))
