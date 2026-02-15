

def two_sum(nums: list[int], target: int) -> list[int]:
    for outer_index, num in enumerate(nums):
        complement = target - num
        for inner_index, other in enumerate(nums):
            if inner_index != outer_index and other == complement:
                return [outer_index, inner_index]
    
    return [0, 1]
    
   

def test():
    samples = [
        ([2,7,11,15], 9, [0, 1]),
        ([3,2,4], 6, [1, 2]),
        ([3,3], 6, [0, 1]),
    ]
    
    for (input, target, expected) in samples:
        result = two_sum(input, target)
        print(f"{result}: {expected}")
        assert result == expected
        

if __name__ == "__main__":
    test()
    print("Test Passed ✅")