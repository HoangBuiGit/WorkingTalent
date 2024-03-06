print('Start csv read application')
import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df["Attack"])

# for loop
for r,rij in df.iterrows():
    print("Test:",r,rij["Name"])