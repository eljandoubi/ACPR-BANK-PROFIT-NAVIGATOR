# BANK PROFIT NAVIGATOR

Extraction of key financial metrics from financial reports.

The application is deployed [here](https://acpr-equipe7-webapp.streamlit.app/).

## Installation
If you want to run it locally, you need to set some environment variables in the `.env` file:

```dotenv
AOAIKey=your_key
AOAIEndpoint=your_endpoint
AOAIDeploymentId=your_model

SearchEndpoint=your_endpoint
SearchKey=your_key
SearchIndex=your_index
```

To install dependencies

```bash
pip install -U -r requirements.txt
```

To run it type 

```bash
streamlit run webapp.py
```
