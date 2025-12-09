from datetime import datetime


class OrderNode:
    def __init__(self, order_id, client, products):
        self.id = order_id
        self.client = client
        self.products = products 
        self.date = datetime.now().isoformat()
        self.total = 0.0
        self.next = None 
    
    def to_dict(self):
        return {
            "id": self.id,
            "client": self.client,
            "products": self.products,
            "date": self.date,
            "total": self.total
        }


class LinkedList_Orders:
    def __init__(self):
        self.head = None  # First order
        self.counter_id = 1  # Auto-increment ID
    
    def add_order(self, client, products, bst_products):
        new_order = OrderNode(self.counter_id, client, products)
        
        # Calculate order total using BST
        total = 0.0
        for item in products:
            product = bst_products.search(item['product_id'])
            if product:
                total += product.price * item['quantity']
        new_order.total = round(total, 2)
        
        # Insert at the end of the list
        if self.head is None:
            self.head = new_order
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_order
        
        self.counter_id += 1
        return new_order
    
    def search_order(self, order_id):
        current = self.head
        while current:
            if current.id == order_id:
                return current
            current = current.next
        return None
    
    def update_order(self, order_id, new_products, bst_products):
        order = self.search_order(order_id)
        if order:
            order.products = new_products
            
            # Recalculate total
            total = 0.0
            for item in new_products:
                product = bst_products.search(item['product_id'])
                if product:
                    total += product.price * item['quantity']
            order.total = round(total, 2)
            
            return order
        return None
    
    def delete_order(self, order_id):
        if self.head is None:
            return False
        
        # If it's the first node
        if self.head.id == order_id:
            self.head = self.head.next
            return True
        
        # Search for the previous node
        current = self.head
        while current.next:
            if current.next.id == order_id:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def list_all(self):
        orders = []
        current = self.head
        while current:
            orders.append(current.to_dict())
            current = current.next
        return orders
    
    def to_list(self):
        return self.list_all()
    
    def from_list(self, orders_list, bst_products):
        self.head = None
        self.counter_id = 1
        
        for order_data in orders_list:
            new_order = OrderNode(
                order_data['id'],
                order_data['client'],
                order_data['products']
            )
            new_order.date = order_data['date']
            new_order.total = order_data['total']
            
            # Insert
            if self.head is None:
                self.head = new_order
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_order
            
            # Update counter
            if order_data['id'] >= self.counter_id:
                self.counter_id = order_data['id'] + 1