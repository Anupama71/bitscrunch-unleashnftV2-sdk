from bitscrunch_sdk_unleashnft_v2.api.Nft import NFTAPI

# Initialize the SDK with your API key
sdk = NFTAPI(api_key="316dd88ae8840897e1f61160265d1a3f")
contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
token_ids = ["1000"]

nft_traders = sdk.get_nft_traders(contract_addresses=contract_address, token_ids=token_ids,time_range="all")
print("NFT Traders Data:")
print(nft_traders)

nft_analytics = sdk.get_nft_analytics(contract_addresses=contract_address, token_ids=token_ids, time_range="all")
print("NFT Analytics Data:")
print(nft_analytics)

nft_washtrade = sdk.get_nft_washtrade(contract_addresses=contract_address, token_ids=token_ids, time_range="all")
print("NFT Washtrade Data:")
print(nft_washtrade)

nft_holders = sdk.get_nft_holders(contract_addresses=contract_address, token_ids=token_ids, time_range="all")
print("NFT Holders Data:")
print(nft_holders)

nft_scores = sdk.get_nft_scores(contract_addresses=contract_address, token_ids=token_ids, time_range="all")
print("NFT Scores Data:")
print(nft_scores)

nft_top_deals = sdk.get_nft_top_deals(sort_by="deal_score", sort_order="desc")
print("NFT Top Deals Data:")
print(nft_top_deals)