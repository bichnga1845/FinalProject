from libs.JsonFileFactory import JsonFileFactory


class Order:
    FILE_PATH = "../dataset/orders.json"

    def __init__(self, order_id, reader_id, book_id, quantity, borrow_date=None, return_date=None, status="Not Returned", items=[]):
        self.order_id = order_id
        self.reader_id=reader_id
        self.book_id=book_id
        self.quantity = quantity
        self.status = status
        self.borrow_date = borrow_date
        self.return_date = return_date

        self.items = items

    @staticmethod
    def get_all_orders():
        return JsonFileFactory.read_data(Order.FILE_PATH, Order)
