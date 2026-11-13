import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)


def show_genres(df, chart_folder):
    genres = df["genres"].dropna().str.split(";").explode()
    top_genres = genres.value_counts().head(10)

    print("\nTop 10 game genres:")
    print(top_genres.to_string())

    plt.figure(figsize=(10, 6))
    plt.barh(top_genres.index, top_genres.values)
    plt.gca().invert_yaxis()
    plt.title("Top 10 Steam Game Genres")
    plt.xlabel("Number of Games")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.savefig(chart_folder / "genres.png")
    plt.show()
    plt.close()


def show_prices(df, chart_folder):
    paid_games = df.loc[df["price"] > 0, ["genres", "price"]].copy()
    paid_games["genres"] = paid_games["genres"].str.split(";")
    paid_games = paid_games.explode("genres")

    price_stats = paid_games.groupby("genres")["price"].agg(
        ["count", "mean", "median"]
    )
    top_prices = (
        price_stats.sort_values("count", ascending=False)
        .head(10)
        .sort_values("mean", ascending=False)
    )

    print("\nPrices by genre (paid games):")
    print(top_prices.round(2).to_string())

    plt.figure(figsize=(10, 6))
    plt.barh(top_prices.index, top_prices["mean"])
    plt.gca().invert_yaxis()
    plt.title("Average Price by Steam Game Genre")
    plt.xlabel("Average Price (GBP)")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.savefig(chart_folder / "genre_prices.png")
    plt.show()
    plt.close()


def show_releases(df, chart_folder):
    dates = pd.to_datetime(
        df["release_date"], format="%Y-%m-%d", errors="coerce"
    )
    yearly_counts = dates.dt.year.value_counts().sort_index()
    chart_counts = yearly_counts.loc[:2018]

    print("\nGame releases by year:")
    print(yearly_counts.to_string())
    print("\n2019 is incomplete and is excluded from the chart.")

    plt.figure(figsize=(10, 6))
    plt.plot(chart_counts.index, chart_counts.values, marker="o")
    plt.title("Steam Game Releases by Year (1997-2018)")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Games")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(chart_folder / "releases_by_year.png")
    plt.show()
    plt.close()


def show_ownership(df, chart_folder):
    games = df[["price", "owners"]].copy()
    bounds = games["owners"].str.split("-", expand=True).astype(int)
    games["estimated_owners"] = np.mean(bounds.to_numpy(), axis=1)
    games["type"] = np.where(games["price"] == 0, "Free", "Paid")

    stats = games.groupby("type")["estimated_owners"].agg(
        ["count", "mean", "median"]
    )
    stats = stats.loc[["Free", "Paid"]]

    print("\nEstimated game ownership:")
    print(stats.round().astype(int).to_string())
    print("Owner counts are estimates based on the midpoint of each range.")

    plt.figure(figsize=(8, 5))
    plt.bar(stats.index, stats["median"])
    plt.title("Estimated Steam Game Owners: Free vs. Paid")
    plt.xlabel("Game Type")
    plt.ylabel("Median Estimated Owners")
    plt.tight_layout()
    plt.savefig(chart_folder / "free_vs_paid.png")
    plt.show()
    plt.close()


def show_ratings(df, chart_folder):
    games = df.loc[
        df["price"] > 0,
        ["price", "positive_ratings", "negative_ratings"],
    ].copy()
    games["total_ratings"] = (
        games["positive_ratings"] + games["negative_ratings"]
    )
    games = games.loc[
        (games["total_ratings"] >= 20) & (games["price"] <= 50)
    ].copy()
    games["positive_pct"] = (
        100 * games["positive_ratings"] / games["total_ratings"]
    )
    correlation = games["price"].corr(games["positive_pct"])

    print(f"\nPrice and ratings ({len(games)} games):")
    print(f"Pearson correlation: {correlation:.3f}")
    print("Only paid games with at least 20 ratings and a price up to GBP 50 are included.")

    plt.figure(figsize=(10, 6))
    plt.scatter(games["price"], games["positive_pct"], s=8, alpha=0.2)
    plt.title("Steam Game Price vs. Positive Ratings")
    plt.xlabel("Price (GBP)")
    plt.ylabel("Positive Ratings (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(chart_folder / "price_vs_ratings.png")
    plt.show()
    plt.close()
