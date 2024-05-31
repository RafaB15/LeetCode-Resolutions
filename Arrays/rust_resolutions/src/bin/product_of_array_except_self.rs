fn _product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let mut left_products = vec![0; nums.len()];
    let mut right_products = vec![0; nums.len()];
    let mut products = vec![0; nums.len()];
    
    left_products[0] = 1;
    right_products[nums.len() - 1] = 1; 

    let mut left_product = 1;
    let mut right_product = 1;

    for i in 0..nums.len() {
        left_products[i] = left_product;
        left_product *= nums[i];

        right_products[nums.len() - 1 - i] = right_product;
        right_product *= nums[nums.len() - 1 - i];
    }
    
    for i in 0..nums.len() {
        products[i] = right_products[i] * left_products[i];
    }
    products
}

fn product_except_self_better(nums: Vec<i32>) -> Vec<i32> {
    let mut products = vec![0; nums.len()];
    let mut left_product = 1;
    let mut right_product = 1;

    for i in 0..nums.len() {
        products[i] = left_product;
        left_product *= nums[i];
    }

    for i in 0..nums.len() {
        products[nums.len() - 1 - i] *= right_product;
        right_product *= nums[nums.len() - 1 - i]
    }

    products
}

fn product_except_self_even_better(nums: Vec<i32>) -> Vec<i32> {
    let mut products = vec![1; nums.len()];
    let mut left_product = 1;
    let mut right_product = 1;

    for i in 0..nums.len() {
        products[i] *= left_product;
        left_product *= nums[i];

        products[nums.len() - 1 - i] *= right_product;
        right_product *= nums[nums.len() - 1 - i]
    }
    products
}

fn main() {
    let nums = vec![2,7,2,15];
    let result = product_except_self_even_better(nums);
    println!("{:?}", result);
}