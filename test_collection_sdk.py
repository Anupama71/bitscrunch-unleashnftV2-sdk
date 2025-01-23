from bitscrunch_sdk_unleashnft_v2.api.collection import CollectionAPI

# Initialize the SDK with your API key
sdk = CollectionAPI(api_key="316dd88ae8840897e1f61160265d1a3f")
single_contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
multiple_contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d,0x60E4d786628Fea6478F785A6d7e704777c86a7c6"

# Fetch metadata for a single contract address
metadata_single = sdk.get_collection_metadata(contract_address="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d")
print("Single Contract Address Metadata:")
print(metadata_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
contract_addresses = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d,0x60E4d786628Fea6478F785A6d7e704777c86a7c6"
metadata_multiple = sdk.get_collection_metadata(contract_address=contract_addresses,limit=1)
print("Multiple Contract Addresses Metadata:")
print(metadata_multiple)

analytics_single = sdk.get_collection_analytics_data(contract_address="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d")
print("Single Contract Address Analytics:")
print(analytics_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
contract_addresses = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d,0x60E4d786628Fea6478F785A6d7e704777c86a7c6"
analytics_multiple = sdk.get_collection_analytics_data(contract_address=contract_addresses,limit=1)
print("Multiple Contract Addresses Analytics:")
print(analytics_multiple)

holders_single = sdk.get_collection_holders_data(contract_address=single_contract_address)
print("Single Contract Address Holders Data:")
print(holders_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
holders_multiple = sdk.get_collection_holders_data(contract_address=multiple_contract_address,limit=1)
print("Multiple Contract Addresses Holders Data:")
print(holders_multiple)

scores_single = sdk.get_collection_scores(contract_address=single_contract_address)
print("Single Contract Address Scores Data:")
print(scores_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
scores_multiple = sdk.get_collection_scores(contract_address=multiple_contract_address,limit=1)
print("Multiple Contract Addresses Scores Data:")
print(scores_multiple)

scores_single = sdk.get_collection_traders_data(contract_address=single_contract_address)
print("Single Contract Address Traders Data:")
print(scores_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
scores_multiple = sdk.get_collection_traders_data(contract_address=multiple_contract_address,limit=1)
print("Multiple Contract Addresses Traders Data:")
print(scores_multiple)

scores_single = sdk.get_collection_washtrade_data(contract_address=single_contract_address)
print("Single Contract Address washtrade Data:")
print(scores_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
scores_multiple = sdk.get_collection_washtrade_data(contract_address=multiple_contract_address,limit=1)
print("Multiple Contract Addresses washtrade Data:")
print(scores_multiple)

scores_single = sdk.get_collection_whales_data(contract_address=single_contract_address)
print("Single Contract Address whales Data:")
print(scores_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
scores_multiple = sdk.get_collection_whales_data(contract_address=multiple_contract_address,limit=1)
print("Multiple Contract Addresses whales Data:")
print(scores_multiple)

scores_single = sdk.get_collection_profile_data(contract_address=single_contract_address)
print("Single Contract Address collection Profile Data:")
print(scores_single)
print("\n")  # Print a newline for better readability

# Fetch metadata for multiple contract addresses
scores_multiple = sdk.get_collection_profile_data(contract_address=multiple_contract_address,limit=1)
print("Multiple Contract Addresses collection Profile Data:")
print(scores_multiple)



