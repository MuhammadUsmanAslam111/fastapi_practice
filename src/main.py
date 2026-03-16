from fastapi import FastAPI, Query
from product import get_products
app = FastAPI()
from pydantic import BaseModel
class Product(BaseModel):
    id: int
    name: str
    

@app.get("/")
def read_root():
    return {"Hello": "World"}
  
@app.get("/products")
def search_products(name: str = Query(None)):
    products = get_products()
    print("hello")
    if name:
        # case-insensitive search
        return [p for p in products if name.lower() in p["name"].lower()]
    return products

@app.get("/about")
def get_about():
    return {"message": "This is a sample FastAPI application."}

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, name: str = Query(None) ):
    """
    Get a product by ID.
    Optionally filter by name (case-insensitive).
    """
    products = get_products()
    filtered = [p for p in products if p["id"] == product_id]
    
    if name:
        filtered = [p for p in filtered if name.lower() in p["name"].lower()]
    
    if not filtered:
        return {"error": "Product not found"}
    
    return filtered[0]  # return single product
@app.post("/products")
def create_product(product: Product):
    # In a real application, you'd save the product to a database here
    return {"message": "Product created", "product": product.dict()}


@app.post("/products/{product_id}/{product_name}")
def add_product(product_id: int, product_name: str, product: Product):
    # In a real app, you'd insert this into your database
    return {
        "message": "Product added",
        "product_id": product_id,
        "product_name": product_name,
        "product_details": product.dict()
    }