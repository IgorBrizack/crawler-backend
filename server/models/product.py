from typing import Optional
from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    website: str = Field(...)
    product_type: str = Field(...)

    class Config: 
        schema_extra = {
            "example": {
                "website": "mercadolivre",
                "product_type": "Geladeira",
            }
        }

class UpdateProductModel(BaseModel):
    website: Optional[str]
    description: Optional[str]
    product_type: Optional[str]
    price: Optional[str]
    external_link: Optional[str]
    image_link: Optional[str]

    class Config: 
        schema_extra = {
            "example": {
                "website": "Mercado Livre",
                "product_type": "Geladeira",
                "description": "Computador Apple",
                "price": "R$ 20000,00",
                "external_link": "www.apple.com/computador",
                "image_link": "www.aplle.com/image/computador"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {"error":error, "code": code, "message": message}
