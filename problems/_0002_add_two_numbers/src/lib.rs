pub fn add_two_numbers(left: u64, right: u64) -> u64 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add_two_numbers(2, 2);
        assert_eq!(result, 4);
    }
}
