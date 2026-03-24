import pandas as pd

df = pd.read_csv("mtcars.csv")

print("\n1. 5 automobila sa najvecom potrosnjom:")
najveca_potrosnja = df.sort_values("mpg").head(5)
print((najveca_potrosnja[["car", "mpg"]]))


print("\n\n2. 3 automobila sa 8 cilindara sa najmanjom potrosnjom:")
cil8 = df[df["cyl"] == 8].sort_values("mpg", ascending=False).head(3)
print(cil8[["car", "cyl", "mpg"]])


print("\n\n3. Srednja potrosnja automobila sa 6 cilindara:")
srednja_6cil = df[df["cyl"] == 6]["mpg"].mean()
print(f"{srednja_6cil:.2f} mpg")


print("\n\n4. Srednja potrosnja automobila sa 4 cilindra sa masom izmedju 2000-2200 lbs:")
filter_4cil = df[(df["cyl"] == 4) & (df["wt"] * 1000 >= 2000) & (df["wt"] * 1000 <= 2200)]
srednja_4cil = filter_4cil["mpg"].mean()
print(f"{srednja_4cil:.2f} mpg")


print("\n\n5. Broj automobila sa automatskim i rucnim mjenjacem:")
mjenjac = df["am"].value_counts()
print(f"Sa automatskim: {mjenjac.get(0, 0)}")
print(f"Sa rucnim: {mjenjac.get(1, 0)}")


print("\n\n6. Automobili sa automatskim mjenjacem i snagom > 100ks:")
auto_100hp = df[(df["am"] == 0) & (df["hp"] > 100)]
print(f"Broj automobila: {len(auto_100hp)}")


print("\n\n7. Masa automobila u kg:")
df["wt_kg"] = (df["wt"] * 1000 * 0.453592).round(2)
print(df[["wt", "wt_kg"]].rename(columns={"wt": "masa u 1k lbs", "wt_kg": "masa u kg"}))