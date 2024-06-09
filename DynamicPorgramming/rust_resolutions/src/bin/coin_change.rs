fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
    let mut opt = vec![amount + 1; (amount + 1) as usize];
    opt[0] = 0;

    for i in 1..=amount {
        for &coin in coins.iter() {
            println!("{:?}", opt);
            let rest = i - coin;
            if rest < 0 {continue}
            opt[i as usize] = opt[i as usize].min(opt[rest as usize] + 1)
        }
    }
    if opt[amount as usize] == amount + 1{
        return -1;
    }
    opt[amount as usize]
}

fn main() {
    let coins = vec![2];
    let result = coin_change(coins, 3);
    println!("{}", result);
}