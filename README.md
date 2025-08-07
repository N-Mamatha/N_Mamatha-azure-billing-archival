# N_Mamatha-azure-billing-archival
Cost optimization for azure cosmos DB billing records
# Azure Billing Archival - Cost Optimization Challenge

## Problem Statement

We're using Azure Cosmos DB to store billing records in a serverless system. The database is read-heavy, with over 2 million records (300KB each), and records older than 3 months are rarely accessed — causing high storage and RU/s costs.

## Solution Overview

We propose a **hybrid storage solution**:

- **Hot Data** (< 3 months): stays in **Cosmos DB**
- **Cold Data** (> 3 months): archived to **Azure Blob Storage**
- Azure Function reads from Cosmos DB; if not found, falls back to Blob Storage.
- Archival is managed by **Durable Function**, running daily.

### Architecture Diagram

![Architecture Diagram](diagrams/architecture.png)

## Benefits

✅ Cost-efficient (Blob storage is cheaper)  
✅ No API changes needed  
✅ No downtime  
✅ Data is always available

## Files & Folders

- `/functions/`: Durable Function pseudocode for archival
- `/scripts/`: Retrieval logic + fallback read script
- `/diagrams/`: Architecture PNG (upload separately)
- `chatgpt_conversation.pdf`: Full AI conversation exported

## Future Improvements

- Add query indexing via Azure Data Lake
- Implement metadata tagging in Blob for faster search
- Integrate Application Insights for telemetry
