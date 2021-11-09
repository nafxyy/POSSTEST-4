#  Program CRUD #

import os
import secrets as randomday

FoodList = ['Nasi Goreng', 'Mie Goreng', 'Beef Burger', 'Special Omelette', 'Spaghetti', 'Bakso']
FoodPrice = [15000, 16000, 25000, 20000, 22000, 12000]

DrinkList = ['Ice Tea', 'Ice Coffee', 'Milkshake', 'Aqua', 'Orange Juice', 'Soft Drink '] 
DrinkPrice = [5000, 8000, 4000, 9000, 15000, 8000]

FoodCart = []
DrinkCart = []
PriceFood = []
PriceDrink = []


def Poster():
        print("""
|---------------------------------------------------| 
|              Welcome to Our Restaurant            |
| ================================================= | 
| ------------------------------------------------- | 
""")

def ClearMenu():
        os.system('cls' if os.name == 'nt' else 'clear') 

def FoodInput():
        F = 1
        print("\n==========================================")
        print("Silahkan Pesan Makanan sesuai selera anda")
        print("Ketik 'selesai' jika selesai memesan")
        print("==========================================")
        while F > 0:
                FoodOrder = input("Silahkan Pesan Makanan anda = ")
                Order = FoodOrder.title()
                if Order in FoodList:
                        index = FoodList.index(Order) 
                        pricef = FoodPrice[index]
                        FoodCart.append(Order) 
                        PriceFood.append(pricef)
                elif FoodOrder == 'selesai' or FoodOrder == 'Selesai':
                        DrinkMenu()
                        DrinkInput()
                        break
                        

# Input Minuman #
def DrinkInput():
        D = 1
        print("==========================================")
        print("Silahkan Pesan Minuman sesuai selera anda")
        print("Ketik 'selesai' jika selesai memesan")
        print("==========================================")
        while D > 0:
                DrinkOrder = input("Silahkan Pesan Minuman anda = ")
                Order = DrinkOrder.title()
                if Order in DrinkList:
                        index = DrinkList.index(Order) 
                        priced = DrinkPrice[index]
                        DrinkCart.append(Order) 
                        PriceDrink.append(priced)
                elif DrinkOrder == 'selesai' or DrinkOrder == 'Selesai':
                        Buy()
                        break

def Buy():

        TotalFoodPrice = sum(PriceFood)
        TotalDrinkPrice = sum(PriceDrink)

        diskon = 0

# Pemilihan hari beli dilakukan secara acak #
        TotalHari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        HariBeli = randomday.choice(TotalHari)

# Pengaplikasian Diskon Makanan Jika Beli >2 #
        if len(FoodCart) >= 2:
                print("\n================================================================")
                print("Pesanan Makanan Anda : ")
                for FL in FoodCart:
                        print(FL)
                print("Total Harga : Rp.", TotalFoodPrice)
                print("==================================================================")
                print("Anda mendapat diskon sebesar 5% karena memesan 2 menu atau lebih.")
                print("Mohon siapkan uang pas atau kembalian anda menjadi milik kami")
                print("==================================================================")
                diskon+=5

        else:
                print("==================================================================")
                print("Pesanan Makanan Anda : ")
                for FL in FoodCart:
                        print(FL)
                print("Total Harga : Rp.", TotalFoodPrice)  
                print("=========================================")  
                print("Gak diskon ya bang karena pesen 1 doang")
                print("=========================================")


# Pengaplikasian Diskon Minuman Jika Beli >3 #
        if len(DrinkList) >= 3:
                print("===================================================================")
                print("Pesanan Minuman Anda : ")
                for DL in DrinkCart:
                        print(DL)
                print("Total Harga : Rp.", TotalDrinkPrice)
                print("===================================================================")
                print("Anda mendapat diskon sebesar 10% karena memesan 3 menu atau lebih")
                print("Mohon siapkan uang pas atau kembalian anda menjadi milik kami")
                print("===================================================================")
                diskon+=10
        else:
                print("====================================================================")
                print("Pesanan Minuman Anda : ")
                for DL in DrinkCart:
                        print(DL)
                print("Total Harga : Rp.", TotalDrinkPrice)
                print("Gak diskon ya bang karena pesen 1 doang")
                print("====================================================================")

        TotalPrice = TotalDrinkPrice + TotalFoodPrice

# Pengaplikasian Diskon Pembayaran #
        print("\n=======================================")
        print("Silahkan Pilih Metode Pembayaran : ")
        print("1. Uang Cash. \n2. Credit Card. \n3. e-wallet. \n4. Ngutang")
        print("=======================================")

        Metode = input("Saya Memilih = ")
        if Metode == 'E-Wallet' or Metode == 'e-wallet':
                print("=================================================")
                print("Hore Diskon Tambahan berhasil didapat Sebesar 5% ")
                print("=================================================")
                diskon+=5
        elif Metode == 'Ngutang' or Metode == 'ngutang':
                print("Mau dipukul apa gimana?")
                print("==========================")
        else:
                print("================================")
                print("Total Harga : Rp.", TotalPrice)
                print("Gak diskon ya bang")
                print("================================")

        # Pengaplikasian Diskon Hari #
        print("\n==========================================================")
        print("Eits, masih ada diskon tambahan. \nHari ini hari apa hayo")
        if HariBeli == 'Sabtu' or HariBeli == 'Minggu':
                print("Hore, karena hari ini hari", HariBeli, "\nKamu dapat diskon tambahan sebesar 5%")
                diskon+=5
                
        else:
                print("Hore, karena hari ini hari", HariBeli, "Kamu dapat diskon tambahan sebesar 10%")
                diskon+=10

        print("==========================================================")
        print("Total diskon kamu sebesar = "+str(diskon)+"%")
        print('=',TotalPrice,"-",(diskon/100*TotalPrice))

        TotalPrice = TotalPrice - (diskon/100*TotalPrice)
        print("Jadi total harga yang kamu bayar = Rp.", TotalPrice)
        print("==========================================================")

        print("\n=============================================================")
        print("terima kasih telah berbelanja! \nJangan lupa kembali untuk menghamburkan duit anda")
        print("==============================================================")
        ExitProgram()
        

def Main():
        ClearMenu()
        Poster()
        print("=====What You Want to Do?=====")
        print("[1] Show Food Menu")
        print("[2] Show Drink Menu")
        print("[3] Add New Menu")
        print("[4] Change Menu")
        print("[5] Delete Menu")
        print("[0] Quit Program")
        print("=" * 29)

        SelectedOption = input("Choose number> ")
        print("=" * 29)
        if(SelectedOption == "1"):
                FoodMenu()
                FoodInput()
        elif(SelectedOption == "2"):
                DrinkMenu()
                DrinkInput()
        elif(SelectedOption == "3"):
                choose = input("Add Normal or Using Index? = ")
                if choose == 'Normal' or choose == 'normal':
                        AddMenu()
                elif choose == 'Index' or choose == 'index':
                        AddFoodIndex()
                else:
                        print("We cant identify your input")
        elif(SelectedOption == "4"):
                ChangeMenu()
        elif(SelectedOption == "5"):
                DeleteMenu()
        elif(SelectedOption == "0"):
                print("\n======================")
                print("Thanks for your visit \nHave a good day")
                print("======================")
                exit()
        else:
                print("We can't identify your input.")
                Back()

def Back():
        print("\n")
        input("Tekan Enter untuk kembali...")
        Main()

def ExitProgram():
        print("=" * 30)
        print("Thanks for using our programs \nExiting program...")
        print("=" * 30)
        exit

def FoodMenu():
        print("\n============================================")
        print("                Food Menu                   ")
        print("============================================")
        num = 1
        for x in FoodList:
                y = FoodList.index(x)
                print("{}. {} \n= Rp.{}".format(num,x,FoodPrice[y]))
                num+=1
        print('============================================')

def DrinkMenu():
        print("============================================")
        print("                Drink Menu                  ")
        print("============================================")
        num = 1
        for x in DrinkList:
            y = DrinkList.index(x)
            print("{}. {} \n= Rp.{}".format(num,x,DrinkPrice[y]))
            num+=1
        print('===============================')


def AddMenu():
        # Add Menu Makanan di AKhir #
        F = 1
        AddFood = input("Input your new food name = ")
        AddFPrice = input("Input the menu price = ")
        FoodList.append(AddFood)
        FoodPrice.append(AddFPrice)
        F +=1
        choose = input("Do you want to add another food? (Yes/Continue) ")
        if choose == 'Yes' or choose == 'yes':
                AddMenu()
        elif choose == 'Continue' or choose == 'continue':
                choose2 = input("Do you want to add drink normal or using index? = ")
                if choose2 == 'Normal' or 'normal':
                        AddDrink()
                elif choose2 == 'index' or choose2 == 'Index':
                        AddDrinkIndex()
                else:
                        print("=" * 30)
                        print("We cant identify your input. \nPlease Try Again...")
                        print("=" * 30)
                        Main()     

        else:
                print("=" * 30)
                print("We cant identify your input. \nPlease Try Again...")
                print("=" * 30)
                Main()

def AddFoodIndex():        
        # Add Menu Makanan dengan Index
        F = 1
        print(FoodList)
        index = int(input("Insert your new index = "))
        AddFIndex = input("Input your new food name = ")
        AddFIPrice = input("Input the menu price = ")

        FoodList.insert(index,AddFIndex)
        FoodPrice.insert(index,AddFIPrice)

        print("\n============================")
        print("Your new food has been added")
        print("============================")

        print("\n==================================================")
        choose = input("Do you want to add another food? (Yes/Continue) ")
        if choose == 'Yes' or choose == 'yes':
                AddFoodIndex()
        elif choose == 'Continue' or choose == 'continue':
                chose = input("Do you want to add drink normal or using index? = ")
                if chose == 'Normal' or chose == 'normal':
                        AddDrink()
                elif chose == 'index' or chose == 'Index':
                        AddDrinkIndex()
                else:
                        print("=" * 30)
                        print("We cant identify your input. \nPlease Try Again...")
                        print("=" * 30)
                        Main()     

        else:
                print("=" * 30)
                print("We cant identify your input. \nPlease Try Again...")
                print("=" * 30)
                Main()
        F+=1

def AddDrink():
        # Add Menu Minuman di Akhir #
        D = 1
        print("\n==========================================")
        AddDmenu = input("Input your new drink name = ")
        AddDPrice = input("Input the menu price = ")
        DrinkList.append(AddDmenu)
        DrinkPrice.append(AddDPrice)
        D +=1
        choose = input("Do you want to add another drink? ")
        if choose == 'Yes' or choose == 'yes':
                AddDrink()
        elif choose == 'No'or choose =='no':
                print("=\n=========================")
                print("changes saved successfully")
                print("==========================")
        Back()

def AddDrinkIndex():
        # Add Menu Minuman using index Akhir #
        D = 1
        print(DrinkList)
        index = int(input("Insert your new index = "))
        AddDIndex = input("Input your new drink name = ")
        AddDIPrice = input("Input the menu price = ")

        DrinkList.insert(index,AddDIndex)
        DrinkPrice.insert(index,AddDIPrice)
        D +=1

        choose = input("Do you want to add another drink? ")
        if choose == 'Yes' or choose == 'yes':
                AddDrinkIndex()
        elif choose == 'No'or choose =='no':
                print("\n=============================")
                print("Your new drink has been added")
                print("=============================")
        Back()

def ChangeMenu():
        print("\n=============== Change Menu ================")
        choose = input("Which one do you want to edit? (Food/Drink) ")
        print("============================================")
        if choose == 'Food' or choose == 'food':
                FoodMenu()
                x = input("Choose Food That You Want to Edit : ")
                change_food = x.title()
                new_name = ''
                if change_food in FoodList:
                        change_name = input('Change menu name? (Yes/No) ')
                        if change_name == 'Yes' or change_name == 'yes':
                                name = input('Input your new menu name: ')
                                new_name = name.title()
                                FoodList[FoodList.index(change_food)] = new_name
                        
                        change_price = input('Change menu price? (Yes/No) ')
                        if change_price == 'Yes' or change_price == 'yes':
                                new_price = int(input('Input your new menu price: '))
                                if new_name in FoodList:
                                        FoodPrice[FoodList.index(new_name)] = new_price
                                        print("Change has been successfully saved.")
                                        input("Returning to menu...")
                                        Back()
                                else:
                                        FoodPrice[FoodList.index(change_food)] = new_price
                                        print("Change has been successfully saved.")

                                        choice = input("do you want to change another menu? ")
                                        if choice == 'yes' or choice == 'Yes':
                                                ChangeMenu()
                                        elif choice == 'no' or choice == 'No':
                                                Back()

                        elif change_price == 'No' or change_price == 'no':
                                print("The price has no changes")
                                Main()

        elif choose == 'Drink' or choose == 'drink':
                DrinkMenu()
                y = input("Choose Drink That You Want to Edit : ")
                change_drink = y.title()
                new_name = ''
                if change_drink in DrinkList:
                        change_name = input('Change menu name? (Yes/No) ')
                        if change_name == 'Yes' or change_name == 'yes':
                                name = input('Input your new menu name: ')
                                new_name = name.title()
                                DrinkList[DrinkList.index(change_drink)] = new_name

                change_price = input('Change menu price? (yes/no)')
                if change_price == 'Yes' or change_price == 'yes':
                        price = int(input('Input your new menu price: '))
                        new_price = price.title()
                        if new_name in DrinkList:
                                DrinkPrice[DrinkList.index(new_name)] = new_price
                                print("Change has been successfully saved.")
                                input("Returning to menu...")
                                Back()
                        else:
                                DrinkPrice[DrinkList.index(change_drink)] = new_price
                                print("Change has been successfully saved.")

                                choice = input("do you want to change another menu? ")
                                if choice == 'yes' or choice == 'Yes':
                                        ChangeMenu()
                                elif choice == 'no' or choice == 'No':
                                                Back()
        else:
                ChangeMenu()

def DeleteMenu():
        print("\n==========================================")
        choose = input("Which one do you want to delete? (Food/Drink) ")
        print("==========================================")
        if choose == 'Food' or choose == 'food':
                FoodMenu()
                df = input("Please choose food that you want to delete = ")
                delete_food = df.title()
                if delete_food in FoodList:
                        delete_menu = input("Do you want to delete this menu? (Yes/No) ")
                        if delete_menu == 'Yes' or delete_menu == 'yes':
                                FPrice = FoodList.index(delete_food)
                                FoodList.remove(delete_food)
                                FoodPrice.pop(FPrice)
                                input("Menu has been deleted.")
                                Back()

        elif choose == 'Drink' or choose == 'drink':
                DrinkMenu()
                dd = input("Please choose drink that you want to delete = ")
                delete_drink = dd.title()
                if delete_drink in DrinkList:
                        delete_menu = input("Do you want to delete this menu? (Yes/No) ")
                        if delete_menu == 'Yes' or delete_menu == 'yes':
                                DPrice = DrinkList.index(delete_drink)
                                DrinkList.remove(delete_drink)
                                DrinkPrice.pop(DPrice)
                                input("Menu has been deleted.")
                                Back()
                
        else:
                print("We cant identify your input. \nPlease try again ")
                DeleteMenu()
Main()