
# Self Service Cashier Pacmann
~ This was a final project for Python Class Pacmann.

## Background
Andi merupakan seorang pemilik supermarket di Indonesia dan ingin melakukan perbaikan untuk bisnisnya, yaitu membuat sistem kasir self-service. Agar customer bisa langsung memasukkan item yang dibeli, jumlah item, harga item, dan fitur lainnya.

## Goals
Self Service Cashier memiliki fitur untuk membantu pembeli sebagai berikut:
- Memasukkan item beserta jumlah dan harganya
- Dapat mengubah/menghapus item yang telah ditambahkan
- Mengecek semua pesanan beserta harganya.

## Files
- main.py
    
    a function to run self service cashier, and make a Transaction Instance. This main will be the main menu for self service cashier and can help user to make a transaction, add, update, delete item and can calculate the amount of money for a single transaction.

- cashier_self_service.py

    This file contain Transaction Class, an instance/class that made to assist self service for buyer such as add, update and delete item.

    This Class will contains Buyer's item information like Item name, its quantity and its price.

    Transaction Attribute:
    
    order_item_list: a dictionary that will store all of item's that buyer's will purchase.

## Features
Transaction Method:
- add_item: adding new item to order_item_list, or if the item alreadyexist, it will sum with the new quantity
```python
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
```

- update_item_name: update an item name in order_item_list if exist
```python
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
```

- update_item_quantity: update an item quantity in order_item_list if exist
```python
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
```

- update_item_price: update an item price in order_item_list if exist
```python
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
```

- delete_item: delete an item in order_item_list if exist
```python
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
```

- reset transaction: empty the order_item_list
```python
    def reset_transaction(self):
        """
        delete all of item in order_item_list

        Parameter:
        - self: instance of Transaction

        Output:
        - emptied order_item_list
        """
        self.order_item_list = {}
```

- check_order: print all item in order_item_list
```python
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
```

- total_price: calculate & return total price of all item in order_item_list and return total price with discount if certain condition is achieved.
```python
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
```

## Flow Chart
Memulai program dengan menjalankan file main.py

![flowchart](https://drive.google.com/uc?export=view&id=1sg0y2AdwY5hJgtWDhpyC9MdtX99cARmJ)

![main menu](https://drive.google.com/uc?export=view&id=1pmXAu842SUicKbkGh_ebdxagochK9fZv)

## Test Case
1. Add Item dengan ketentuan:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
![test case 1](https://drive.google.com/uc?export=view&id=1ezC6Z-WZPqvBx3lFIRkXohAc45TeYIP9)

2. Menghapus Item yang bernama Pasta Gigi
![test case 2](https://drive.google.com/uc?export=view&id=1AhrItjHHz0Q1oyeubWNGOuPccoCvqwrs)

3. Reset semua transaksi
![test case 3](https://drive.google.com/uc?export=view&id=1ue4YbLkffh0iltUHZa5IwPvnD7UMakri)

4. Output Total Belanja
![test case 4](https://drive.google.com/uc?export=view&id=1aqEINIiPHMbe7mpJOq_Gw4Dwdyp8toW_)
