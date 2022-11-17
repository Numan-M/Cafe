import csv

def view_list(viewed_list,*keys):
    print('')
    i = 0
    for items in viewed_list:
        print (f'{i}| {items[keys[0]]}: {items[keys[1]]}')
        i += 1
    return 
                
def product_menu(menu_name,some_list,*keys):
    product_menu_input = int(input(f'\n--- {menu_name} Menu ---\n\
0. Return\n\
1. View {menu_name}\'s menu\n\
2. Add a {menu_name}\n\
3. Rename a {menu_name}\n\
4. Remove a {menu_name}\n\
>> ')) 

    # # 0. Return
    if product_menu_input == 0:

        return

    # # 1. View
    if product_menu_input == 1:
        view_list(some_list,*keys)

        return product_menu(f'{menu_name}', some_list,*keys) 

    # # 2. Add
    if product_menu_input == 2:
        new_entry = input(f'\nEnter {menu_name} {keys[0]}\n>> ')
        new_entry_price = input(f'\nEnter {menu_name} {keys[1]}\n>> ')

        if some_list == products_list:
            some_list.append({f"{keys[0]}": f"{new_entry.title()}",
                            f"{keys[1]}": f"{float(new_entry_price)}"})
            print(f'\n{new_entry.title()} has been added. {keys[1]} has been set to {float(new_entry_price)}.')

        elif some_list == couriers_list:
            some_list.append({f"{keys[0]}": f"{new_entry.title()}",
                            f"{keys[1]}": f"{new_entry_price}"})
            print(f'\n{new_entry.title()} has been added. {keys[1]} has been set to {new_entry_price}.')


        return product_menu(f'{menu_name}', some_list,*keys) 

    # # 3. Rename
    if product_menu_input == 3:
        view_list(some_list,*keys)
        rename_index = int(input(f'\nSelect {menu_name} Index:\n>> '))
        some_list_copy = some_list[rename_index].copy()

        for key,value in some_list[rename_index].items():
            value = input(f'{key}: ' )
            if value == '':
                value = some_list_copy[f'{key}']
            some_list[rename_index].update({key: value})

        return product_menu(f'{menu_name}', some_list,*keys)   

    # # 4. Remove
    if product_menu_input == 4:
        view_list(some_list,*keys)
        removal_index = int(input(f'Which {menu_name} would you like to remove?\n>> '))
        print(f'\n{menu_name} no. {removal_index} has been removed.')
        some_list.remove(some_list[removal_index])

        return product_menu(f'{menu_name}', some_list,*keys)

    else:
        print('\nInvalid option.')

        return product_menu(f'{menu_name}', some_list,*keys)

def orders_menu_view(orders):
    i = 0
    for _ in orders:
        print(f'''
{i}.
______________________________________________________________________
Customer Name: {orders[i]["customer_name"]}
Customer Address: {orders[i]["customer_address"]}
Customer phonenumber: {orders[i]["customer_phone"]}
Order Status: {orders[i]["status"]}
______________________________________________________________________'''
)
        i += 1

def orders_menu(orders,status):
    orders_menu_input = int(input(f'\n--- Orders Menu ---\n\
0. Return\n\
1. View Orders\n\
2. New Order\n\
3. Update Order Status\n\
4. Update Existing Order\n\
5. Cancel Order\n\
>> ')) 
    # 0. Return
    if orders_menu_input == 0:
        return
    # 1. View
    if orders_menu_input == 1:
        orders_menu_view(orders)
        return orders_menu(orders,status)

    # 2. New order
    if orders_menu_input == 2:
        customer_name = input('Enter your name\n>>')
        customer_address = input('Enter your address\n>>')
        customer_number = input('Enter your number\n>>')
        customer_order_status = 'Preparing'

        new_order = {
        "customer_name":customer_name, 
        "customer_address": customer_address,
        "customer_phone": customer_number,
        "status": customer_order_status
        }

        orders.append(new_order)
        return orders_menu(orders,status)

        
    # 3. Update status
    if orders_menu_input == 3:
        orders_menu_view(orders)

        update_order_status_index = int(input('\nEnter order number:\n>> '))
        print('\nWhat would you like to update the order status to?\n')
        for option in enumerate(status):
            print(f'{option[0]}. {option[1]}')

        update_order_status = int(input('\n>> '))
        print(f'\nOrder status: \'{orders[update_order_status_index]["status"]}\' has been updated to \'{status[update_order_status]}\'.')
        orders[update_order_status_index]['status'] = status[update_order_status]

        return orders_menu(orders,status)
    # 4. Update Order
    if orders_menu_input == 4:
        orders_menu_view(orders)
        update_order_index = int(input('\nEnter order number:\n>> '))
        orders_copy = orders[update_order_index].copy()

        for key,value in orders[update_order_index].items():
            value = input(f'{key}: ' )
            if value == '':
                value = orders_copy[f'{key}']
            orders[update_order_index].update({key: value})

        return orders_menu(orders,status)
            
            

    # 5. Cancel
    if orders_menu_input == 5:
        orders_menu_view(orders)
        cancel_order_index = int(input('Which order would you like to cancel?\n>> '))
        print(f'\nOrder no {cancel_order_index} has been cancelled.')
        orders.remove(orders[cancel_order_index])

        return orders_menu(orders,status)

    else:
        print('Invalid option.')
        
        return orders_menu(orders,status)

def main_menu():
    main_menu_input = int(input('\n--- Main Menu ---\n\
0. Exit\n\
1. Product Menu\n\
2. Order Menu\n\
3. Courier Menu \n\
>> '))
    return main_menu_input

order_status = ('Preparing','Ready for collection','Out for delivery','Complete')

products_list = []
couriers_list = []
orders_list = []

def read_file(filename,loading_list):
        with open (f'{filename}.csv','r' ) as f:
                reader=csv.DictReader(f,delimiter=',',skipinitialspace = True)
                for row in reader:
                        loading_list.append(row)
        return

def write_file(filename,loading_list):
        with open(f'{filename}.csv', 'w', newline='') as f:
                keys = loading_list[0].keys()
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerows(loading_list)
        return

read_file('products',products_list)
read_file('couriers',couriers_list)
read_file('orders',orders_list)

while True:
    main_input = main_menu()
    if main_input == 0:
        write_file('products',products_list)
        write_file('couriers',couriers_list)
        write_file('orders',orders_list)         
        print('\nGoodbye!')
        break
    elif main_input == 1:
        product_menu('Product',products_list,"Name","Cost")
    elif main_input == 2:
        orders_menu(orders_list,order_status)
    elif main_input == 3:
        product_menu('Courier',couriers_list, "Name","Number")
    elif main_input > 3 or main_input < 0:
        print('\nInvalid input. Please try again.')


