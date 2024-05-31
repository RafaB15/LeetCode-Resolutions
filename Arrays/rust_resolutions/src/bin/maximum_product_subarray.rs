use std::cmp::{
    max,
    min
};

fn max_product(nums: Vec<i32>) -> i32 {
    let mut largest_product = nums[0];
    let mut current_largest = nums[0];
    let mut current_smallest = nums[0];

    for &num in nums.iter().skip(1) {
        let temp = current_largest;
        current_largest = max(num.max(num * current_largest), num * current_smallest);
        current_smallest = min(num.min(num * temp), num * current_smallest);
        largest_product = max(current_largest, largest_product);
    }

    largest_product
}

fn main() {
    let nums = vec![-2,7,-10,15];
    let result = max_product(nums);
    println!("{:?}", result);
}