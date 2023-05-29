# biblioteca para lidar com chamadas asyncronas no mongo
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from scraper import manage_scrape

load_dotenv()

uri = os.environ.get('MONGO_URL')

client = MongoClient(uri)

db = client['products_data']

products_collection = db['products']

website_helper = {
        "mercadolivre": 'Mercado Livre',
        "buscape": 'Busca Pé'
    }

async def add_product(website: str, product: str):
    scrape_data = manage_scrape(website, product)

    products_collection.insert_many(scrape_data)
    new_products = products_collection.find({"website": website_helper[website], "product_type": product})

    products_list = []

    for prod in list(new_products):
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
    products_data_result = products_collection.find({"website": website_helper[website], "product_type": product})

    products_data = list(products_data_result)

    if not products_data:
        data = await add_product(website, product)
        return data
    
    products_list = []

    for prod in products_data:
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
