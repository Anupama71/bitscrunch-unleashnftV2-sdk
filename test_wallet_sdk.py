from bitscrunch_sdk_unleashnft_v2.api.Wallet import Wallet

sdk = Wallet(api_key="316dd88ae8840897e1f61160265d1a3f")

response = sdk.get_defi_portfolio(addresses="0x8ab83d869f2bc250b781d26f6584fd5c562fdd9d")
print("DeFi Portfolio")
print(response)
nft_response = sdk.get_nft_portfolio(wallet="0x8ab83d869f2bc250b781d26f6584fd5c562fdd9d")
erc20_response = sdk.get_erc20_portfolio(address="0x8ab83d869f2bc250b781d26f6584fd5c562fdd9d")
label_response = sdk.get_wallet_labels(address="0x8ab83d869f2bc250b781d26f6584fd5c562fdd9d")

print("NFT Portfolio Response:", nft_response)
print("ERC-20 Portfolio Response:", erc20_response)
print("Wallet Labels Response:", label_response)