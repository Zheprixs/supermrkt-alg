import time

def signup(username, pwd):
    print('Welcome to our company!')


timestamp = time.time()
current_date = time.ctime(timestamp)


def signin(username, pwd, current_date):
    user = input("Enter your username")
    while user != username or user != owneruser:
        print('Our system cannot recognize it!')
        user = input("Enter your username")

    
    pw = input('Enter your password')
    for i in range (4):
        if pw != pwd or pw != ownerpass:
            print('Your password does not match!')
            pw = input('Enter your password')
        else:
            print('Welcome', user or owneruser, 'time login: ', current_date)
        break


Mulai = str(input(
    'input the number! '
    '1. New employee sign up '
    '2. Cashier. 0. off'))

owneruser = 'Owner'
ownerpass = 'owner234'
username = ''
pwd = ''
daftar = 0
while Mulai != '0':
    if Mulai == '1':
        username = input('Enter your name!')
        pwd = input('Make your password')
        signup(username, pwd )
        daftar +=1
    
    
    elif Mulai == '2':
        user = input("Enter your username")
        while user != username and user != owneruser:
            print('Our system cannot recognize it!')
            user = input("Enter your username")

        
        pw = input('Enter your password')
        for i in range (4):
            if pw != pwd and pw != ownerpass:
                print('Your password does not match!')
                pw = input('Enter your password')
            else:
                print('Welcome', user or owneruser, 'time login: ', current_date)
            break
        barang=[]
        print('1. bar soap')
        print('2. liquid soap')
        print('3. deodorant')
        print('4. instant noodles')
        print('5. snack')
        kasir = input("Enter the number of things you want to buy! type 'off' to stop ")
        deodorant = 20000
        instant_noodles = 3500
        barsoap = 5000
        liquidsoap = 30000
        snack = 15000
        water = 3000
        total1 = 0
        total2 = 0
        total3 = 0
        total4 = 0
        total5 = 0
        while kasir != 'off':
            if kasir == '1':
                jumlah1 = int(input('Input the amount of things they want to buy!'))
                total1 = barsoap*jumlah1
                bills1 ='Barsoap  ' + str(jumlah1) + '  ' + str(total1)
                print('You buy a barsoap x', jumlah1)
                barang.append(bills1)

            elif kasir == '2':
                jumlah2 = int(input('Input the amount of things they want to buy!'))
                total2 = liquidsoap*jumlah2
                bills2 ='Liquidsoap  ' + str(jumlah2) + '  ' + str(total2)
                barang.append(bills2)
                print('You buy a liquidsoap x', jumlah2)
            elif kasir == '3':
                jumlah3 = int(input('Input the amount of things they want to buy!'))
                total3 = deodorant*jumlah3
                bills3 ='Deodorant  ' + str(jumlah3) + '  ' + str(total3)
                barang.append(bills3)
                print('You buy a deodorant x', jumlah3)
            elif kasir == '4':
                jumlah4 = int(input('Input the amount of things they want to buy!'))
                total4 = instant_noodles*jumlah4
                bills4 ='Instant Noodles  ' + str(jumlah4) + '  ' + str(total4)
                barang.append(bills4)
                print('You buy an instant noodles x', jumlah4)

            elif kasir == '5':
                jumlah5 = int(input('Input the amount of things they want to buy!'))
                total5 = snack*jumlah5
                bills5 ='Snack  ' + str(jumlah5) + '  ' + str(total5)
                barang.append(bills5)
                print('You buy a snack x', jumlah5)
            else:
                print('We doesnt have the product')
            print('1. bar soap')
            print('2. liquid soap')
            print('3. deodorant')
            print('4. instant noodles')
            print('5. snack')
            kasir = input('Enter the number of things you want to buy!')
            total = total1 + total2 + total3 + total4 + total5
        print("\n************** Bill **************")
        print('Date:', current_date)
        print('==================================')
        for i in range (len(barang)):
            print(barang [i])
        print("----------------------------------")
        print('Total:', total)
        print("**********************************")
    
    else:
        print('Invalid code!') 
    Mulai = str(input(
    'input the number! '
    '1. New employee sign up '
    '2. Cashier. 0. Off'))

    
    



















