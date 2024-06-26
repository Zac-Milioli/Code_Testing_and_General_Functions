import pandas as pd
import os
os.chdir(r"Python/Pandas/Testes para o LabEEE/compare_dfs")

df_desktop = pd.read_csv(r"desktop.csv")
df_webapp = pd.read_csv(r"webapp.csv")


df_desktop = df_desktop.loc[df_desktop['zone'] == "SALA"]
df_webapp = df_webapp.loc[df_webapp['zone'] == "SALA"]
df_desktop =df_desktop.drop(columns=['case', 'flux'])
df_webapp = df_webapp.drop(columns=['case', 'flux'])
print("\n\n\nDesktop:\n")
print(df_desktop)
print(f"Size: {len(df_desktop)}")
print("\n\n\nWebApp:\n")
print(df_webapp)
print(f"Size: {len(df_webapp)}")
print("\n\n\n")

merged_df = pd.merge(df_desktop, df_webapp, on=["gains_losses", "zone", "heat_direction"], suffixes=('_desktop', '_webapp'))

merged_df['value_comparison'] = merged_df['value_desktop'] == merged_df['value_webapp']

false_df = merged_df[merged_df["value_comparison"] == False]

true_df = merged_df[merged_df["value_comparison"] == True]

print("\n\n\nComparison Results:\n")
print(merged_df[['gains_losses', 'heat_direction', 'zone', 'value_desktop', 'value_webapp', 'HEI_desktop', 'HEI_webapp', 'value_comparison']])
print("\n\n\nFalse values:\n")
print(false_df[['gains_losses', 'heat_direction', 'zone', 'value_desktop', 'value_webapp', 'HEI_desktop', 'HEI_webapp', 'value_comparison']])
print("\n\n\nTrue values:\n")
print(true_df[['gains_losses', 'heat_direction', 'zone', 'value_desktop', 'value_webapp', 'HEI_desktop', 'HEI_webapp', 'value_comparison']])
print("\n\n\n")
