import grpc 
import inventory_pb2, inventory_pb2_grpc
from app.configs.db import order_collection, product_collection
from bson import ObjectId


class OrderServiceImplementation(inventory_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        try:
            address = {
                "street": request.address.street,
                "city": request.address.city,
                "state": request.address.state,
                "country": request.address.country,
                "zip_code": request.address.zip_code
            }

            data = {
                'products': request.products,
                'shipping_address': address,
                'created_at': request.created_at,
                'created_by': request.created_by,
                'order_date': request.order_date,
                'total_price': request.total_price,
                'order_status': request.order_status
            }

            new_order = order_collection.insert_one(data)
            if new_order.inserted_id: 
                return inventory_pb2.ID(_id=str(new_order.inserted_id))
            
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.ID()


    def GetOrdersByUser(self, request, context):
        try:
            orders = list(order_collection.find({'name': request.username}).skip((request.page - 1) * request.limit).limit(request.limit))
            if not orders:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No orders found!")
                return inventory_pb2.OrderResponseList()

            orders = [{k: str(v) if k == "_id" else v for k, v in order.items()} for order in orders]

            return inventory_pb2.OrderResponseList(orders=orders)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.OrderResponseList()
        

    def GetOrder(self, request, context):
        try:
            order = order_collection.find_one({'_id': ObjectId(request._id)})
            if not order:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No such order!")
                return inventory_pb2.OrderResponse()
                
            order['_id'] = str(order['_id'])
            return inventory_pb2.OrderResponse(**order)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.OrderResponse()
    

    def SearchOrder(self, request, context):
        try:
            query = request.query.lower()
            orders = list(product_collection.find({'created_by': query, '$options': 'i'}))
            if not orders:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("No orders found!")
                return inventory_pb2.OrderResponseList()

            orders = [{k: str(v) if k == "_id" else v for k, v in order.items()} for order in orders]
            
            return inventory_pb2.OrderResponseList(orders=orders)
        
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Internal server error: {str(e)}")
            return inventory_pb2.OrderResponseList() 