def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    pounds = kg * 2.205

    print('Weight in pounds: {0}'.format(pounds))

def pounds_kg():
    pounds = float(input('Enter weight in pounds: '))
    kg = pounds / 2.205

    print('Weight in kilograms: {0}'.format(kg))

def cel_fahren():
    celsius = float(input('Enter temperature in celsius: '))
    fahrenheit =  celsius* (9 / 5) + 32
    print('Temperature in fahrenheit: {0}'.format(fahrenheit))

def fahren_cel():
    fahrenheit = float(input('Enter temperature in fahrenheit: '))
    celsius = (fahrenheit - 32)*(5/9)
    print('Temperature in celsius: {0}'.format(celsius))

def  unit_conversion():
    print_menu()
    choice = input('Which conversion would you like to do? ')

    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()

    if choice == '3':
        kg_pounds()
    if choice == '4':
        pounds_kg()

    if choice == '5':
        cel_fahren()
    if choice == '6':
        fahren_cel()

def find_corr_x_y(x,y):

    if len(x) != len(y):
        print('The two sets of numbers are of unequal size')
        return None

    n = len(x)

    # find the sum of the products
    prod = [xi*yi for xi, yi in zip(x, y)]
    sum_prod_x_y = sum(prod)

    # sum of the numbers in x
    sum_x = sum(x)
    # sum of the numbers in y
    sum_y = sum(y)

    # square of the sum of the numbers in x
    squared_sum_x = sum_x**2
    # square of the sum of the numbers in y
    squared_sum_y = sum_y**2

    # find the squares of numbers in x and the
    # sum of the squares
    x_square = [xi**2 for xi in x]
    x_square_sum = sum(x_square)

    # find the squares of numbers in y and the
    # sum of the squares
    y_square = [yi**2 for yi in y]
    y_square_sum = sum(y_square)

    # numerator
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5

    correlation = numerator/denominator

    return correlation
