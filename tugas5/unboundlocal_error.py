def calculate_area(radius):
    if radius <= 0:
        raise ValueError("radius harus lebih besar dari 0.")
    else:
        try:
            area = 3.14 * radius ** 2
            print("Area lingkaran:", area)
            radius = 0 
        except UnboundLocalError as e:
            print("Error: ", e)
            radius = 0 
        
    return radius

calculate_area(-5) 