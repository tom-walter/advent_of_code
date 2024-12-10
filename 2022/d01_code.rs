use std::fs;


fn process_part1(payload: &str) -> String {
    let result = payload
        .split("\n\n")
        .map(|elf_load| {
            elf_load
            .lines()
            .map(|item| item.parse::<u32>().unwrap())
            .sum::<u32>()
        })
        .max()
        .unwrap();
    result.to_string()
}


fn main() {
    let file = fs::read_to_string("./d01.txt").unwrap();
    let result = process_part1(&file);
    println!("{}", result)
}