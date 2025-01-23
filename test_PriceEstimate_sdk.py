from bitscrunch_sdk_unleashnft_v2.api.price_estimate import NFT_Price_Estimate

# Initialize the SDK with your API key
price_estimate_sdk = NFT_Price_Estimate(api_key="316dd88ae8840897e1f61160265d1a3f")

# Fetch price estimate for a specific NFT
price_estimate_data = price_estimate_sdk.get_price_estimate(
    blockchain="ethereum",
    contract_address="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
    token_id="153"
)

# Print the results
print("NFT Price Estimate Data:", price_estimate_data)
# Fetch price estimate for a collection and its NFTs
collection_price_data = price_estimate_sdk.get_collection_price_estimate(
    blockchain="ethereum",
    contract_address="0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
    offset=0,
    limit=10
)

# Print the results
print("Collection Price Estimate Data:", collection_price_data)


# Fetch metadata for supported collections
supported_collections_data = price_estimate_sdk.get_supported_collections(
    blockchain="polygon",
    offset=0,
    limit=10
)

# Print the results
print("Supported Collections Data:", supported_collections_data)