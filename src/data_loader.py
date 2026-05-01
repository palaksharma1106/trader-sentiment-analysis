import pandas as pd

def load_data():
    trades = pd.read_csv("data/historical_data.csv")
    sentiment = pd.read_csv("data/fear_greed_index.csv")

    # Convert datetime
    trades['Timestamp IST'] = pd.to_datetime(
        trades['Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce'
    )
    trades['date'] = trades['Timestamp IST'].dt.date

    sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce').dt.date

    # Rename columns
    trades.rename(columns={
        'Closed PnL': 'closedPnL',
        'Execution Price': 'price',
        'Size USD': 'size_usd'
    }, inplace=True)

    # Clean sentiment
    sentiment['classification'] = sentiment['classification'].str.strip()

    # Merge
    df = pd.merge(trades, sentiment[['date', 'classification']], on='date', how='inner')

    # Features
    df['is_profit'] = df['closedPnL'] > 0
    df['sentiment_group'] = df['classification'].replace({
        'Extreme Fear': 'Fear',
        'Extreme Greed': 'Greed'
    })

    df = df.dropna(subset=['closedPnL', 'sentiment_group'])

    return df