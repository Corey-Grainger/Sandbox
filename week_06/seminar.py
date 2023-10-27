from monster import Monster

all_monsters = [Monster("Mike", 340, "blue"), Monster("James", 14, "green"), Monster("Randall", 24, "purple"), Monster("Jim", 2, "red")]
scary_monsters = [monster for monster in all_monsters if monster.is_scary()]

print(f"Should be Mike, James, Randall, Jim: \n{all_monsters}")
print(f"Should be Mike, Randal, Jim: \n{scary_monsters}")


