import grpc
import inventory_pb2, inventory_pb2_grpc
from app.configs.db import product_collection
from bson import ObjectId


class ProductServiceImplementation(inventory_pb2_grpc.ProductServiceServicer):
    def CreateProduct(self, request, context):
        try:
            product = product_collection.find_one({'name': request.name})
            if product:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("Product already exists!")
                return inventory_pb2.ID

            data = {
                'name': request.name,
                'category': request.category.name,
                'price': request.price,
                'quanitiy': request.quanitiy
            }

            new_product = product_collection.insert_one(data)
            if new_product.inserted_id: 
                return inventory_pb2.ID(_id=str(new_product.inserted_id))
            
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ID()


    def GetProducts(self, request, context):
        try:
            products = list(product_collection.find({}).skip((request.page - 1) * request.limit).limit(request.limit))
            if not products:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No products found!")
                return inventory_pb2.ProductResponseList()

            products = [{k: str(v) if k == "_id" else v for k, v in product.items()} for product in products]

            return inventory_pb2.ProductResponseList(products=products)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ProductResponseList()

        
    def GetProduct(self, request, context):
        try:
            product = product_collection.find_one({'_id': ObjectId(request._id)})
            if not product:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such product!")
                return inventory_pb2.ProductResponse()
                
            product['_id'] = str(product['_id'])
            return inventory_pb2.ProductResponse(**product)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ProductResponse()
        

    def UpdateProduct(self, request, context):
        try:
            product = product_collection.find_one({'_id': ObjectId(request._id)})
            if not product:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such product!")
                return inventory_pb2.ID()
            
            req_data = {
                'name': request.request_body.name,
                'category': request.request_body.category.name,
                'price': request.request_body.price,
                'quanitiy': request.request_body.quanitiy
            }

            updated_product = product_collection.update_one({'_id': ObjectId(request._id)}, {'$set': req_data})
            if updated_product.modified_count == 0:
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)
                context.set_details("Product not updated!")
                return inventory_pb2.ID()
            
            return inventory_pb2.ID(_id=request._id)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ID()
        

    def DeleteProduct(self, request, context):
        try:
            category = product_collection.find_one({'_id': ObjectId(request._id)})
            if not category:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such product!")
                return inventory_pb2.Empty()
  
            deleted_product = product_collection.delete_one({'_id': ObjectId(request._id)})
            if deleted_product.deleted_count == 0:
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)
                context.set_details("Product not deleted!")
                return inventory_pb2.Empty()
            
            return inventory_pb2.Empty()
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.Empty() 
        

    def SearchProduct(self, request, context):
        try:
            query = request.query.lower()
            products = list(product_collection.find({'name': {'$regex': f'.*{query}.*', '$options': 'i'}}))
            if not products:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No products found!")
                return inventory_pb2.ProductResponseList()

            products = [{k: str(v) if k == "_id" else v for k, v in product.items()} for product in products]
            
            return inventory_pb2.ProductResponseList(products=products)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ProductResponseList() 