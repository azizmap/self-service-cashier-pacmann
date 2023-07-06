from cashier_self_service import Transaction
from os import system, name
from time import sleep

def clear():
    """
    this function helps to clear the interface of main function.
    
    """

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    """
    a function to run self service cashier, and make a Transaction Instance.
    This main will be the main menu for self service cashier and can help user
    to make a transaction, add, update, delete item and can calculate the amount of
    money for a single transaction.
    """

    print("Welcome to Self-Service Supermarket!")
    print("silahkan pilih menu dibawah ini!")
    transaction = Transaction()
    while True:
        print("="*40)
        print("1. Tambah Item Belanja")
        print("2. Update Nama Item")
        print("3. Update Quantity Item")
        print("4. Update Harga Item")
        print("5. Hapus Item Belanja")
        print("6. Cek Pesanan")
        print("7. Hitung Total Harga Belanja")
        print("8. Reset Transaksi")
        print("9. Keluar")
        print("="*40)
        try:
            menu = int(input("Masukkan Pilihan Menu Anda: "))
            if menu == 1:
                clear()
                item_name = input("Masukkan Nama Item: ")
                item_qty = int(input("Masukkan Quantity Item: "))
                item_price = int(input("Masukkan Harga Item: "))
                transaction.add_item([item_name, item_qty, item_price])
            elif menu == 2:
                clear()
                item_name = input("Masukkan Nama Item: ")
                update_name = input("Masukkan Nama Item yang baru: ")
                transaction.update_item_name(item_name, update_name)
            elif menu == 3:
                clear()
                item_name = input("Masukkan Nama Item: ")
                update_qty = int(input("Masukkan Quantity Item yang baru: "))
                transaction.update_item_qty(item_name, update_qty)
            elif menu == 4:
                clear()
                item_name = input("Masukkan Nama Item: ")
                update_price = int(input("Masukkan Harga Item yang baru: "))
                transaction.update_item_price(item_name, update_price)
            elif menu == 5:
                clear()
                item_name = input("Masukkan Nama Item yang ingin dihapus: ")
                transaction.delete_item(item_name)
            elif menu == 6:
                clear()
                transaction.check_order()
            elif menu == 7:
                clear()
                transaction.total_price()
            elif menu == 8:
                clear()
                transaction.reset_transaction()
                print("semua item berhasil dihapus!")
            elif menu == 9:
                break
            else:
                clear()
                print("Pilihan yang anda masukkan tidak valid, silahkan coba kembali!")
        except ValueError:
            clear()
            print("Pilihan yang anda masukkan tidak valid, silahkan coba kembali!")
        except Exception as e:
            clear()
            print(e)

if __name__ == "__main__":
    main()