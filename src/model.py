from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

def train_model(df):
    features = df[['price', 'size_usd']]
    features = pd.get_dummies(features.join(df['sentiment_group']), drop_first=True)

    target = df['is_profit']

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("\n🤖 Model Performance:")
    print(classification_report(y_test, preds))