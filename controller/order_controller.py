from libs.JsonFileFactory import JsonFileFactory
from models.Order import Order
from models.User import User


class OrderController:
    orders_file = "../dataset/orders.json"

    @staticmethod
    def get_all_orders():
        orders = JsonFileFactory.read_data(OrderController.orders_file,Order)
        return orders
    @staticmethod
    def generate_order_id():
        orders = JsonFileFactory.read_data(OrderController.orders_file,Order)
        order_ids = [int(order.order_id) for order in orders if isinstance(order, Order)]
        return max(order_ids) + 1 if order_ids else 1001

    @staticmethod
    def get_order_by_id(order_id):
        orders = OrderController.get_all_orders()
        for order in orders:
            if str(order.order_id) == order_id:
                return order
        return None


    @staticmethod
    def delete_order(order_id):
        orders = OrderController.get_all_orders()

        for order in orders:
            if order.order_id == order_id:
                orders.remove(order)
                JsonFileFactory.write_data(orders, OrderController.orders_file)
                return True, f"Delete #{order_id} successfully!"

        return False, "Can't find order!"


