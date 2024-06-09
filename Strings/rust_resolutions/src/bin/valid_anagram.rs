use std::collections::HashMap;

fn is_anagram_la_otra(s: String, t: String) -> bool {
    let mut s_hash = HashMap::new();
    for s_char in s.chars() {
        if s_hash.contains_key(&s_char) {
            if let Some(value) = s_hash.get_mut(&s_char) {
                *value += 1
            }
        } else {
            s_hash.insert(s_char, 1);
        }
    }
    for t_char in t.chars() {
        if let Some(value) = s_hash.get_mut(&t_char) {
            if *value <= 0 {
                return false;
            }
            *value -= 1
        } else {
            return false;
        }
    }
    !s_hash.values().any(|&n| n > 0)
}

fn is_anagram(s: String, t: String) -> bool {
    let mut s_hash = HashMap::new();
    for s_char in s.chars() {
        *s_hash.entry(s_char).or_insert(0) += 1;
    }
    for t_char in t.chars() {
        if let Some(value) = s_hash.get_mut(&t_char) {
            if *value <= 0 {
                return false;
            }
            *value -= 1
        } else {
            return false;
        }
    }
    !s_hash.values().any(|&n| n > 0)
}

fn main() {
    let s = "aloH".to_string();
    let t = "Hola".to_string();
    let result = is_anagram_la_otra(s, t);
    println!("{}", result);
}