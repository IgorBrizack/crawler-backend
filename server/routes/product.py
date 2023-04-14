from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_product,
    get_products,
)

from server.models.product import (
    ErrorResponseModel, 
    ResponseModel, 
    ProductSchema,
    UpdateProductModel,
)

router = APIRouter()

@router.post("/", response_description="Insert Products Data")
async def add_products_data(product: ProductSchema = Body(...)):
    products = jsonable_encoder(product)
    new_products = await add_product(products["website"], products['product_type'])
    return ResponseModel(new_products, "Student added successfully")


@router.post("/get_products", response_description="Search for Products")
async def get_products_data(product: ProductSchema = Body(...)):
    products =  jsonable_encoder(product)
    data_products = await get_products(products["website"], products['product_type'])
    return ResponseModel(data_products, "Get products succesfully")