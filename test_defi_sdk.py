from bitscrunch_sdk_unleashnft_v2.api.defi import DeFi

# Initialize the SDK with your API key
sdk = DeFi(api_key="316dd88ae8840897e1f61160265d1a3f")

# Fetch metadata for a DeFi pool
response_metadata = sdk.get_defi_pool_metadata(blockchains="ethereum", pair_addresses="0x021a7e21fd1412d1b2b7e8ffafcfbd4384cb62e0")
print("DeFi Pool Metadata Response:")
print(response_metadata)

# Fetch metrics for a DeFi pool
response_metrics = sdk.get_defi_pool_metrics(blockchain="ethereum", pair_address="0x021a7e21fd1412d1b2b7e8ffafcfbd4384cb62e0")
print("DeFi Pool Metrics Response:")
print(response_metrics)

# Fetch metadata for a DeFi protocol
response_protocol = sdk.get_defi_protocol_metadata(blockchain="ethereum", protocol="unicly")
print("DeFi Protocol Metadata Response:")
print(response_protocol)

response = sdk.get_supported_defi_protocols(blockchains=["ethereum"])
print("Supported Defi Protocols")
print(response)
