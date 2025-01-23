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

Getting Started

Importing the SDK

You can import specific modules depending on the APIs you want to use. For example:

```bash
from bitscrunch_unleashnftV2_sdk import NFT_Market_Insights
```

Initialization

Before using the SDK, initialize it with your API key:

```bash
from bitscrunch_unleashnftV2_sdk import NFT_Market_Insights

# Initialize the SDK with your API key
api_key = "Your_API_Key"
market_sdk = NFT_Market_Insights(api_key)
```

#Example Usage

Analyze NFT Market Insights

```bash
from bitscrunch_unleashnftV2_sdk import NFT_Market_Insights

# Initialize the SDK with your API key
api_key = "Your API Key"
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

```

# Details Reagarding Different Functions/API(s):

#### A) NFT_Brand:

### 1. `get_brand_metadata`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `brand` (`list` of `str`): List of brand names to fetch metadata for, default is `None`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.

---

### 2. `get_brand_metrics`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `brand` (`list` of `str`): List of brand names to fetch metrics for, default is `None`.
   - `time_range` (`str`): Time range for metrics, default is `"24h"`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.
   - `sort_by` (`str`): Field to sort metrics by, default is `"mint_tokens"`.
   - `sort_order` (`str`): Sorting order, default is `"desc"`.

---

### 3. `get_brand_profile`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `brand` (`list` of `str`): List of brand names to fetch profile for, default is `None`.
   - `time_range` (`str`): Time range for profile data, default is `"24h"`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.
   - `sort_by` (`str`): Field to sort profile by, default is `"diamond_hands"`.
   - `sort_order` (`str`): Sorting order, default is `"desc"`.

---

### 4. `get_brand_contract_metadata`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `contract_address` (`list` of `str`): List of contract addresses to fetch metadata for, default is `None`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.

---

### 5. `get_brand_contract_metrics`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `contract_address` (`list` of `str`): List of contract addresses to fetch metrics for, default is `None`.
   - `time_range` (`str`): Time range for metrics, default is `"24h"`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.
   - `sort_by` (`str`): Field to sort metrics by, default is `"mint_tokens"`.
   - `sort_order` (`str`): Sorting order, default is `"desc"`.

---

### 6. `get_brand_contract_profile`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `contract_address` (`list` of `str`): List of contract addresses to fetch profile for, default is `None`.
   - `time_range` (`str`): Time range for profile data, default is `"24h"`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.
   - `sort_by` (`str`): Field to sort profile by, default is `"diamond_hands"`.
   - `sort_order` (`str`): Sorting order, default is `"desc"`.

---

### 7. `get_brand_category`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `"ethereum"`.
   - `category` (`list` of `str`): List of categories to fetch data for, default is `None`.
   - `offset` (`int`): Index of the page to return, default is `0`.
   - `limit` (`int`): Number of items to return in the result set, default is `30`.

#### B) CollectionAPI:

### 1. `get_collection_metadata`
   **Parameters:**
   - `sort_order` (`str`): The order to sort the result set, defaults to `'desc'`.
   - `offset` (`int`): Index of the page to return, defaults to `0`.
   - `limit` (`int`): Number of items to return in the result set, defaults to `30`.
   - `contract_address` (`str` or `list` of `str`): Comma-separated string or list of contract addresses to fetch metadata for, default is `None`.

---

### 2. `get_collection_analytics_data`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`list` of `str`): List of contract addresses to include in the aggregation, default is `None`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Pagination limit, default is `30`.
   - `sort_by` (`str`): Property to sort the results by, default is `'sales'`.
   - `time_range` (`str`): Time range for filtering the results, default is `'24h'`.
   - `sort_order` (`str`): Order to sort the result set by, default is `'desc'`.

---

### 3. `get_collection_holders_data`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`list` of `str`): List of contract addresses to include in the query, default is `None`.
   - `time_range` (`str`): The time range over which to filter results, default is `'24h'`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of results to return, default is `30`.
   - `sort_by` (`str`): Property to sort results by, default is `'holders'`.
   - `sort_order` (`str`): Order of sorting, default is `'desc'`.

---

### 4. `get_collection_scores`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`str` or `list` of `str`): Contract address or list of addresses to include in the query, default is `None`.
   - `time_range` (`str`): Time range for filtering results, default is `'24h'`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.
   - `sort_by` (`str`): Property to sort results by, default is `'market_cap'`.
   - `sort_order` (`str`): Order of sorting, default is `'desc'`.

---

### 5. `get_collection_traders_data`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`str` or `list` of `str`): Contract address or list of addresses to include in the query, default is `None`.
   - `time_range` (`str`): Time range for filtering results, default is `'24h'`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.
   - `sort_by` (`str`): Property to sort results by, default is `'traders'`.
   - `sort_order` (`str`): Order of sorting, default is `'desc'`.

---

### 6. `get_collection_washtrade_data`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`str` or `list` of `str`): Contract address or list of addresses to include in the query, default is `None`.
   - `time_range` (`str`): Time range for filtering results, default is `'24h'`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.
   - `sort_by` (`str`): Property to sort results by, default is `'washtrade_assets'`.
   - `sort_order` (`str`): Order of sorting, default is `'desc'`.

---

### 7. `get_collection_whales_data`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`str` or `list` of `str`): Contract address or list of addresses to include in the query, default is `None`.
   - `time_range` (`str`): Time range for filtering results, default is `'24h'`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.
   - `sort_by` (`str`): Property to sort results by, default is `'nft_count'`.
   - `sort_order` (`str`): Order of sorting, default is `'desc'`.

---

### 8. `get_collection_profile_data`
   **Parameters:**
   - `blockchain` (`str`): Blockchain type, default is `'ethereum'`.
   - `contract_address` (`str` or `list` of `str`): Contract address or list of addresses to include in the query, default is `None`.
   - `time_range` (`str`): Time range for filtering results, default is `'all'`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.
   - `sort_by` (`str`): Property to sort results by, default is `'washtrade_index'`.
   - `sort_order` (`str`): Order of sorting, default is `'desc'`.

---

#### C) DeFi:

### 1. `get_defi_pool_metadata(self, blockchains=None, pair_addresses=None, offset=0, limit=30)`
   **Parameters:**
   - `blockchains` (`list` of `str`): List of blockchain types to query, default is `None`.
   - `pair_addresses` (`list` of `str`): List of pair addresses for the DeFi pools, default is `None`.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.

---

### 2. `get_defi_pool_metrics(self, blockchain, pair_address, offset=0, limit=30)`
   **Parameters:**
   - `blockchain` (`str`): The blockchain type (e.g., 'Ethereum').
   - `pair_address` (`str`): The address of the DeFi pool.
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.

---

### 3. `get_defi_protocol_metadata(self, blockchain, protocol, offset=0, limit=30)`
   **Parameters:**
   - `blockchain` (`str`): The blockchain type (e.g., 'Ethereum').
   - `protocol` (`str`): The identifier for the DeFi protocol (e.g., 'Uniswap').
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, default is `30`.

---

### 4. `get_supported_defi_protocols(self, blockchains, offset=0, limit=30)`
   **Parameters:**
   - `blockchains` (`list` of `str`): List of blockchain types to query (e.g., ['Ethereum', 'Binance Smart Chain']).
   - `offset` (`int`): Pagination offset, default is `0`.
   - `limit` (`int`): Number of items to return, maximum is `100`, default is `30`.



### Similarly, all APIs under Unleash NFT v2 are defined.
