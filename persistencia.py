import json
import os


class PersistenceJSON:
    def __init__(self, products_file="products.json", orders_file="orders.json"):
        self.products_file = products_file
        self.orders_file = orders_file
    
    def save_products(self, bst_products):
        products_list = bst_products.to_list()
        
        with open(self.products_file, 'w', encoding='utf-8') as f:
            json.dump(products_list, f, ensure_ascii=False, indent=2)
        
        print(f"{len(products_list)} products saved to {self.products_file}")
    
    def load_products(self, bst_products):
        if not os.path.exists(self.products_file):
            print(f"{self.products_file} does not exist. Creating new...")
            return
        
        with open(self.products_file, 'r', encoding='utf-8') as f:
            products_list = json.load(f)
        
        bst_products.from_list(products_list)
        print(f"{len(products_list)} products loaded from {self.products_file}")
    
    def save_orders(self, linked_list_orders):
        orders_list = linked_list_orders.to_list()
        
        with open(self.orders_file, 'w', encoding='utf-8') as f:
            json.dump(orders_list, f, ensure_ascii=False, indent=2)
        
        print(f"{len(orders_list)} orders saved to {self.orders_file}")
    
    def load_orders(self, linked_list_orders, bst_products):
        if not os.path.exists(self.orders_file):
            print(f"{self.orders_file} does not exist. Creating new...")
            return
        
        with open(self.orders_file, 'r', encoding='utf-8') as f:
            orders_list = json.load(f)
        
        linked_list_orders.from_list(orders_list, bst_products)
        print(f"{len(orders_list)} orders loaded from {self.orders_file}")