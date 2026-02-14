pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    for (outer_index, num) in nums.iter().enumerate() {
        let complement = target - *num;
        for (inner_index, other) in nums.iter().enumerate() {
            if inner_index != outer_index && *other == complement {
                return vec![outer_index as i32, inner_index as i32];
            }
        }
    }
    
    vec![0, 1]
}



#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_works() {
        let samples = vec![
            (vec![2,7,11,15], 9, vec![0,1]),
            (vec![3,2,4], 6, vec![1,2]),
            (vec![3,3], 9, vec![0,1]),
        ];
        
        for (input, target, expected) in samples.into_iter() {
            let result = two_sum(input, target);
            assert_eq!(result, expected);
        }
        
    }

}
