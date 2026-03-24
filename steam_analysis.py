import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("steam.csv")

df = df[
    [
        "name",
        "price",
        "average_playtime",
        "positive_ratings",
        "negative_ratings",
        "genres",
    ]
]

df = df.dropna()
df = df[df["average_playtime"] > 0]
df = df[df["price"] >= 0]
df = df[(df["positive_ratings"] + df["negative_ratings"]) > 50]

df["rating"] = df["positive_ratings"] / (
    df["positive_ratings"] + df["negative_ratings"]
)

df_story = df[
    df["genres"].str.contains("RPG|Adventure|Indie", case=False, na=False)
].copy()

print("Total filtered games:", len(df))
print("Story-like games:", len(df_story))

df_story = df_story[df_story["price"] > 0]
df_story = df_story[df_story["average_playtime"] < 10000]

print("\nCorrelations:")
print("Price vs Playtime:", df_story["price"].corr(df_story["average_playtime"]))
print("Playtime vs Rating:", df_story["average_playtime"].corr(df_story["rating"]))
print("Price vs Rating:", df_story["price"].corr(df_story["rating"]))

plt.figure()
plt.scatter(df_story["price"], df_story["average_playtime"], alpha=0.3)
plt.yscale("log")
plt.xlabel("Price")
plt.ylabel("Playtime (log)")
plt.title("Story-like Games: Price vs Playtime")
plt.show()

df_story["playtime_hours"] = df_story["average_playtime"] / 60
df_story["value"] = (
    df_story["playtime_hours"] * df_story["rating"]
) / df_story["price"]

print("\nTop 10 Value Games:")
print(df_story.sort_values("value", ascending=False)[["name", "value"]].head(10))