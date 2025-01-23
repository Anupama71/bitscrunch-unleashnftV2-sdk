from bitscrunch_sdk_unleashnft_v2.api.gaming import NFT_GamingApi

# Initialize the SDK with your API key
sdk = NFT_GamingApi(api_key="316dd88ae8840897e1f61160265d1a3f")

# Define the contract addresses (single or multiple)
single_contract_address = "0xfdf5acd92840e796955736b1bb9cc832740744ba"
multiple_contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d,0x60E4d786628Fea6478F785A6d7e704777c86a7c6"

# Fetch gaming metrics for single contract address
# single_contract_metrics = sdk.get_wallet_gaming_metrics(contract_addresses=single_contract_address)

# # Fetch gaming metrics for multiple contract addresses
# multiple_contract_metrics = sdk.get_wallet_gaming_metrics(contract_addresses=multiple_contract_address)

# # Print the results
# print("Single Contract Metrics:", single_contract_metrics)
# print("Multiple Contract Metrics:", multiple_contract_metrics)

# Fetch gaming metrics for all contracts (no contract address provided)
# all_contract_metrics = sdk.get_wallet_gaming_metrics()

# # Print the results
# print("All Contract Metrics:", all_contract_metrics)


# # Fetch gaming collection metrics for all contracts (no contract address provided)
# all_collection_metrics = sdk.get_wallet_gaming_collection_metrics()

# # Print the results
# print("All Gaming Collection Metrics:", all_collection_metrics)

# Fetch gaming collection metrics for a specific contract address
# single_contract_metrics = sdk.get_wallet_gaming_collection_metrics(contract_addresses="0xfdf5acd92840e796955736b1bb9cc832740744ba")

# # Print the results
# print("Single Contract Collection Metrics:", single_contract_metrics)



# # Initialize the SDK with your API key
# sdk = NFT_GamingApi(api_key="316dd88ae8840897e1f61160265d1a3f")

# # Fetch gaming collection trend metrics for all contracts (no contract address provided)
# all_collection_trends = sdk.get_wallet_gaming_collection_trend()

# # Print the results
# print("All Gaming Collection Trend Metrics:", all_collection_trends)

# Fetch gaming collection trend metrics for a specific contract address
single_contract_trend = sdk.get_wallet_gaming_collection_trend(contract_addresses="0xfdf5acd92840e796955736b1bb9cc832740744ba")

# Print the results
print("Single Contract Collection Trend Metrics:", single_contract_trend)
