resource cosmosDb 'Microsoft.DocumentDB/databaseAccounts@2023-03-01' = {
  name: 'billing-cosmos'
  location: resourceGroup().location
  kind: 'GlobalDocumentDB'
  properties: {
    databaseAccountOfferType: 'Standard'
  }
}

resource blobStorage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'billingarchive'
  location: resourceGroup().location
  sku: {
    name: 'Standard_GRS'
  }
  kind: 'StorageV2'
}
