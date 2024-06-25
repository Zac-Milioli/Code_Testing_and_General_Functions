import pandas as pd

df_correct = pd.read_csv(r"compare_dfs/correct.csv")
df_new = pd.read_csv(r"compare_dfs/new.csv")

print("\n\n\nCorrect:\n")
print(df_correct)
print("\n\n\nNew:\n")
print(df_new)
print("\n\n\n")
