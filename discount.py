def apply_discount(price, discount):

    #1,price is int or float
    if type(price) is not int and type(price) is not float:
        return "The price should be a number"

    #2, discouont is int or float
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    #3, price <= 0
    if price <= 0:
        return "The price should be greater than 0"

    #4, discount <0 or >100
    if discount  < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    #5, final price
    final_price = price * (1 - discount/100)
    return final_price