import pandas as pd
df = pd.read_csv(r"C:\Users\ACER\Downloads\DSAJourneySwaraj\Python-ML-AL\my_first_project\employees.csv")
print("--Original Data--")
print(df)
df["Bonus"] = df["Salary"]*0.10
print("\n --After Adding Bonus--")
print(df)
it_item = df[df["Department"]=="IT"]
print("\n--Just the IT Team--")
print(it_item)
top_performer = df.sort_values("Performance_Score", ascending=False).head(1)
print("\n--Top Performer--")
print(f"Winner {top_performer['Name'].values[0]}")
