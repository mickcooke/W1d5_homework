
def get_pet_shop_name(shop):
    name = shop["name"]
    return name

def get_total_cash(shop):
    sum = shop["admin"]["total_cash"]
    return sum

def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount

def get_pets_sold(shop):
    sold = shop["admin"]["pets_sold"]
    return sold

def increase_pets_sold(shop, pet_count):
    shop["admin"]["pets_sold"] += pet_count

def get_stock_count(shop):
    count = len(shop["pets"])
    return count

def get_pets_by_breed(shop, breed):
    pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)

    return pets

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        
    return None

def remove_pet_by_name(shop, pet_name):
     for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    cash = customer["cash"]
    return cash

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    count = len(customer["pets"])
    return count

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    cash = customer["cash"]
    price = new_pet["price"]
    if cash >= price:
        return True
    else:
        return False
    
def sell_pet_to_customer(shop, pet_given, customer):
    # pdb.set_trace()
    for pet in shop["pets"]:
        if pet == pet_given:
            if customer["cash"] >= pet["price"]:
                customer["pets"].append(pet)
                shop["admin"]["pets_sold"] += 1
                customer["cash"] -= pet["price"]
                shop["admin"]["total_cash"] += pet["price"]
              
    return None
    

    







