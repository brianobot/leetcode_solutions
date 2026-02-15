

def is_palindrome(x: int) -> bool:
    # negative numbers can not be palindrome by defintion of the problem
    if x < 0:
        return False
    
    if len(str(x)) == 1:
        return True
    
    return str(x) == str(x)[::-1]
    

def test():
    samples = [(121, True), (-121, False), (10, False)]
    for input, output in samples:
        assert is_palindrome(input) is output
    
    
if __name__ == "__main__":
    test()
    print("Test Passed ✅")
        
    