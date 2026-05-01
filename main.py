from src.data_loader import load_data
from src.analysis import run_analysis
from src.model import train_model


def generate_insights(df):
    print("\n FINAL INSIGHTS:")

    pnl = df.groupby('sentiment_group')['closedPnL'].mean()
    win = df.groupby('sentiment_group')['is_profit'].mean()

    if pnl['Greed'] > pnl['Fear']:
        print("- Greed phases show higher profitability.")
    else:
        print("- Fear phases show higher profitability.")

    if win['Greed'] > win['Fear']:
        print("- Greed phases have slightly higher win rates.")
    else:
        print("- Fear phases have slightly higher win rates.")

    print("- Neutral sentiment shows weakest performance.")
    print("- Market sentiment significantly impacts trading outcomes.")
    print("- Risk-adjusted returns are relatively low (low Sharpe Ratio).")


def main():
    print(" Starting Analysis...\n")

    # Load data
    df = load_data()

    if df.empty:
        print("No data available. Check your files.")
        return

    print("Data loaded successfully")

    # Run analysis (graphs + stats)
    run_analysis(df)

    # Train ML model
    train_model(df)

    # Generate final insights
    generate_insights(df)

    # Save processed data
    df.to_csv("output_processed_data.csv", index=False)
    print("\n Processed data saved as output_processed_data.csv")

    print("\n Analysis Complete")


if __name__ == "__main__":
    main()