pub fn search(nums: Vec<i32>, target: i32) -> i32 {
    let mut l = 0;
    let mut r = nums.len() - 1;

    let mut index: i32 = -1;

    while l <= r {
        let m = (l + r) / 2;

        if nums[m] == target {
            index = m as i32;
            break;
        }

        if nums[l] <= nums[m] {
            if nums[m] > target && nums[l] <= target {
                r = m - 1;
            } else {
                l = m + 1;
            }
        } else {
            if nums[m] < target && target <= nums[r] {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
    }
    index
}

fn main() {
    let nums = vec![4,5,6,7,0,1,2];
    let result = search(nums, 0);
    println!("Resultado final: {}", result);
}