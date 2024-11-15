from pydantic import BaseModel;
from typing import List;

class ImageRequest(BaseModel):
    name_of_the_object: str;
    position: list;
