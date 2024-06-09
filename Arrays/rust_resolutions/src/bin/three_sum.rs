// Lo clonamos para respetar la firma original, pero en leetcode se puede poner como mutable en la firma
// y no lo tendríamos que clonar. La otra forma de no clonarlo sería usando hashes.
fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut answer: Vec<Vec<i32>> = Vec::new();

    let mut nums_ts = nums.clone();
    nums_ts.sort();

    for i in 0..nums_ts.len() {
        
        if i > 0 && nums_ts[i] == nums_ts[i - 1] {
            continue;
        }

        let target = -1 * nums_ts[i];

        let mut l = i + 1;
        let mut r = nums_ts.len() - 1;

        while l < r {
            let sum = nums_ts[l] + nums_ts[r];
            if sum < target {
                l += 1;
            } else if sum > target {
                r -= 1
            } else {
                answer.push(vec![nums_ts[i], nums_ts[l], nums_ts[r]]);
                l += 1;
                while l < r && nums_ts[l] == nums_ts[l - 1] {
                    l += 1
                }
            }
        }

    }

    answer
}

fn main() {
    let nums = vec![-1,0,1,2,-1,-4];
    let result = three_sum(nums);
    println!("[{:?}]", result);
}