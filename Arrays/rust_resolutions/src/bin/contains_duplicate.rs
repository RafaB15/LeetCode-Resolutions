use std::collections::HashSet;

fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut set = HashSet::new();
    for num in nums.iter() {
        if set.contains(num) {
            return true;
        }
        set.insert(num);
    }        
    false
}

fn _contains_duplicate_loquillo(nums: Vec<i32>) -> bool {
    let mut set = HashSet::new();
    nums.into_iter().any(|n| !set.insert(n))
}

fn main() {
    let nums = vec![2,7,2,15];
    let result = contains_duplicate(nums);
    println!("{}", result);
}