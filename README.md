#  Trader Performance vs Market Sentiment

## Overview

This project analyzes how **market sentiment (Fear vs Greed)** affects trader performance using historical trading data.

It focuses on identifying patterns in **profitability, win rate, and risk** to support better trading decisions.



##  What I Did

* Cleaned and merged trading + sentiment data
* Created features like `is_profit` and `sentiment_group`
* Analyzed performance across market conditions
* Built a **Random Forest model** to predict trade profitability
* Calculated **risk metrics** like drawdown and Sharpe ratio



## Key Insights

* Fear markets show **higher win rates (safer trades)**
* Greed markets show **higher risk and volatility**
* Trade size significantly impacts outcomes
* Market sentiment influences trader performance



## Project Structure


project/
├── data/
├── src/
│   ├── data_loader.py
│   ├── analysis.py
│   └── model.py
├── main.py
```



## Run the Project

```
pip install -r requirements.txt
python main.py
```



##  Output

* Console insights
* Graphs (PnL, drawdown, trends)
* `final_output.csv`



## Conclusion

This project shows how combining **market sentiment with trading data** can generate actionable insights and improve strategy decisions.


