use std::collections::HashSet;

pub fn length_of_longest_substring(s: String) -> i32 {
    let mut set = HashSet::new();
    let chars: Vec<char> = s.chars().collect();
    let mut max_lenght = 0;
    
    let mut l = 0;
    let mut r = 0;

    while r < chars.len() {
        while set.contains(&chars[r]) {
            set.remove(&chars[l]);
            l += 1;
        }
        set.insert(chars[r]);
        r += 1;

        max_lenght = max_lenght.max(r - l);
    }

    max_lenght as i32
}

fn main() {
    let s = "abcabcbb".to_string();
    let result = length_of_longest_substring(s);
    println!("Result: {}", result);
}