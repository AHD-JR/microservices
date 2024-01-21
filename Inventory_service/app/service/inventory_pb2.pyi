from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ID(_message.Message):
    __slots__ = ("_id",)
    _ID_FIELD_NUMBER: _ClassVar[int]
    _id: str
    def __init__(self, _id: _Optional[str] = ...) -> None: ...

class CategoryRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CategoryResponse(_message.Message):
    __slots__ = ("_id", "name")
    _ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    _id: str
    name: str
    def __init__(self, _id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CategoryResponseList(_message.Message):
    __slots__ = ("categories",)
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[CategoryResponse]
    def __init__(self, categories: _Optional[_Iterable[_Union[CategoryResponse, _Mapping]]] = ...) -> None: ...

class PaginationRequest(_message.Message):
    __slots__ = ("page", "limit")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    page: int
    limit: int
    def __init__(self, page: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class UpdateCategoryRequest(_message.Message):
    __slots__ = ("_id", "request_body")
    _ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    _id: str
    request_body: CategoryRequest
    def __init__(self, _id: _Optional[str] = ..., request_body: _Optional[_Union[CategoryRequest, _Mapping]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class ProductRequest(_message.Message):
    __slots__ = ("name", "category", "price", "quanitiy")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANITIY_FIELD_NUMBER: _ClassVar[int]
    name: str
    category: CategoryRequest
    price: float
    quanitiy: int
    def __init__(self, name: _Optional[str] = ..., category: _Optional[_Union[CategoryRequest, _Mapping]] = ..., price: _Optional[float] = ..., quanitiy: _Optional[int] = ...) -> None: ...

class ProductResponse(_message.Message):
    __slots__ = ("_id", "name", "category", "price", "quanitiy")
    _ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANITIY_FIELD_NUMBER: _ClassVar[int]
    _id: str
    name: str
    category: str
    price: float
    quanitiy: int
    def __init__(self, _id: _Optional[str] = ..., name: _Optional[str] = ..., category: _Optional[str] = ..., price: _Optional[float] = ..., quanitiy: _Optional[int] = ...) -> None: ...

class ProductResponseList(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[ProductResponse]
    def __init__(self, products: _Optional[_Iterable[_Union[ProductResponse, _Mapping]]] = ...) -> None: ...

class UpdateProductRequest(_message.Message):
    __slots__ = ("_id", "request_body")
    _ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_FIELD_NUMBER: _ClassVar[int]
    _id: str
    request_body: ProductRequest
    def __init__(self, _id: _Optional[str] = ..., request_body: _Optional[_Union[ProductRequest, _Mapping]] = ...) -> None: ...

class Address(_message.Message):
    __slots__ = ("street", "city", "state", "country", "zip_code")
    STREET_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    street: str
    city: str
    state: str
    country: str
    zip_code: str
    def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., zip_code: _Optional[str] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = ("products", "shipping_address", "created_at", "created_by", "total_price", "order_status")
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    products: ProductResponseList
    shipping_address: Address
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    total_price: float
    order_status: str
    def __init__(self, products: _Optional[_Union[ProductResponseList, _Mapping]] = ..., shipping_address: _Optional[_Union[Address, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., total_price: _Optional[float] = ..., order_status: _Optional[str] = ...) -> None: ...

class OrderResponse(_message.Message):
    __slots__ = ("_id", "products", "shipping_address", "created_at", "created_by", "order_date", "total_price", "order_status")
    _ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    ORDER_DATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    _id: str
    products: ProductResponseList
    shipping_address: Address
    created_at: str
    created_by: str
    order_date: _timestamp_pb2.Timestamp
    total_price: float
    order_status: str
    def __init__(self, _id: _Optional[str] = ..., products: _Optional[_Union[ProductResponseList, _Mapping]] = ..., shipping_address: _Optional[_Union[Address, _Mapping]] = ..., created_at: _Optional[str] = ..., created_by: _Optional[str] = ..., order_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total_price: _Optional[float] = ..., order_status: _Optional[str] = ...) -> None: ...

class OrderResponseList(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderResponse]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderResponse, _Mapping]]] = ...) -> None: ...

class GetOrdersByUserRequest(_message.Message):
    __slots__ = ("username", "page", "limit")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    username: str
    page: int
    limit: int
    def __init__(self, username: _Optional[str] = ..., page: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...
