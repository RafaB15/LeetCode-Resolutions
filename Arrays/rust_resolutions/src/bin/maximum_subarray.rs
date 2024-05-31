use std::cmp::max;

pub fn max_sub_array(nums: Vec<i32>) -> i32 {
    let mut largest_sum = nums[0];
    let mut current_sum = nums[0];
    for &num in nums.iter().skip(1) {
        current_sum = max(num, num + current_sum);
        largest_sum = max(largest_sum, current_sum);
    }
    largest_sum
}

fn main() {
    let nums = vec![2,7,-10,15];
    let result = max_sub_array(nums);
    println!("{:?}", result);
}