from pyscript import display # type: ignore


restaurant_name = ' Baked Flower' # String
owner_name = "ADM" # String
year_established = "2024" # String
popular_item_price = 1003 #Integer
has_delivery = False # Boolean
product_names = ['Fried squid', 'Cotton candy', 'Lollipops', 'Cupcakes'] # List
menu_prices = 10.99, 12.99, 8.99, 15.99 # Tuple
business_hours = {'Monday, Saturday'} # dictionary
tax_rate = '0.07' # Float


display (f' {restaurant_name}', target='topheader')
display (f' ~ Established by {owner_name} in {year_established} ~', target='displayer')

display (f' Popular item price: {popular_item_price}', target='information')

chosen_item1 = product_names[1]
chosen_item2 = product_names[2]
chosen_item3 = product_names[3]

display (f' {chosen_item1} for {menu_prices[1]}', target='information')
display (f' {chosen_item2} for {menu_prices[2]}', target='information')
display (f' {chosen_item3} for {menu_prices[3]}', target='information')


display (f' Business Hours: {business_hours}', target='footer')


