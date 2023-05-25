# Helper scripts
Scripts useful for minor tasks and for local debugging. 

## Dependencies
- Scripts have been written on ***Python 3.11*** 
- Dependencies can be installed using 
    ```
    pip install -r requirements.txt
    ```


## Usage
Run --help on respective scripts to find usage 

## Pending
1. Manipulating Effective dated tables 
2. Creating dynamic dropdowns in Grafana 

## Completed 
### URL Encoder/Decoder
- url-en-de-code-string.py
### Base64 Encoder/Decoder
- base64-en-de-code-string.py
### GUID/uber-trace-id generator
- guid-generator.py 
### JWT token parser 
- jwt-decode.py
### Repo parser
The script fetches all remote branches from the repo and parses them based on convention. 
Also fetches `manifest.json` and checks the workflows key to find out whether the branch has a single workflow or multiple. 
Creates a list of all workflows in the file and makes API calls to delete the workflows from DB. 

Creates lists based on parsing and prints it out at the end. 
- filter-workflows-by-namespace.py