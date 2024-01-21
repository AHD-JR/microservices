import grpc
import logging
from concurrent import futures
import inventory_pb2_grpc
from category import CategoryServiceImplementation 
from product import ProductServiceImplementation


def serve():
    port = "243243"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_CategoryServiceServicer_to_server(CategoryServiceImplementation(), server)
    inventory_pb2_grpc.add_ProductServiceServicer_to_server(ProductServiceImplementation(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print(f"Inventory server listening on port {port}...")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()


