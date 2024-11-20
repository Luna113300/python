name_of_customer= input ('Enter your name: ')
purchase_amount= int(input("Enter purchase_amount: $"))

if purchase_amount < 100:
    print('NO DISCOUNT')
elif purchase_amount == 100 or purchase_amount ==500:
        print('you have recieved 10% discont')
elif purchase_amount > 500:
      print('you have revieved 20% discount')

      tax= int(input('You are o pay  {Amount-discount+Tax} Thanks'))