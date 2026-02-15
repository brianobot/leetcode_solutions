pub fn is_palindrome(x: i32) -> bool {
    if x < 0 {
        return false;
    }
    
    if x.to_string().len() == 1 {
        return true;
    }
    
    x.to_string() == x.to_string().chars().rev().collect::<String>()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let samples = vec![
            (121, true),
            (-121, false),
            (10, false),
        ];
        
        for (input, output) in samples.iter() {
            assert_eq!(is_palindrome(*input), *output);    
        }
        
    }
}
