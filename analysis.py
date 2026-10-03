import pandas as pd

df = pd.read_csv("highest_salaries_by_major.csv")

# DATA CLEANING

# Clean columns "Early Career Pay" and "Mid-Career Pay" from "$" and "," | "% High Meaning" from "%"
# Convert salary data from string to interger
df["Early Career Pay"] = df["Early Career Pay"].str.replace("$", "").str.replace(",", "").astype(int)
df["Mid-Career Pay"] = df["Mid-Career Pay"].str.replace("$", "").str.replace(",", "").astype(int)

# Convert % data from string to float
df["% High Meaning"] = df["% High Meaning"].str.replace("%", "").astype(float)

# Create a new index column
df = df.drop(columns=["Index"])
df = df.reset_index(drop=True)

# Insert Difference column
diff_column = df["Mid-Career Pay"] - df["Early Career Pay"]
df.insert(4, "Mid to Early Diff", diff_column)

# Top 5 Early Career Pay
top_early = df.nlargest(5, "Early Career Pay")[["Major", "Early Career Pay"]]
# Low 5 Early Career Pay
low_early = df.nsmallest(5, "Early Career Pay")[["Major", "Early Career Pay"]]

# Top 5 Mid-Career
top_mid = df.nlargest(5, "Mid-Career Pay")[["Major", "Mid-Career Pay"]]
# Low 5 Mid-Career
low_mid = df.nsmallest(5, "Mid-Career Pay")[["Major", "Mid-Career Pay"]]

# Top 5 Mid to Early Diff
top_dif = df.nlargest(5, "Mid to Early Diff")[["Major", "Mid to Early Diff"]]
# Low 5 Mid to Early Diff
low_dif = df.nsmallest(5, "Mid to Early Diff")[["Major", "Mid to Early Diff"]]

# Top % High Meaning
clean_df = df.dropna(subset=["% High Meaning"])
top_meaning = clean_df.nlargest(5, "% High Meaning")[["Major", "% High Meaning"]]
# Low % High Meaning
low_meaning = clean_df.nsmallest(5, "% High Meaning")[["Major", "% High Meaning"]]

# pip install openpyxl
def combine_top_low(top, low, col_name):
    top = top.reset_index(drop=True)
    low = low.reset_index(drop=True)
    top.columns = [f'Top {col_name} Major', f'Top {col_name}']
    low.columns = [f'Low {col_name} Major', f'Low {col_name}']
    return pd.concat([top, low], axis=1)

# Add the insights to a new Excel file
with pd.ExcelWriter('salary_analysis.xlsx') as writer:
    combine_top_low(top_early, low_early, 'Early Career').to_excel(writer, sheet_name='Early Career Pay', index=False)
    combine_top_low(top_mid, low_mid, 'Mid Career').to_excel(writer, sheet_name='Mid-Career Pay', index=False)
    combine_top_low(top_dif, low_dif, 'Diff').to_excel(writer, sheet_name='Salary Growth', index=False)
    combine_top_low(top_meaning, low_meaning, 'Meaning').to_excel(writer, sheet_name='High Meaning', index=False)
