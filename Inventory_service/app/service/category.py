import grpc
import inventory_pb2, inventory_pb2_grpc
from app.configs.db import category_collection
from bson import ObjectId


class CategoryServiceImplementation(inventory_pb2_grpc.CategoryServiceServicer):
    def CreateCategory(self, request, context):
        try:
            category = category_collection.find_one({'name': request.name})
            if category:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("Category already exists!")
                return inventory_pb2.ID

            data = {'name': request.name}
            new_category = category_collection.insert_one(data)
            if new_category.inserted_id: 
                return inventory_pb2.ID(_id=str(new_category.inserted_id))
            
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ID()
        

    def GetCategories(self, request, context):
        try:
            categories = list(category_collection.find({}).skip((request.page - 1) * request.limit).limit(request.limit))
            if not categories:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No categories found!")
                return inventory_pb2.CategoryResponseList()

            categories = [{k: str(v) if k == "_id" else v for k, v in category.items()} for category in categories]

            return inventory_pb2.CategoryResponseList(categories=categories)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.CategoryResponseList()
        
    
    def GetCategory(self, request, context):
        try:
            category = category_collection.find_one({'_id': ObjectId(request._id)})
            if not category:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such category!")
                return inventory_pb2.CategoryResponse()
                
            category['_id'] = str(category['_id'])
            return inventory_pb2.CategoryResponse(**category)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.CategoryResponse()
        
    
    def UpdateCategory(self, request, context):
        try:
            print(request)
            category = category_collection.find_one({'_id': ObjectId(request._id)})
            if not category:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such category!")
                return inventory_pb2.ID()

            req_data ={"name": request.request_body.name}
            updated_category = category_collection.update_one({'_id': ObjectId(request._id)}, {'$set': req_data})
            if updated_category.modified_count == 0:
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)
                context.set_details("Category not updated!")
                return inventory_pb2.ID()
            
            return inventory_pb2.ID(_id=request._id)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ID()
        

    def DeleteCategory(self, request, context):
        try:
            category = category_collection.find_one({'_id': ObjectId(request._id)})
            if not category:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such category!")
                return inventory_pb2.Empty()
  
            deleted_category = category_collection.delete_one({'_id': ObjectId(request._id)})
            if deleted_category.deleted_count == 0:
                context.set_code(grpc.StatusCode.UNIMPLEMENTED)
                context.set_details("Category not deleted!")
                return inventory_pb2.Empty()
            
            return inventory_pb2.Empty()
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.Empty() 


    def SearchCategory(self, request, context):
        try:
            query = request.query.lower()
            categories = list(category_collection.find({'name': {'$regex': f'.*{query}.*', '$options': 'i'}}))
            if not categories:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No categories found!")
                return inventory_pb2.CategoryResponseList()

            categories = [{k: str(v) if k == "_id" else v for k, v in category.items()} for category in categories]
            
            return inventory_pb2.CategoryResponseList(categories=categories)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.CategoryResponseList() 