# Azure Billing Archival – Cost Optimization Challenge

## Overview
This solution implements a tiered storage architecture to reduce costs in a read-heavy Azure serverless system using Cosmos DB and Blob Storage.

## Architecture
- **Hot Tier**: Azure Cosmos DB for recent billing records
- **Cold Tier**: Azure Blob Storage (Archive Tier) for records older than 3 months
- **Azure Functions**: Handle archival and retrieval seamlessly

![Architecture Diagram](docs/architecture.png)

## Features
- Zero downtime
- No changes to API contracts
- Simple deployment
- Cost-efficient storage

## Files
- `functions/`: Azure Functions for archival and retrieval
- `infra/`: Optional Bicep file for provisioning resources
- `conversation/`: Copilot chat transcript
