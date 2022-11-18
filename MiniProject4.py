import csv

# # 1. View
def view_list(viewed_list,*keys):
    print('')
    i = 0
    for items in viewed_list:
        print (f'{i}| {items[keys[0]]}: {items[keys[1]]}')
        i += 1
    return 

# # 2. Add
def adding_to_list(menu_name,some_list,*keys):
    new_entry = input(f'\nEnter {menu_name} {keys[0]}\n>> ')
    new_entry_input = input(f'\nEnter {menu_name} {keys[1]}\n>> ')

    if some_list == products_list:
        some_list.append({f"{keys[0]}": f"{new_entry.title()}",
                        f"{keys[1]}": f"{float(new_entry_input)}"})
        print(f'\n{new_entry.title()} has been added. {keys[1]} has been set to {float(new_entry_input)}.')

    elif some_list == couriers_list:
        some_list.append({f"{keys[0]}": f"{new_entry.title()}",
                        f"{keys[1]}": f"{new_entry_input}"})
        print(f'\n{new_entry.title()} has been added. {keys[1]} has been set to {new_entry_input}.')
    return

# # 3. Rename
def renaming_list_index(menu_name,some_list,):
    rename_index = int(input(f'\nSelect {menu_name} Index:\n>> '))
    some_list_copy = some_list[rename_index].copy()

    for key,value in some_list[rename_index].items():
        value = input(f'{key}: ' )
        if value == '':
            value = some_list_copy[f'{key}']
        some_list[rename_index].update({key: value})
    return 



# # 4. Remove
def remove_entry(menu_name,some_list):
    removal_index = int(input(f'Which {menu_name} would you like to remove?\n>> '))
    print(f'\n{menu_name} no. {removal_index} has been removed.')
    return some_list.remove(some_list[removal_index])


def second_menu(menu_name,menu_output,some_list,*keys):
    # # 0. Return
    if menu_output == 0:
        return
    # # 1. View
    if menu_output == 1:
        view_list(some_list,*keys)
        return main_menu(main_menu_input)
    # # 2. Add
    if menu_output == 2:
        adding_to_list(f'{menu_name}',some_list,*keys)
        return main_menu(main_menu_input) 
    # # 3. Rename
    if menu_output == 3:
        view_list(some_list,*keys)
        renaming_list_index(f'{menu_name}',some_list)
        return main_menu(main_menu_input) 
    # # 4. Remove
    if menu_output == 4:
        view_list(some_list,*keys)
        remove_entry(f'{menu_name}',some_list)
        return main_menu(main_menu_input) 
    else:
        print('\nInvalid option.')
        return main_menu(main_menu_input) 


# # 1. View
def orders_menu_view(orders):
    i = 0
    for _ in orders:
        print(f'''
{i}.
______________________________________________________________________
Customer Name: {orders[i]["customer_name"]}
Customer Address: {orders[i]["customer_address"]}
Customer phonenumber: {orders[i]["customer_phone"]}
Courier: {orders[i]["courier"]}
Order Status: {orders[i]["status"]}
Items: {orders[i]["items"]}
______________________________________________________________________'''
)
        i += 1
        
# # 2. New Order
def new_customer_order(orders):
    customer_name = input('Enter your name\n>>')
    customer_address = input('Enter your address\n>>')
    customer_number = input('Enter your number\n>>')
    customer_order_status = 'Preparing'

    view_list(products_list,"Name","Cost")
    customer_items = []
    print('\nEnter one product. Leave blank when you have chosen your products.')
    while True:
        customer_items_input=input(">>")
        customer_items.append(customer_items_input)
        if customer_items_input == '':
            customer_items.pop()
            break
    customer_items = ','.join(set(customer_items))
    
    view_list(couriers_list,"Name","Number")
    customer_courier_index = int(input('\nPlease pick from the available couriers.\n>>'))
    
    new_order = {
    "customer_name":customer_name, 
    "customer_address": customer_address,
    "customer_phone": customer_number,
    "courier": customer_courier_index,
    "status": customer_order_status,
    "items": customer_items
    }

    return orders.append(new_order)
# # 3. Update status
def update_status(orders,status):
    update_order_status_index = int(input('\nEnter order number:\n>> '))
    print('\nWhat would you like to update the order status to?\n')
    for option in enumerate(status):
        print(f'{option[0]}. {option[1]}')

    update_order_status = int(input('\n>> '))
    print(f'\nOrder status: \'{orders[update_order_status_index]["status"]}\' has been updated to \'{status[update_order_status]}\'.')
    orders[update_order_status_index]['status'] = status[update_order_status]
    return

def orders_menu(orders):
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
        return orders_menu(orders)

    # 2. New order
    if orders_menu_input == 2:
        new_customer_order(orders)
        return orders_menu(orders)

    # 3. Update status
    if orders_menu_input == 3:
        orders_menu_view(orders)
        update_status(orders,('Preparing','Ready for collection','Out for delivery','Complete'))
        return orders_menu(orders)

    # 4. Update Order
    if orders_menu_input == 4:
        orders_menu_view(orders)
        renaming_list_index('Orders',orders)
        return orders_menu(orders)

    # 5. Cancel
    if orders_menu_input == 5:
        orders_menu_view(orders)
        remove_entry('Order',orders)
        return orders_menu(orders)

    else:
        print('\nInvalid option.')
        return orders_menu(orders)

products_list = []
couriers_list = []
orders_list = []

def menu_input(menu_name):
    menu_output = int(input(f'\n--- {menu_name} Menu ---\n\
0. Return\n\
1. View {menu_name}\'s menu\n\
2. Add a {menu_name}\n\
3. Rename a {menu_name}\n\
4. Remove a {menu_name}\n\
>> '))
    return menu_output
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

def main_menu(main_input):
    if main_input == 0:
        write_file('products',products_list)
        write_file('couriers',couriers_list)
        write_file('orders',orders_list)         
        print('\nGoodbye!')
        exit()
    elif main_input == 1:
        while True:
            product_menu_output = menu_input('Product')
            second_menu('Product', product_menu_output, products_list, "Name", "Cost")
            return
    elif main_input == 2:
        orders_menu(orders_list)
        return
    elif main_input == 3:
        while True:
            courier_menu_output = menu_input('Courier')
            second_menu('Courier', courier_menu_output, couriers_list, "Name", "Number")
            return
    else:
        print('\nInvalid option.')
        return

while True:
    main_menu_input = int(input('\n--- Main Menu ---\n\
0. Exit\n\
1. Product Menu\n\
2. Order Menu\n\
3. Courier Menu \n\
>> '))
    main_menu(main_menu_input)
        