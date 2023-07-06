from tabulate import tabulate

class Transaction:
    """
    Class Transaction is an instance/class that made to assist self service for
    buyer such as add, update and delete item.

    This Class will contains Buyer's item information like Item name, its
    quantity and its price.

    Transaction Attribute:
    - order_item_list: a dictionary that will store all of item's that buyer's
    will purchase.

    Transaction Method:
    - add_item: adding new item to order_item_list, or if the item already
    exist, it will sum with the new quantity
    - update_item_name: update an item name in order_item_list if exist
    - update_item_quantity: update an item quantity in order_item_list if exist
    - update_item_price: update an item price in order_item_list if exist
    - delete_item: delete an item in order_item_list if exist
    - reset transaction: empty the order_item_list
    - check_order: print all item in order_item_list
    - total_price: calculate & return total price of all item in order_item_list
    and return total price with discount if certain condition is achieved.

    """
    def __init__(self):
        """
        initialization of Transaction with empty dictionary order_item_list
        """
        self.order_item_list = {}

    def add_item(self, item):
        """
        adding new item to order_item_list, or if the item already exist, it
        will sum with the new quantity

        Parameter:
        - self: instance of Transaction
        - item (list): list contains name, quantity and price

        Output: -
        """
        try:
            name, qty, price = item
            if name in self.order_item_list:
                self.order_item_list[name][0] += qty
            else:
                self.order_item_list[name] = [qty, price]
            print(f"Item {name} berhasil ditambahkan")
        except ValueError:
            print("Mohon masukkan nama, jumlah, dan harga item dengan benar!")

    def update_item_name(self, item_name, update_item_name):
        """
        update an item name in order_item_list if exist

        Parameter:
        - self: instance of Transaction
        - item_name (string): previous item name
        - update_item_name (string): updated item name

        Output: -
        """
        try:
            self.order_item_list[update_item_name] = self.order_item_list.pop(item_name)
            print(f"item {update_item_name} berhasil di-update")
        except KeyError:
            print(f"Item {item_name} tidak ditemukan!")

    def update_item_qty(self, item_name, update_item_qty):
        """
        update an item quantity in order_item_list if exist

        Parameter:
        - self: instance of Transaction
        - item_name (string): item name that quantity will be update
        - update_item_qty (int): updated item quantity

        Output: -
        """
        try:
            self.order_item_list[item_name][0] = update_item_qty
            print(f"item {item_name} berhasil di-update")
        except KeyError:
            print(f"Item {item_name} tidak ditemukan!")

    def update_item_price(self, item_name, update_item_price):
        """
        update an item price in order_item_list if exist

        Parameter:
        - self: instance of Transaction
        - item_name (string): item name that price will be update
        - update_item_price (int): updated item price

        Output: -
        """
        try:
            self.order_item_list[item_name][1] = update_item_price
            print(f"item {item_name} berhasil di-update")
        except KeyError:
            print(f"Item {item_name} tidak ditemukan!")

    def delete_item(self, item_name):
        """
        delete an item in order_item_list if exist

        Parameter:
        - self: instance of Transaction
        - item_name (string): item name that will be deleted

        Output: -
        """
        try:
            self.order_item_list.pop(item_name)
            print(f"item {item_name} berhasil di-hapus")
        except KeyError:
            print(f"Item {item_name} tidak ditemukan!")

    def reset_transaction(self):
        """
        delete all of item in order_item_list

        Parameter:
        - self: instance of Transaction

        Output:
        - emptied order_item_list
        """
        self.order_item_list = {}

    def check_order(self):
        """
        print all of items inside order_item_list and the total_price per item

        Parameter:
        - self: instance of Transaction

        Output:
        - total_prices (int): total price from all item in order_item_list
        without discount
        """
        if self.order_item_list:
            list_item = []
            total_prices = 0
            headers = ["No.", "Item", "Qty", "Price/Item", "Total Price"]

            for idx, (name, item_info) in enumerate(self.order_item_list.items(), start=1):
                qty, price = item_info
                total_price = qty * price
                list_item.append([idx, name, qty, price, total_price])
                total_prices += total_price
            print(tabulate(list_item, headers=headers, tablefmt='grid'))

            # print(f"Total Price for all Items: Rp{total_prices:,},-")
            return total_prices
        else:
            print("List Item masih kosong!")

    def total_price(self):
        """
        calculate & return total price of all item in order_item_list
        and return total price with discount if certain condition is achieved.

        Parameter:
        - self: instance of Transaction

        Output:
        - total_prices (int): total price from all item in order_item_list
        with discount.
        """
        total_prices = self.check_order()
        disc = 0
        if total_prices > 500000:
            disc = 0.1
        elif total_prices > 300000:
            disc = 0.08
        elif total_prices > 200000:
            disc = 0.05

        print(f"Total Price for all Items: Rp{total_prices - total_prices * disc:,}-")