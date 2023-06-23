print("Enter f for Fahrenheit, c for celcius,r for Rømer,k for kelvin:")
print("To get the temperature one scale to another scales:")

op1 = input("From(f,c,r,k):")
op2 = input("To(f,c,r,k):")

if op1 == 'f' and op2 == 'c':
    temp = float(input("Enter the degree of Fahrenheit:"))
    c = (5*(temp - 32))/9
    print("Degree of celcius is:",c)
elif op1 == 'f' and op2 == 'r':
    temp = float(input("Enter the degree of Fahrenheit:"))
    r = (4*(temp - 32))/9
    print("Degree of Rømer:",r)
elif op1 == 'f' and op2 == 'k':
    temp = float(input("Enter the degree of Fahrenheit:"))
    k = ((5*(temp -32))/9) + 273
    print("Degree of kelvin:",k)
elif op1 == 'c' and op2 == 'k':
    temp = float(input("Enter the degree of celcius:"))
    f = ((9*temp)/5) + 32
    print("Degree of Fahrenhiet is:",f)
elif op1 == 'c' and op2 == 'r':
    temp = float(input("Enter the degree of celcius:"))
    r = (4*temp)/5
    print("Degree of Rømer is:",r)
elif op1 == 'c' and op2 == 'k':
    temp = float(input("Enter the degree of celcius:"))
    k = temp + 273
    print("Degree of kelvin is:",k)
elif op1 == 'r' and op2 == 'c':
    temp  = float(input("Enter the degree of Rømer:"))
    c = (5*temp)/4
    print("Degree of celcius:",c)
elif op1 == 'r' and op2 == 'f':
    temp  = float(input("Enter the degree of Rømer:"))
    f = ((9*temp)/4) + 32
    print("Degree of Fahrenhiet:",f)
elif op1 == 'r' and op2 == 'k':
    temp  = float(input("Enter the degree of Rømer:"))
    k = ((5*temp)/4) +273
    print("Degree of kelvin:",k)
elif op1 == 'k' and op2 == 'c':
    temp = float(input("Enter the degree of kelvin:"))
    c = temp - 273
    print("Degree of celcius:",c)
elif op1 == 'k' and op2 == 'f':
    temp = float(input("Enter the degree of kelvin:"))
    f = ((9*(temp - 273))/5) + 32
    print("Degree of Fahrenheit:",f)
elif op1 == 'k' and op2 == 'r':
    temp = float(input("Enter the degree of kelvin:"))
    r = ((4*(temp - 273))/5)
    print("Degree of Rømer:",r)