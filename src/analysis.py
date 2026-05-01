import matplotlib.pyplot as plt
import seaborn as sns

def run_analysis(df):
    print("\n📊 Average PnL by Sentiment:")
    print(df.groupby('sentiment_group')['closedPnL'].mean())

    print("\n📈 Win Rate by Sentiment:")
    print(df.groupby('sentiment_group')['is_profit'].mean())

    print("\n📊 Total Trades:")
    print(df['sentiment_group'].value_counts())
    df['cumulative_pnl'] = df['closedPnL'].cumsum()

    plt.figure()
    df['cumulative_pnl'].plot(title="Cumulative Profit Over Time")
    plt.show()

    df['rolling_max'] = df['cumulative_pnl'].cummax()
    df['drawdown'] = df['cumulative_pnl'] - df['rolling_max']

    plt.figure()
    df['drawdown'].plot(title="Drawdown Analysis")
    plt.show()

    sharpe = df['closedPnL'].mean() / df['closedPnL'].std()
    print("\n📊 Sharpe Ratio:", sharpe)

    # Plots
    sns.set(style="whitegrid")

    plt.figure()
    sns.boxplot(x='sentiment_group', y='closedPnL', data=df)
    plt.title("PnL Distribution by Sentiment")
    plt.show()

    plt.figure()
    df.groupby('sentiment_group')['is_profit'].mean().plot(kind='bar')
    plt.title("Win Rate by Sentiment")
    plt.show()