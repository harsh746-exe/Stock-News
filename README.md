# Stock Price Alert with News Updates 📈📰

This Python script tracks the stock price of a specified company and fetches related news articles when the stock price changes significantly (5% or more). If the condition is met, the script provides a percentage change alert along with the top 3 news articles about the company.

## Features
- **Stock Price Monitoring**: Uses the Alpha Vantage API to fetch daily stock price data.
- **News Updates**: Fetches top 3 news articles related to the company using the News API.
- **Customizable Threshold**: Triggers alerts when stock price changes exceed 5% (can be modified as needed).
- **Formatted Alerts**: Displays percentage change, news headlines, and brief descriptions.

## Prerequisites
1. Python 3.x
2. Install the following Python libraries:
   - `requests`

   You can install the required library using:
   ```bash
   pip install requests
   ```

3. API Keys:
   - Alpha Vantage API key: Obtain from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
   - News API key: Obtain from [News API](https://newsapi.org/).

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-price-alert.git
   ```
2. Navigate to the project directory:
   ```bash
   cd stock-price-alert
   ```
3. Update the script with your API keys:
   - Replace `API_KEY` with your Alpha Vantage API key.
   - Replace `NEWS_API` with your News API key.

4. Run the script:
   ```bash
   python stock_alert.py
   ```

## Output Example
When the stock price change exceeds the threshold, the script will display alerts like:

```
TSLA: 🔺5.12%
Headline: Tesla Achieves Record High Sales in 2024
Brief: Tesla Inc. announced its highest-ever sales numbers, reflecting strong demand for EVs.

TSLA: 🔺5.12%
Headline: Elon Musk Unveils Tesla's New AI Plans
Brief: Tesla is now leveraging AI to revolutionize its EV production process.

TSLA: 🔺5.12%
Headline: Tesla's Expansion into Renewable Energy
Brief: The company is diversifying into renewable energy with significant investments.
```

## Customization
- Modify the `STOCK` and `COMPANY_NAME` variables to monitor different companies.
- Adjust the price change threshold by modifying the `if per_chng <=-5 or per_chng >= 5` condition.

