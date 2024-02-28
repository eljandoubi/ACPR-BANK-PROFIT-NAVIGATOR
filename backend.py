import os
import openai
import re
from io import StringIO

from dotenv import load_dotenv

load_dotenv()

endpoint = os.environ.get("AOAIEndpoint")
api_key = os.environ.get("AOAIKey")
deployment = os.environ.get("AOAIDeploymentId")

with open("system_promt.txt", "r", encoding="utf-8") as file:
    system_promt = file.read()

#user_prompt = " banque: [JP Morgan Chase, BNP Paribas, Groupe scociété génarle], trimestre: [1, 3,2], année: [2023, 2023,2023]"

client = openai.AzureOpenAI(
    base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
    api_key=api_key,
    api_version="2023-08-01-preview"
)

def exctracter(user_prompt:str)->str:
    """extract data from database"""
    completion = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        extra_body={
            "dataSources": [
                {
                    "type": "AzureCognitiveSearch",
                    "parameters": {
                        "endpoint": os.environ["SearchEndpoint"],
                        "key": os.environ["SearchKey"],
                        "indexName": os.environ["SearchIndex"],
                        "semanticConfiguration": "default",
                        "queryType": "vectorSemanticHybrid",
                        "fieldsMapping": {},
                        "inScope": True,
                        "roleInformation": system_promt,
                        "strictness": 3,
                        "topNDocuments": 20,
                        "embeddingDeploymentName": "ada-002"
                    }
                }
            ]
        },
        temperature=0,
        top_p=0,
        max_tokens=800,
        stop=None,

    )
    res = completion.model_dump()
    res=res["choices"][0]["message"]["content"]

    pattern = r'\{(.*?)\}'

    match = re.search(pattern, res, re.DOTALL)

    json_content = "{" + match.group(1) + "}"
 
    return StringIO(json_content)
