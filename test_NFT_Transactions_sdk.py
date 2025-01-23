from bitscrunch_sdk_unleashnft_v2.api.transactions import NFT_Transactions

# Initialize the SDK with your API key
transactions_sdk = NFT_Transactions(api_key="316dd88ae8840897e1f61160265d1a3f")

# Fetch NFT transactions for a specific contract and token ID
transaction_data = transactions_sdk.get_transactions(
    blockchain="ethereum",
    time_range="30d",
    contract_address="0x60E4d786628Fea6478F785A6d7e704777c86a7c6",
    token_id="19110",
    offset=0,
    limit=30
)

# Print the results
print("NFT Transactions Data:", transaction_data)
