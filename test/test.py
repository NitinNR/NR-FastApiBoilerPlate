
import json
from env import getValue
import requests
from core import Core
def own_api_test(question):
    headers = {
        'Content-Type': 'application/json',
    }
    payload = json.dumps({
        "prompt": question
    })

    with requests.post("http://localhost:8000/getresp",headers=headers,stream=True,data=payload) as x_res:
        for line in x_res.iter_lines():
            print(json.loads(line)['text'])
            
            
def own_api_test2():
    with requests.get("http://localhost:8000",stream=True) as x_res:
        for line in x_res.iter_content(16):
            print(line)

        
def ask_llm(question):
    c = Core()
    gen = c.ask_llm(question)
    for g in gen:
        print(g)
    
            
# ask_llm("Why sky is blue in 10 words?")
user_question_query = "'include the date too?'"
given_context_from_chromadb = "'The historic document, the Declaration of Independence, was signed by the American colonies' representatives on July 4, 1776, marking the United States' independence from Britain.'"
template = f"Provide a concise answer to the question  Do not include any reasoning or additional information, just the answer from the given context. question:{user_question_query},context: {given_context_from_chromadb}"
# own_api_test("generate the answer only for given question and answer.don't add instructions from your side such as 'Based on the information provided', dont include such statement' question is 'how old kiran is ?' and answer is 'kiran was born in southern country and his date of birth is 20/1/1999 hi is quite old now?'")
own_api_test(template)
# own_api_test("this is strict instructions for you have to generate the answer only for given question and answer.don't add any instructions from your side such as 'Based on the information provided', dont include such statement' question is 'how old kiran is ?' and answer is 'kiran was born in southern country and his date of birth is 20/1/1999 hi is quite old now?'")
# own_api_test2()