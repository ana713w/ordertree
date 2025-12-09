
class ProductNode:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id 
        self.name = name 
        self.price = price
        self.stock = stock
        self.left = None  
        self.right = None
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }


class BST_Products:
    def __init__(self):
        self.root = None
    
    def insert(self, product_id, name, price, stock):
        if self.root is None:
            self.root = ProductNode(product_id, name, price, stock)
        else:
            self._insert_recursive(self.root, product_id, name, price, stock)
    
    def _insert_recursive(self, node, product_id, name, price, stock):
        if product_id < node.id:
            if node.left is None:
                node.left = ProductNode(product_id, name, price, stock)
            else:
                self._insert_recursive(node.left, product_id, name, price, stock)
        
        elif product_id > node.id:
            if node.right is None:
                node.right = ProductNode(product_id, name, price, stock)
            else:
                self._insert_recursive(node.right, product_id, name, price, stock)
    
    def search(self, product_id):
        return self._search_recursive(self.root, product_id)
    
    def _search_recursive(self, node, product_id):
        if node is None:
            return None
        
        if product_id == node.id:
            return node
        
        elif product_id < node.id:
            return self._search_recursive(node.left, product_id)
        
        else:
            return self._search_recursive(node.right, product_id)
    
    def list_all(self):
        products = []
        self._in_order(self.root, products)
        return products
    
    def _in_order(self, node, products):
        if node:
            self._in_order(node.left, products)
            products.append(node.to_dict())
            self._in_order(node.right, products)
    
    def to_list(self):
        return self.list_all()
    
    def from_list(self, products_list):
        self.root = None
        for prod in products_list:
            self.insert(prod['id'], prod['name'], prod['price'], prod['stock'])