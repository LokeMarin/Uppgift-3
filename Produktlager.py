import csv
import os
import locale


def load_data(filename):
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products
    
def get_product(products,id):
    if id < 0 and id > len(products):
        return "Produkten hittas inte"
    else:
        return f"{products[id]['name']} {products[id]['desc']}" 
    
def remove_product(products,id):
    temp_product = products[id]["name"]
    products.pop(id)
    return f"Produkt: {id} {temp_product} har tagis bort"

def get_products(products):
    product_list = []
    for product in products:
        product_info = f"{product['id']} {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
products=load_data('db_products.csv')


while True:
    try:
        #os.system('cls')

        print("\n")
        print(get_products(products))
        id = int(input("Produkt id: "))
        
        products = remove_product(products,id)
        break
    except:
        print("Produkt ID finns inte. Använd siffror")
        continue



#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id