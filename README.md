# CrossPrism API
Note: The API is not meant to be exposed to external, or untrusted users. It's a single threaded, non-security hardened interface for single, trusted users.  
The main app: https://apps.apple.com/us/app/crossprism-photo-keywords/id1638429352?mt=12  
Also see the LR plugin: https://github.com/crossprism/lrplugin  

# Operations
- classify
  - Execute classification operations against images or features
- extract
  - Obtain features/embeddings from an image
- train
  - Train a trainer with images and labels
- screener
  - Sync images with the screener UI in the app
- trees
  - Get the list of domains/trees
- trainers
  - Get the list of available trainers
- screeners
  - Get the list of screeners
- status
  - Check the server availability
