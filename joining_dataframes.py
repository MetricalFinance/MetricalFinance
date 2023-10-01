import pandas as pd

data_left = {
    "key": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "value_left": ["A", "B", "C", "D", "E", "F", "G", "I", "J", "K"]
}

data_right = {
    "key": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    "value_right": ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
}

df_left = pd.DataFrame(data_left)
df_right = pd.DataFrame(data_right)

df_merged_inner = pd.merge(df_left, df_right, on="key", how="inner")
df_merged_left = pd.merge(df_left, df_right, on="key", how="left")
df_merged_right = pd.merge(df_left, df_right, on="key", how="right")
df_merged_outer = pd.merge(df_left, df_right, on="key", how="outer")


print("df_left")
print(df_left)

print("\n")

print("df_right")
print(df_right)

print("\n")

print("df_merged_inner")
print(df_merged_inner)

print("\n")

print("df_merged_left")
print(df_merged_left)

print("\n")

print("df_merged_right")
print(df_merged_right)

print("\n")

print("df_merged_outer")
print(df_merged_outer)