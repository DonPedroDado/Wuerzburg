import pandas as pd

df = pd.read_csv("excersise3.csv")

positions_strategies = dict(zip(df['Position'], df['Strategy']))

try:
    strategyinput = input("Write your current position: ").upper()
    if positions_strategies[strategyinput] == "loss":
        print("You lost")
    else:
        print(f"Move to {positions_strategies[strategyinput]} from {strategyinput}")
except KeyError:
    print("Invalid input")
