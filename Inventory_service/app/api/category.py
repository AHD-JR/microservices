from fastapi import APIRouter
from app.service.server import CategoryServiceImplementation, serve, inventory_pb2
from app.models.category import Category
from app.utils.response import response

router = APIRouter(
    prefix="/api/categories",
    tags=['Category']
)

category_service = CategoryServiceImplementation()

@router.post('/')
def create_category(req: Category):
    try:
        grpc_request = inventory_pb2.CategoryRequest(name=req.name)
        category_id = category_service.CreateCategory(grpc_request, None)

        return str(category_id._idid)
    
    except Exception as e:
        return response(status_code=500, message=str(e))