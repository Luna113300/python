Amount = float(input('Enter your Amount:'))
original_price =700
Amount_to_pay =800
discount =Amount*20/100
Tax = discount*8/100
if Amount < 100:
    print('Hello.customer! You have no discount')
elif Amount ==100 or Amount <=500:
    print(f'Hello, customer! You have a 10% discount of $ {discount} and a 5% VAT of $ {Tax} . You are to pay ${Amount-discount+Tax} Thanks.')
elif Amount >500:
    print(f'hello, customer! You have a 20% discount of ${discount} and an 8% VAT of ${Tax} . You are to pay ${Amount-discount+Tax} Thanks.')