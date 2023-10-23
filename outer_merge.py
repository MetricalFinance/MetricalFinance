import pandas as pd

df_left = pd.read_excel("Example data tables.xlsx", sheet_name="Left table")
df_right = pd.read_excel("Example data tables.xlsx", sheet_name="Right table")

df_merged_outer = pd.merge(df_left, df_right, on="instrument identifier", how="outer")

df_merged_outer.to_excel("outer_merge.xlsx", sheet_name="Merged table", index=False)



