fn climb_stairs_recursive(n: i32) -> i32 {
    match n {
        1 | 0 => 1,
        _ => climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)
    }
}

//Nota: Puedo directamente tener dos variables en vez de guardarme el vector entero
fn climb_stairs(n: i32) -> i32 {
    let mut steps = Vec::new();
    for i in 0..=n{
        if i == 0 || i == 1 {
            steps.push(1);
            continue;
        }
        steps.push(steps[(i - 1) as usize] + steps[(i - 2) as usize])
    }
    steps[steps.len() - 1]
}

fn main() {
    let n = 3;
    let result = climb_stairs(n);
    println!("Result: {}", result);
}