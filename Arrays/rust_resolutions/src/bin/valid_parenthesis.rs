use std::collections::HashMap;

pub fn is_valid(s: String) -> bool {
    let mut bracket_map: HashMap<char, char> = HashMap::new();
    bracket_map.insert('}', '{');
    bracket_map.insert(')', '(');
    bracket_map.insert(']', '[');

    let mut stack: Vec<char> = Vec::new();

    for parenthesis in s.chars() {
        if bracket_map.contains_key(&parenthesis) {
            if stack.len() == 0 {
                return false;
            }
            if let Some(&key_parenthesis) = bracket_map.get(&parenthesis) {
                if key_parenthesis == stack[stack.len() - 1] {
                    stack.pop();
                    continue;
                }
            }
            return false;
        } else {
            stack.push(parenthesis);
        }
    }
    stack.is_empty()
}

pub fn is_more_valid(s: String) -> bool {
    let mut stack: Vec<char> = Vec::new();

    for parenthesis in s.chars() {
        match parenthesis {
            '{' => stack.push('}'),
            '(' => stack.push(')'),
            '[' => stack.push(']'),
            '}' | ')' | ']' => {
                if stack.pop() != Some(parenthesis) {
                    return false;
                }
            },
            _ => continue
        }
    }
    stack.is_empty()
}

fn main() {
    let string = "()(){}{[][]".to_string();
    let result = is_valid(string);
    println!("{}",result);
}