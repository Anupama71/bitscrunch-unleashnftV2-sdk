from bitscrunch_sdk_unleashnft_v2.api.token import Token

# Initialize the SDK with your API key
token_sdk = Token(api_key="3e351d7d91d9d7be9d733814928bfd85")

# Fetch token balance details
try:
    token_balance_data = token_sdk.get_token_balance(
        blockchain="ethereum",
        token_address="0xdAC17F958D2ee523a2206206994597C13D831ec7",
        address="0x74989ef41bf5fdbcc252ab3eb3edcd986d4b0b0e",
        offset=0,
        limit=10
    )

    # Print the token balance details
    print("Token Balance Data:", token_balance_data)

except Exception as e:
    print(f"An error occurred: {e}")


# Fetch token metrics details
try:
    token_metrics_data = token_sdk.get_token_metrics(
        blockchain="ethereum",
        token_address="0xdAC17F958D2ee523a2206206994597C13D831ec7",
        offset=0,
        limit=10
    )

    # Print the token metrics details
    print("Token Metrics Data:", token_metrics_data)

except Exception as e:
    print(f"An error occurred: {e}")


# Fetch token holders details
try:
    token_holders_data = token_sdk.get_token_holders(
        blockchain="ethereum",
        token_address="0xdAC17F958D2ee523a2206206994597C13D831ec7",
        offset=0,
        limit=10
    )

    # Print the token holders details
    print("Token Holders Data:", token_holders_data)

except Exception as e:
    print(f"An error occurred: {e}")




# Fetch token transfers details
try:
    token_transfers_data = token_sdk.get_token_transfers(
        token_address="0xdAC17F958D2ee523a2206206994597C13D831ec7",
        blockchain="ethereum",
        time_range="all",
        offset=0,
        limit=10
    )

    # Print the token transfers details
    print("Token Transfers Data:", token_transfers_data)

except Exception as e:
    print(f"An error occurred: {e}")



# Define the token address you want to query
token_address = "0x4a220E6096B25EADb88358cb44068A3248254675"

# Call the get_token_price_prediction function
response = token_sdk.get_token_price_prediction(token_address)

# Print the response from the API
print(response)