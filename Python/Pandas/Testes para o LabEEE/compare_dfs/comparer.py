import pandas as pd

df_correct = pd.read_csv(r"compare_dfs/correct.csv")
df_new = pd.read_csv(r"compare_dfs/new.csv")


df_correct = df_correct.loc[df_correct['zone'] == "BWC"]
df_new = df_new.loc[df_new['zone'] == "BWC"]
df_correct =df_correct.drop(columns=['case', 'flux'])
df_new = df_new.drop(columns=['case', 'flux'])
print("\n\n\nCorrect:\n")
print(df_correct)
print("\n\n\nNew:\n")
print(df_new)
print("\n\n\n")

merged_df = pd.merge(df_correct, df_new, on=["gains_losses", "zone", "heat_direction"], suffixes=('_correct', '_new'))

merged_df['value_comparison'] = merged_df['value_correct'] == merged_df['value_new']

false_df = merged_df[merged_df["value_comparison"] == False]

true_df = merged_df[merged_df["value_comparison"] == True]

print("\n\n\nComparison Results:\n")
print(merged_df[['gains_losses', 'heat_direction', 'zone', 'value_correct', 'value_new', 'HEI_correct', 'HEI_new', 'value_comparison']])
print("\n\n\nFalse values:\n")
print(false_df[['gains_losses', 'heat_direction', 'zone', 'value_correct', 'value_new', 'HEI_correct', 'HEI_new', 'value_comparison']])
print("\n\n\nTrue values:\n")
print(true_df[['gains_losses', 'heat_direction', 'zone', 'value_correct', 'value_new', 'HEI_correct', 'HEI_new', 'value_comparison']])
print("\n\n\n")
