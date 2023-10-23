import pandas as pd

df_left = pd.read_excel("Example data tables.xlsx", sheet_name="Left table")
df_right = pd.read_excel("Example data tables.xlsx", sheet_name="Right table")

df_merged_left = pd.merge(df_left, df_right, on="instrument identifier", how="left")

df_merged_left.to_excel("left_merge.xlsx", sheet_name="Merged table", index=False)