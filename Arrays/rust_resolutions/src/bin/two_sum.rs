use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, i32> = HashMap::new();
    for (index, num) in nums.iter().enumerate() {
        let new_target = target - num;
        if let Some(value) = map.get(&new_target) {
            return vec![*value, index as i32];
        }
        map.insert(*num, index as i32);
    }
    Vec::new()
}

fn main() {
    let nums = vec![2,7,11,15];
    let target = 9;
    let result = two_sum(nums, target);
    println!("[{},{}]", result[0], result[1]);
}