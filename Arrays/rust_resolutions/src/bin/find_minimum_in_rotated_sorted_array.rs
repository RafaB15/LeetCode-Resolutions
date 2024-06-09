fn find_min(nums: Vec<i32>) -> i32 {
    let mut start = 0;
    let mut end = nums.len() - 1;
    let mut current_min = i32::MAX;

    while end >= start {
        if nums[end] >= nums[start] {
            current_min = current_min.min(nums[start]);
            break;    
        }
        let middle = (end + start) / 2;
        current_min = current_min.min(nums[middle]); 

        if nums[start] <= nums[middle] {
            start = middle + 1;
        } else {
            end = middle - 1;
        }
    }
    current_min
}

fn main() {
    let nums = vec![7, 8, 9, 10, 11, 12, 1, 2, 5];
    let result = find_min(nums);
    println!("Resultado final: {}", result);
}