from bitscrunch_sdk_unleashnft_v2.api.marketplace import MarketplaceAPI

# Initialize the SDK with your API key
sdk = MarketplaceAPI(api_key="3e351d7d91d9d7be9d733814928bfd85")


# Test fetching metadata with default parameters
try:
    default_metadata = sdk.get_marketplace_metadata()
    print("Default Marketplace Metadata:")
    print(default_metadata)
    print("\n")  # Print a newline for better readability
except Exception as e:
    print(f"Error fetching default metadata: {e}")

# Test fetching metadata with custom parameters
try:
    custom_metadata = sdk.get_marketplace_metadata(sort_order="asc", offset=10, limit=5)
    print("Custom Marketplace Metadata (sort_order=asc, offset=10, limit=5):")
    print(custom_metadata)
    print("\n")
except Exception as e:
    print(f"Error fetching custom metadata: {e}")

# Test with invalid parameters to handle edge cases
try:
    invalid_metadata = sdk.get_marketplace_metadata(sort_order="invalid_order", offset=-1, limit=101)
    print("Invalid Marketplace Metadata:")
    print(invalid_metadata)
    print("\n")
except Exception as e:
    print(f"Error fetching metadata with invalid parameters: {e}")

# Test the function to get marketplace analytics for OpenSea
# Test the function to get marketplace analytics for OpenSea
# Define the parameters for the marketplace analytics request

params = {
    "blockchain": "ethereum",  # Specify blockchain (default is 'ethereum')
    "time_range": "24h",       # Time range to filter results (default is '24h')
    "sort_by": "name",         # Property to sort the result set by (default is 'name')
    "sort_order": "desc",      # Sort order (default is 'desc')
    "offset": 0,               # Index of the page to return
    "limit": 30,               # Number of items to return
    "name": ["opensea"]        # Optional: filter by specific marketplace names
}

# Fetch marketplace analytics data
response = sdk.get_marketplace_analytics(**params)

# Print the response
if response:
    print(response)
else:
    print("Failed to retrieve data.")


# Fetch marketplace holder data for "opensea"
response = sdk.get_marketplace_holders(name=["opensea"], limit=30)

# Print the response
print(response)



# Fetch marketplace trader data for "opensea"
response = sdk.get_marketplace_traders(name=["opensea"], limit=30)

# Print the response
print(response)


# Fetch marketplace washtrade data for "opensea"
response = sdk.get_marketplace_washtrade(name=None, limit=30)

# Print the response
print(response)