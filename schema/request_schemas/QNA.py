from pydantic import BaseModel
class Prompt(BaseModel):
    qid:int
    question: str
    answer:str