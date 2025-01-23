# BitsCrunch UnleashNFTV2 SDK 2.0.0

## Overview

The **BitsCrunch UnleashNFTV2 SDK** is a Python-based Software Development Kit (SDK) designed to interact with **UnleashNFTs API V2**, offering a comprehensive suite of APIs for NFT, DeFi, and blockchain analytics. The SDK abstracts API complexities, enabling developers to easily access blockchain insights, analyze NFT collections, explore wallet data, and much more.

## Features

The SDK provides access to all the major API sections of **UnleashNFTs API V2**:

1. **Blockchains**  
   Retrieve blockchain-level details, performance metrics, and metadata.
   
2. **NFT Market Insights**  
   Analyze trading volumes, market performance, and trends across NFT marketplaces.
   
3. **NFT Marketplace**  
   Fetch marketplace-specific data, including transaction activity and metrics.
   
4. **NFT Collections**  
   Get detailed analytics and metadata for NFT collections on various blockchains.
   
5. **NFT Wallets**  
   Explore wallet activity, transaction history, and holdings in the NFT ecosystem.
   
6. **NFT**  
   Retrieve metadata, traits, and classifications for specific NFTs.
   
7. **NFT Gaming**  
   Access analytics and metadata for gaming-related NFTs and player statistics.
   
8. **NFT Transactions**  
   Analyze transaction data, including wash trading and sales performance.
   
9. **NFT Price Estimate**  
   Estimate the fair market value of NFTs based on historical data.
   
10. **NFT Brand**  
    Retrieve metadata, categories, and contract details for NFT brands.
    
11. **Token**  
    Analyze token trading volumes, liquidity, and other related data.
    
12. **DeFi**  
    Fetch metadata for DeFi pools, trading pairs, and liquidity information.
    
13. **Wallet**  
    Analyze wallet activity, balances, and transaction patterns.

## Use Cases

- Build dashboards for NFT and DeFi analytics.
- Evaluate NFT collections for investment or market research.
- Detect wash trading and fraudulent activities in NFT marketplaces.
- Analyze wallet behavior and token performance.
- Estimate NFT values to improve marketplace pricing transparency.

---

## Installation

Install the SDK using `pip`:

```bash
pip install bitscrunch-unleashnftV2-sdk==2.0.0
```

##Getting Started

Importing the SDK

You can import specific modules depending on the APIs you want to use. For example:

```bash
from bitscrunch_unleashnftV2_sdk import NFT_Collections, NFT_Marketplace
```

Initialization

Before using the SDK, initialize it with your API key:

```bash
from bitscrunch_unleashnftV2_sdk import DeFi

# Initialize the SDK with your API key
sdk = DeFi(api_key="Your-API-Key")
```

#Example Usage

Analyze NFT Market Insights

```bash
from bitscrunch_unleashnftV2_sdk import NFT_Marketplace
# Initialize the SDK
sdk = NFT_Marketplace(api_key="Your-API-Key")
market_sdk = NFT_Market_Insights(api_key)

# Get market analytics for Ethereum blockchain and last 24 hours
try:
    response = market_sdk.get_market_analytics(blockchain="ethereum", time_range="24h")
    if response:
        print("Market Insights Data:", response)
    else:
        print("No data available.")
except APIError as e:
    print(f"API Error: {e}")

