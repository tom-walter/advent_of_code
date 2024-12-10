use std::fs::File;
use std::io::Read;
use std::collections::HashMap;

fn load_unaltered(filepath: &str) -> String {
    let mut file = File::open(filepath).expect("Error reading file");
    let mut payload = String::new();
    file.read_to_string(&mut payload).unwrap();
    payload
}

fn main () {
    let payload = load_unaltered("./d02.txt");
    let possible_game_sets: HashMap<&str, u8> = HashMap::from([
        ("red", 12),
        ("green", 13),
        ("blue", 14),
    ]);

    let mut possible_game_solutions: Vec<u32> = Vec::new();
    for line in payload.lines() {
        let parts: Vec<&str> = line.split(":").collect();

        let game = parts[1];
        let game_id: u32 = parts[0].trim().split_whitespace().last().unwrap_or("0").parse().unwrap_or(0);

        let possible: Vec<bool> = game
            .split(';')
            .flat_map(|sets| {
                sets.split(',').map(|role| {
                    let parts: Vec<&str> = role.trim().split_whitespace().collect();
                    let (num, col) = (parts[parts.len() - 2], parts[parts.len() - 1]);
                    let num: u8 = num.parse().unwrap_or(0);

                    num <= *possible_game_sets.get(&col).unwrap_or(&0)
                })
            })
            .collect();

        if possible.iter().all(|&p| p) {
            possible_game_solutions.push(game_id);
        }
    }

    let total: u32 = possible_game_solutions.iter().sum();
    println!("{}", total);

}