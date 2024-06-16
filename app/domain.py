from pydantic import BaseModel


class Order(BaseModel):
    id: int
    status: str = "pending"
    client_ip: str


class OrderRequest(BaseModel):
    order_id: int
