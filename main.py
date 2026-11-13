from pathlib import Path

from analysis import (
    load_data,
    show_genres,
    show_prices,
    show_releases,
    show_ownership,
    show_ratings,
)


def main():
    project_folder = Path(__file__).resolve().parent
    chart_folder = project_folder / "charts"
    chart_folder.mkdir(exist_ok=True)

    df = load_data(project_folder / "data" / "steam.csv")

    while True:
        print("\nSteam Games Data Analysis")
        print("1. Game genres")
        print("2. Game prices")
        print("3. Game releases by year")
        print("4. Free vs. paid games")
        print("5. Price and ratings")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            show_genres(df, chart_folder)
        elif choice == "2":
            show_prices(df, chart_folder)
        elif choice == "3":
            show_releases(df, chart_folder)
        elif choice == "4":
            show_ownership(df, chart_folder)
        elif choice == "5":
            show_ratings(df, chart_folder)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
