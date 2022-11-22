# Assemble
# Act
# Assert

from MiniProject4 import view_list, adding_to_list, renaming_list_via_index, remove_entry, read_file, orders_menu_view,new_customer_order,update_status
from unittest.mock import patch

# 1. ViewS
def test_viewing_product_list_with_index():
    # Assemble
    a_list_of_dicts = [{"name":"Numan","surname":"Mahmood"},{"name":"Is","surname":"Testing"}]
    # Act
    actual = view_list(a_list_of_dicts,"name","surname")
    expected = '0| Numan: Mahmood\n1| Is: Testing\n'
    # Assert
    assert actual == expected

# 2. Add
def test_add_product_to_list():
    # Assemble
    product_name = "Cola"
    product_cost = "0.6"
    products_list = []

    # Act
    actual = adding_to_list(product_name,product_cost,products_list,float,"Name","Cost")
    expected = [{"Name": "Cola", "Cost": 0.6}]
    # Assert
    assert actual == expected

# 3. Renaming
# # Test Case: 2 inputs
@patch('builtins.input',side_effect=['Chocolate',0.3])
def test_renaming_list_items(mock_input):
    # Assemble
    a_list_of_dicts = [{"Name":"Muffin","Cost": 1.2,},{"Name": "Croissant","Cost": 0.9,}]
    index = 0
    # Act
    actual = renaming_list_via_index(a_list_of_dicts,index)
    expected = [{"Name":"Chocolate","Cost": 0.3,},{"Name": "Croissant","Cost": 0.9,}]
    # Assert
    assert actual == expected

# # Test Case: 1 input
@patch('builtins.input',side_effect=['',1.3])
def test_renaming_list_items_with_one_empty_input(mock_input):
    # Assemble
    a_list_of_dicts = [{"Name":"Muffin","Cost": 1.2},{"Name": "Croissant","Cost": 0.9}]
    index = 0
    # Act
    actual = renaming_list_via_index(a_list_of_dicts,index)
    expected = [{"Name":"Muffin","Cost": 1.3},{"Name": "Croissant","Cost": 0.9}]
    # Assert
    assert actual == expected

# # Test Case: 0 input
@patch('builtins.input',side_effect=['',''])
def test_renaming_list_items_with_two_empty_inputs(mock_input):
    # Assemble
    a_list_of_dicts = [{"Name":"Muffin","Cost": 1.2},{"Name": "Croissant","Cost": 0.9}]
    index = 0
    # Act
    actual = renaming_list_via_index(a_list_of_dicts,index)
    expected = [{"Name":"Muffin","Cost": 1.2},{"Name": "Croissant","Cost": 0.9}]
    # Assert
    assert actual == expected
    assert mock_input.call_count == 2 
    
# 4. Remove
@patch('builtins.print')
@patch('builtins.input', side_effect = "3")
def test_removing_entry_from_list(mock_print,mock_input):
    # Assemble
    title_of_menu = 'Person'
    a_list_of_dicts = [
    {"Name":"Sal","Number":"0738261362"},
    {"Name":"Joe","Number":"07931729312"},
    {"Name":"Murr","Number":"0797398213"},
    {"Name":"Q","Number":"08793982173"}]
    
    # Act
    actual = remove_entry(title_of_menu,a_list_of_dicts)
    expected = [
    {"Name":"Sal","Number":"0738261362"},
    {"Name":"Joe","Number":"07931729312"},
    {"Name":"Murr","Number":"0797398213"}]

    # Assert
    assert actual == expected

# Test case: 2 
@patch('builtins.input', side_effect = "3")
@patch('builtins.print')
def test_print_removing_entry_from_list(mock_print,mock_input):
    # Assemble
    title_of_menu = 'Person'
    a_list_of_dicts = [
    {"Name":"Sal","Number":"0738261362"},
    {"Name":"Joe","Number":"07931729312"},
    {"Name":"Murr","Number":"0797398213"},
    {"Name":"Q","Number":"08793982173"}]
    # Act
    remove_entry(title_of_menu,a_list_of_dicts)
    # Assert
    mock_print.assert_called_with('\nPerson no. 3 has been removed.')
    
# 5. Read  CSV
def test_read_from_csv():
    # Assemble
    empty_list_of_dicts = []
    a_list_of_dicts = [{"test1":"a","test2":"b"},{"test1":"c","test2":"d"}]
    # Act
    read_file('test',empty_list_of_dicts)
    expected = a_list_of_dicts
    # Assert
    assert empty_list_of_dicts == expected

# 6. Order Menu View
def test_orders_menu_view():
    # Assemble
    a_list_of_dicts = [{"customer_name":"abc","customer_address":"abc","customer_phone":"abc","courier":"abc","status":"abc","items":"abc"}]
    # Act
    actual = orders_menu_view(a_list_of_dicts)
    expected = '''
0.
______________________________________________________________________
Customer Name: abc
Customer Address: abc
Customer phonenumber: abc
Courier: abc
Order Status: abc
Items: abc
______________________________________________________________________'''
    # Assert
    assert actual == expected

# 7. New order
@patch('builtins.input', side_effect=['a','new','customer','1','','3'])
def test_new_order(mock_input):
    # Assemble
    an_order_list = []
    
    # Act
    actual = new_customer_order(an_order_list)
    expected = [{
    "customer_name": "a", 
    "customer_address": "new",
    "customer_phone": "customer",
    "courier": 3,
    "status": "Preparing",
    "items": "1"
    }]

    # Assert
    assert actual == expected

# 8. Update status
@patch('builtins.input', side_effect = ['0','3'])
def test_updating_order_status(mock_input):
    # Assemble
    a_list = [{
    "customer_name": "a", 
    "customer_address": "new",
    "customer_phone": "customer",
    "courier": 3,
    "status": "Preparing",
    "items": "1"
    }]
    # Act
    actual = update_status(a_list,('Preparing','Ready for collection','Out for delivery','Complete'))
    expected = [{
    "customer_name": "a", 
    "customer_address": "new",
    "customer_phone": "customer",
    "courier": 3,
    "status": "Complete",
    "items": "1"
    }]
    # Assert
    assert actual == expected