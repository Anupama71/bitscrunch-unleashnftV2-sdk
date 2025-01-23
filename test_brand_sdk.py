from bitscrunch_sdk_unleashnft_v2.api.brand import NFT_Brand
from bitscrunch_sdk_unleashnft_v2.api.exceptions import APIError

# Initialize the SDK with your API key
api_key = "3e351d7d91d9d7be9d733814928bfd85"
brand_sdk = NFT_Brand(api_key)

# Get brand metadata for specific brands on Ethereum blockchain
try:
    brand_metadata = brand_sdk.get_brand_metadata(blockchain="ethereum", brand=["Coach","Givenchy"], offset=0, limit=30)
    if brand_metadata:
        print("NFT Brand Metadata:", brand_metadata)
    else:
        print("No brand metadata available.")
except APIError as e:
    print(f"API Error: {e}")

# Fetch brand metrics
try:
    brand_metrics = brand_sdk.get_brand_metrics(
        blockchain="ethereum",
        brand=["Coach"],
        time_range="24h",
        offset=0,
        limit=30,
        sort_by="mint_tokens",
        sort_order="desc"
    )
    if brand_metrics:
        print("NFT Brand Metrics:", brand_metrics)
    else:
        print("No brand metrics available.")
except APIError as e:
    print(f"API Error: {e}")


# Fetch brand profile
try:
    brand_profile = brand_sdk.get_brand_profile(
        blockchain="ethereum",
        brand=["Adidas"],
        time_range="7d",
        offset=0,
        limit=10,
        sort_by="diamond_hands",
        sort_order="desc"
    )
    if brand_profile:
        print("NFT Brand Profile:", brand_profile)
    else:
        print("No brand profile data available.")
except APIError as e:
    print(f"API Error: {e}")

import requests

url = "https://api.unleashnfts.com/api/v2/nft/brand/contract_metadata?blockchain=ethereum&offset=0&limit=30"

headers = {
    "accept": "application/json",
    "x-api-key": "3e351d7d91d9d7be9d733814928bfd85"
}

response = requests.get(url, headers=headers)

print(response.text)


# Fetch brand contract metadata
try:
    contract_metadata = brand_sdk.get_brand_contract_metadata(
        blockchain="ethereum",
        contract_address=["0x95353ab606de77d7cf69f5f346fe0e31d9557149"],  # Replace with actual contract addresses
        offset=0,
        limit=10,
    )
    if contract_metadata:
        print("NFT Brand Contract Metadata:", contract_metadata)
    else:
        print("No contract metadata available.")
except APIError as e:
    print(f"API Error: {e}")

# Fetch brand contract metrics
try:
    contract_metrics = brand_sdk.get_brand_contract_metrics(
        blockchain="ethereum",
        contract_address=["0x95353ab606de77d7cf69f5f346fe0e31d9557149"],  # Replace with actual contract address
        time_range="24h",
        offset=0,
        limit=10,
        sort_by="mint_tokens",
        sort_order="desc",
    )
    if contract_metrics:
        print("NFT Brand Contract Metrics:", contract_metrics)
    else:
        print("No contract metrics available.")
except APIError as e:
    print(f"API Error: {e}")



# Fetch brand contract profile
try:
    contract_profile = brand_sdk.get_brand_contract_profile(
        blockchain="ethereum",
        contract_address=["0x95353ab606de77d7cf69f5f346fe0e31d9557149"],  
        time_range="24h",
        offset=0,
        limit=10,
        sort_by="diamond_hands",
        sort_order="desc",
    )
    if contract_profile:
        print("NFT Brand Contract Profile:", contract_profile)
    else:
        print("No contract profile data available.")
except APIError as e:
    print(f"API Error: {e}")



# Fetch brand category information
try:
    brand_category = brand_sdk.get_brand_category(
        blockchain="ethereum",
        category=["Fashion"],  # Replace with desired categories
        offset=0,
        limit=10,
    )
    if brand_category:
        print("NFT Brand Category Information:", brand_category)
    else:
        print("No category information available.")
except APIError as e:
    print(f"API Error: {e}")