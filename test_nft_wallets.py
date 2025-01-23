from bitscrunch_sdk_unleashnft_v2.api.nft_wallets import NFTWalletAPI

# Initialize the SDK with your API key
sdk = NFTWalletAPI(api_key="316dd88ae8840897e1f61160265d1a3f")
single_wallet_address = "0x8ab83d869f2bc250b781d26f6584fd5c562fdd9d"
multiple_wallet_address = "0x8ab83d869f2bc250b781d26f6584fd5c562fdd9d,0x6ed1B934670a5F42E0ba1E19FbFe5B6d1e2eDEa7"

single_wallet_analytics = sdk.get_wallet_analytics(wallets=single_wallet_address,time_range="all")
print(single_wallet_analytics);
multiple_wallet_analytics = sdk.get_wallet_analytics(wallets=multiple_wallet_address);
print(multiple_wallet_analytics);

# Fetch scores data for a single wallet address
single_wallet_scores = sdk.get_wallet_scores(wallets=single_wallet_address, time_range="all", sort_by="portfolio_value")
print("Single Wallet Scores:")
print(single_wallet_scores)

# Fetch scores data for multiple wallet addresses
multiple_wallet_scores = sdk.get_wallet_scores(wallets=multiple_wallet_address)
print("Multiple Wallet Scores:")
print(multiple_wallet_scores)

# Fetch traders data for a single wallet address
single_wallet_traders = sdk.get_wallet_traders(wallets=single_wallet_address, time_range="all", sort_by="traders")
print("Single Wallet Traders:")
print(single_wallet_traders)

# Fetch traders data for multiple wallet addresses
multiple_wallet_traders = sdk.get_wallet_traders(wallets=multiple_wallet_address)
print("Multiple Wallet Traders:")
print(multiple_wallet_traders)

# Fetch washtrade data for a single wallet address
single_wallet_washtrade = sdk.get_wallet_washtrade(wallets=single_wallet_address, time_range="all", sort_by="washtrade_volume")
print("Single Wallet Washtrade:")
print(single_wallet_washtrade)

# Fetch washtrade data for multiple wallet addresses
multiple_wallet_washtrade = sdk.get_wallet_washtrade(wallets=multiple_wallet_address)
print("Multiple Wallet Washtrade:")
print(multiple_wallet_washtrade)

single_wallet_profile = sdk.get_wallet_profile(wallets=single_wallet_address)
print("Single Wallet Profile:")
print(single_wallet_profile)

# Fetch profile data for multiple wallets
multiple_wallet_profile = sdk.get_wallet_profile(wallets=multiple_wallet_address)
print("Multiple Wallets Profile:")
print(multiple_wallet_profile)