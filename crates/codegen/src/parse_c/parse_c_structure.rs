//! Low-level C array initializer parser.
//!
//! Parses C array initializers like:
//! ```c
//! { "name", OPT_TYPE_STRING, { .func_arg = opt_name }, "help text" },
//! ```

/// Parse a C array initializer into a list of element groups.
///
/// Each inner Vec<String> represents one `{ ... }` element in the array.
pub fn parse_c_structure(text: &str) -> Vec<Vec<String>> {
    let mut result = Vec::new();
    let mut current_element = Vec::new();
    let mut current_token = String::new();
    let mut depth = 0;
    let mut in_string = false;
    let mut escape_next = false;

    for ch in text.chars() {
        if escape_next {
            current_token.push(ch);
            escape_next = false;
            continue;
        }

        if ch == '\\' && in_string {
            current_token.push(ch);
            escape_next = true;
            continue;
        }

        if ch == '"' {
            in_string = !in_string;
            current_token.push(ch);
            continue;
        }

        if in_string {
            current_token.push(ch);
            continue;
        }

        match ch {
            '{' => {
                depth += 1;
                if depth == 1 {
                    current_element.clear();
                    current_token.clear();
                } else {
                    current_token.push(ch);
                }
            }
            '}' => {
                depth -= 1;
                if depth == 0 {
                    let trimmed = current_token.trim().to_string();
                    if !trimmed.is_empty() {
                        current_element.push(trimmed);
                    }
                    if !current_element.is_empty() {
                        result.push(current_element.clone());
                    }
                    current_element.clear();
                    current_token.clear();
                } else {
                    current_token.push(ch);
                }
            }
            ',' if depth == 1 => {
                let trimmed = current_token.trim().to_string();
                if !trimmed.is_empty() {
                    current_element.push(trimmed);
                }
                current_token.clear();
            }
            _ => {
                if depth >= 1 {
                    current_token.push(ch);
                }
            }
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_simple() {
        let input = r#"{ "name", OPT_TYPE_STRING, "help" }"#;
        let result = parse_c_structure(input);
        assert_eq!(result.len(), 1);
        assert_eq!(result[0], vec!["\"name\"", "OPT_TYPE_STRING", "\"help\""]);
    }

    #[test]
    fn test_parse_nested_braces() {
        let input = r#"{ "name", { .func_arg = fn }, "help" }"#;
        let result = parse_c_structure(input);
        assert_eq!(result.len(), 1);
        assert_eq!(result[0].len(), 3);
    }
}
