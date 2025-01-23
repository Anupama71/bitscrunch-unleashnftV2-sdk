from bitscrunch_sdk_unleashnft_v2.api.Supported_Blockchain import SupportedBlockchain
sdk = SupportedBlockchain(api_key="316dd88ae8840897e1f61160265d1a3f")

response = sdk.retrieve_supported_blockchains()
print(response)