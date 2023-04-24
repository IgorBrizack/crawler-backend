# biblioteca para lidar com chamadas asyncronas no mongo
import os
import motor.motor_asyncio

from scraper import manage_scrape

# "mongodb://crawler_web_db:27017" URL for container development

MONGO_DETAILS = 'mongodb://mongo:TrUj0l1LilHmLtcxnCUD@containers-us-west-137.railway.app:5845'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database_products = client.products

products_collection = database_products.get_collection("products_collection")

website_helper = {
        "mercadolivre": 'Mercado Livre',
        "buscape": 'Busca Pé'
    }

async def add_product(website: str, product: str):
    scrape_data = manage_scrape(website, product)

    await products_collection.insert_many(scrape_data)
    new_products = products_collection.find({"website": website_helper[website], "product_type": product})

    products_list = []

    for prod in await new_products.to_list(length=1000):
        products_list.append({
            "id": str(prod["_id"]),
            "product_type": str(prod["product_type"]),
            "description": prod["description"],
            "price": prod["price"],
            "website": prod["website"],
            "external_link": prod["external_link"],
            "image_link": prod['image_link']
        })


    return products_list

async def get_products(website: str, product: str):
    products_data = products_collection.find({"website": website_helper[website], "product_type": product})

    products_data_result = await products_data.to_list(length=1000)

    if not products_data_result:
        data = await add_product(website, product)
        return data
    
    products_list = []

    for prod in products_data_result:
        products_list.append({
            "id": str(prod["_id"]),
            "product_type": str(prod["product_type"]),
            "description": prod["description"],
            "price": prod["price"],
            "website": prod["website"],
            "external_link": prod["external_link"],
            "image_link": prod['image_link']
        })

    return products_list
