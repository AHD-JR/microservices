import inventory_pb2_grpc, inventory_pb2
import grpc
import logging


def category_stub():
    with grpc.insecure_channel('localhost:243243') as channel:
        stub = inventory_pb2_grpc.CategoryServiceStub(channel)
        
        response = stub.CreateCategory(inventory_pb2.CategoryRequest(name="R"))
        print(f"\n Added New Category. ID: { response._id}\n\n")

        response = stub.GetCategories(inventory_pb2.PaginationRequest(page=1, limit=5))
        print("All Categories:")
        displayItems(response.categories)

        response = stub.GetCategory(inventory_pb2.CategoryId(_id="65a9e2e22aebfdb76445f0ec"))
        print(f"{response.name} Category:")
        print(f"{response}\n\n")

        response = stub.UpdateCategory(inventory_pb2.UpdateCategoryRequest(_id="65a9e533776eb47fe3b25cc8", request_body=inventory_pb2.CategoryRequest(name="Accessory")))
        print(f"Updated a Category. ID: { response._id}\n\n")

        response = stub.DeleteCategory(inventory_pb2.CategoryId(_id="65aa0911e4dd64b622388c97"))
        print("Category deleted!\n\n")

        response = stub.SearchCategory(inventory_pb2.SearchRequest(query="on"))
        print("Search result:")
        displayItems(response.categories)


def product_stub():
    with grpc.insecure_channel('localhost:243243') as channel:
        stub = inventory_pb2_grpc.ProductServiceStub(channel)

        req_data = {
            "name": "Dell 34-inches Gaming Display", 
            "category": inventory_pb2.CategoryRequest(name="Electronics"),
            "price": 750000, 
            "quanitiy": 10
        } 
        response = stub.CreateProduct(inventory_pb2.ProductRequest(**req_data))
        print(f"\n Added New Product. ID: { response._id}\n\n")

        response = stub.GetProducts(inventory_pb2.PaginationRequest(page=1, limit=10))
        print("All Products:")
        displayItems(response.products)

        response = stub.GetProduct(inventory_pb2.ProductId(_id="65ab5b94c882889c5236dc31"))
        print(f"{response.name} detail:")
        print(f"{response}\n\n")

        req_data = {
            "name": "Rice", 
            "category": inventory_pb2.CategoryRequest(name="Food"),
            "price": 60000, 
            "quanitiy": 100
        } 

        req_body = inventory_pb2.ProductRequest(**req_data)
        response = stub.UpdateProduct(inventory_pb2.UpdateProductRequest(_id="65ab5b94c882889c5236dc31", request_body=req_body))
        print(f"Updated a Category. ID: { response._id}\n\n")

        response = stub.DeleteProduct(inventory_pb2.ProductId(_id="65ab8f2426e6da71d7d723f6"))
        print("Product deleted! \n\n")

        response = stub.SearchProduct(inventory_pb2.SearchRequest(query="ce"))
        print("Search result:")
        displayItems(response.products)

import pytz   
from datetime import datetime 
def order_stub():
    with grpc.insecure_channel("localhost:243243") as channel:
        stub = inventory_pb2_grpc.OrderServiceStub(channel)

        ng_tz = pytz.timezone('Africa/Lagos')

        address = {
            "street": "Graceland",
            "city": "Zaria",
            "state": "Kaduna",
            "country": "Nigeria",
            "zip_code": "123099"
        }

        products = [
            {
                "name": "Rice", 
                "category": inventory_pb2.CategoryRequest(name="Food"),
                "price": 60000, 
                "quanitiy": 100
            },
            {
            "name": "Spaggheti", 
            "category": inventory_pb2.CategoryRequest(name="Food"),
            "price": 60000, 
            "quanitiy": 100
            }
        ]

        total_price = 0
        for product in products:
            total_price += product['price'] 


        data = {
            'products': products,
            'shipping_address': inventory_pb2.Address(**address),
            'created_at': datetime.now(ng_tz),
            'created_by': "username",
            'total_price': total_price,
            'order_status': "Fulfilled"
        }

        response = stub.CreateOrder(inventory_pb2.OrderRequest(**data))
        print(f"\n Added New order. ID: { response._id}\n\n")

        
def displayItems(items: list):
    for item in items:
        print(item)
    print("\n\n")


def run():
    category_stub()
    product_stub()
    order_stub()



if __name__ == "__main__":
    logging.basicConfig()
    run()