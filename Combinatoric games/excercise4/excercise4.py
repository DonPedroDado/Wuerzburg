import pandas as pd

df = pd.read_csv("excercise4.csv")

positions_strategies = {(row['GP1'], row['GP2']): row['S'] for _, row in df.iterrows()}

try:
    strategyinput1 = int(input("Part 1: "))
    strategyinput2 = int(input("Part 2: "))
    key = (strategyinput1, strategyinput2)
    if key in positions_strategies:
        strategy = positions_strategies[key]
        if strategy == "loss":
            print("You lost")
        else:
            print(f"Remove {strategy} sticks")
    else:
        print("Invalid input: Combination not found")
except KeyError:
    print("Invalid input: KeyError")
except ValueError:
    print("Invalid input: Please enter valid integers")