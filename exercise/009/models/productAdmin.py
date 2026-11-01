from models.productOut import ProductOut


class ProductAdmin(ProductOut):
    cost: float
    supplier: str
    stock: int