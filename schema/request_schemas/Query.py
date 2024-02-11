from pydantic import BaseModel
class Query(BaseModel):
    query: str
    collection:str = "qna"