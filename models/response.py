from pydantic import BaseModel

class Response(BaseModel):
    summarized_text: str;
    category: str;
    probability: str;
