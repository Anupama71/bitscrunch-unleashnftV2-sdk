from bitscrunch_sdk_unleashnft_v2.api.market_insights import NFT_Market_Insights
from bitscrunch_sdk_unleashnft_v2.api.exceptions import APIError

# Initialize the SDK with your API key
api_key = "3e351d7d91d9d7be9d733814928bfd85"
market_sdk = NFT_Market_Insights(api_key)

# Get market analytics for Ethereum blockchain and last 24 hours
try:
    response = market_sdk.get_market_analytics(blockchain="ethereum", time_range="24h")
    if response:
        print("Market Insights Data:", response)
    else:
        print("No data available.")
except APIError as e:
    print(f"API Error: {e}")


# Get holders' insights for Ethereum blockchain and last 24 hours
try:
    holders_data = market_sdk.get_holders_insights(blockchain="ethereum", time_range="24h")
    if holders_data:
        print("NFT Holders Insights:", holders_data)
    else:
        print("No holders insights available.")
except APIError as e:
    print(f"API Error: {e}")


# Get scores' insights for Ethereum blockchain and last 24 hours
try:
    scores_data = market_sdk.get_scores_insights(blockchain="ethereum", time_range="24h")
    if scores_data:
        print("NFT Scores Insights:", scores_data)
    else:
        print("No scores insights available.")
except APIError as e:
    print(f"API Error: {e}")

# Get traders' insights for Ethereum blockchain and last 24 hours
try:
    traders_data = market_sdk.get_traders_insights(blockchain="ethereum", time_range="24h")
    if traders_data:
        print("NFT Traders Insights:", traders_data)
    else:
        print("No traders insights available.")
except APIError as e:
    print(f"API Error: {e}")


# Get washtrade insights for Ethereum blockchain and last 24 hours
try:
    washtrade_data = market_sdk.get_washtrade_insights(blockchain="ethereum", time_range="24h")
    if washtrade_data:
        print("NFT Washtrade Insights:", washtrade_data)
    else:
        print("No washtrade insights available.")
except APIError as e:
    print(f"API Error: {e}")