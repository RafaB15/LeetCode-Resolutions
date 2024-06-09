fn max_area(height: Vec<i32>) -> i32 {
    let mut max = i32::MIN;

    let mut l = 0;
    let mut r = height.len() - 1;

    while l < r {
        let floor = (r - l) as i32;
        let current_height = height[r].min(height[l]);

        max = max.max(floor * current_height);

        if height[r] > height[l] {
            l += 1;
        } else {
            r -= 1;
        }
    }

    max
}

fn main() {
    let nums: Vec<i32> = vec![1,8,6,2,5,4,8,3,7];
    let result = max_area(nums);
    println!("Resultado final: {}", result);
}