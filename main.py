'''
    _ANIMEX_: This is a better improved version of Animex

    By Parker Phelps
'''


from tkinter import *
from classes.Product import *


# Windows
startWindow = Tk()
userWindow = Toplevel(startWindow)
loginWindow = Toplevel(userWindow)
storeWindow = Toplevel(userWindow)
cartWindow = Toplevel(storeWindow)


# Colors
carnation = "#F24A51"
outerspace = "#2D383A"
gallery = "#EFEFEF"
christine = "#E7730A"

# Arrays
cart = []
cartQuantities = []
cartPrices = []
doubleCartPrices = []
products = [test, test2, test3]
windows = [startWindow, userWindow, loginWindow, storeWindow, cartWindow]
userName = []
passWord = []

# This 2 arrays are used to check if the user is logged in and to skip the create account window if the user just created one
loggedIn = []
skipAccountCreate = []


# Functions
'This is used to setup a window without reusing the same code'
def windowSetup(window, width, height, titleTxt):
    window.geometry(str(width)+"x"+str(height))
    window.title(titleTxt)
    window.resizable(False, False)
    centerWindow(window, width, height)

'This is used to center a window on the users screen'
def centerWindow(window, width, height):

    # Getting the users screen measurments
    userW = window.winfo_screenwidth()
    userH = window.winfo_screenheight()

    # Getting x and y
    x = (userW/2) - (width/2)
    y = (userH/2) - (height/2)

    # Centering the window
    window.geometry('+%d+%d' % (x, y))

'This is used to exit/close the app'
def exitApp():
    startWindow.quit()

'This is used to hide all the windows'
def hideAllWindows():
    for window in windows:
        window.withdraw()

'This is used to detect if the user has input valid account values'
def checkAccountCreationValues():
   if inputSet1Entry.get() == "":
       print("You cannot have an blank username.")

   if inputSet1Entry in userName:
       print("That username is already being used")

   if inputSet2Entry.get() == "":
       print("You cannot have an blank password.")

   if inputSet1Entry.get().count(' ') > 0:
        print("You cannot have spaces in your username.")

   if inputSet2Entry.get().count(' ') > 0:
        print("You cannot have spaces in your password.")

'This is used to show the passwords and usernames the user has created'
# def showPasswordsAndUsernames():
#     if len(userName) > 0:
#         print("Here is a list of all your usernames:")
#         for u in userName:
#             print(u)
#
#         print("Here is a list of your passwords:")
#         for p in passWord:
#             print(p)

'Entering the different windows'
def enterStart():
    hideAllWindows()
    startWindow.deiconify()
def enterUserOrLoginOrStore():

    if len(loggedIn) > 0:
        enterStore()

    if len(loggedIn) > 0 and len(skipAccountCreate) <= 0:
        enterStore()

    if len(loggedIn) <= 0 and len(skipAccountCreate) <= 0:
        enterUser()

    if len(loggedIn) == 0 and len(skipAccountCreate) > 0:
        enterLogin()
def enterUser():
    # showPasswordsAndUsernames()

    hideAllWindows()
    userWindow.deiconify()
def enterLogin():


    loggedIn.clear()

    print("Here is the username you created: " + inputSet1Entry.get())
    print("Here is the password you created: " + inputSet2Entry.get())

    # showPasswordsAndUsernames()

    checkAccountCreationValues()

    if not inputSet1Entry.get() in userName:
        if inputSet1Entry.get() != "" and not inputSet1Entry.get().count(' ') > 0 and inputSet2Entry.get() != "" and not inputSet2Entry.get().count(' ') > 0:

            hideAllWindows()
            storeAccountInfo()

            skipAccountCreate.append(True)

            loginWindow.deiconify()

    # Skips to store
    if len(skipAccountCreate) > 0:
            hideAllWindows()
            storeAccountInfo()

            loginWindow.deiconify()
def enterStore():
    print(inputSet3Entry.get())

    skipAccountCreate.clear()
    hideAllWindows()
    storeWindow.deiconify()
def enterCart():

    # Printing username
    print(inputSet3Entry.get())

    # Adding cart total

    cartTotalLabel.config(text="$ 0.00")
    cartTotalPrice = calculateCartTotalPrice()
    cartTotalLabel.config(text="$ " + str(cartTotalPrice))

    cartLB.delete(0, END)
    for item in cart:
        cartLB.insert(END, item)

    skipAccountCreate.clear()
    hideAllWindows()
    cartWindow.deiconify()

'This is used to login the user'
def loginUser():

    loggedIn.clear()

    validUsername = False
    validPassword = False

    for u in userName:
        if inputSet3Entry.get() == u:
            print("This username exists")
            validUsername = True

        else:
            print("This username does not exist")

    for p in passWord:
        if inputSet4Entry.get() == p:
            print("This password exists")
            validPassword = True

        else:
            print("This password does not exist")


    if validUsername and validPassword:
        loggedIn.append(True)
        enterStore()

'This is used to logout the user'
def logoutUser():

    inputSet1Entry.delete(0, END)
    inputSet2Entry.delete(0, END)
    inputSet3Entry.delete(0, END)
    inputSet4Entry.delete(0, END)

    userName.clear()
    passWord.clear()
    loggedIn.clear()
    enterStart()

'This is used to store the account info'
def storeAccountInfo():
    if not inputSet1Entry.get() in userName:
        userName.append(inputSet1Entry.get())
        passWord.append(inputSet2Entry.get())

'This is used to add the items to the cart'
def addItemsToCart():

    cart.clear()
    cartPrices.clear()
    cartLB.delete(0, END)

    if storeProductsLB.curselection():
        for selected in storeProductsLB.curselection():
            cart.append(storeProductsLB.get(selected))
            cartPrices.append(storeProductsLB.get(selected).split(" - $")[1].strip())

        enterCart()

    else:
        print("You have not selected any items..")

'This is used to calculate the total price for the cart'
def calculateCartTotalPrice():

    doubleCartPrices.clear()

    for price in cartPrices:
        doubleCartPrices.append(float(price))

    return round(sum(doubleCartPrices), 2)

'This is used to clear the cart'
def clearCart():
    storeProductsLB.selection_clear(0, END)
    cart.clear()
    cartPrices.clear()
    cartLB.delete(0, END)
    doubleCartPrices.clear()
    cartTotalLabel.config(text="$ 0.00")

'This is used to checkout the cart'
def checkoutCart():
    if len(cart) > 0:
        enterStart()
    if len(cart) <= 0:
        print("There are no items to checkout..")

    clearCart()

# WIDGET CREATION FUNCTIONS
'This is used to create a toolbar for each window'
def createToolBar(window):
    if window == userWindow:

        userWindowToolBar = Frame(userWindow)
        userWindowToolBarExitBtn = Button(userWindowToolBar, text="EXIT", command=exitApp, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=5, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(20, 20))
        userWindowToolBarStartBtn = Button(userWindowToolBar, text="START", command=enterStart, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=6, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(0, 0))
        userWindowToolBar.pack(side=TOP, anchor=W)

    if window == loginWindow:

        loginWindowToolBar = Frame(loginWindow)
        loginWindowToolBarExitBtn = Button(loginWindowToolBar, text="EXIT", command=exitApp, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=5, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(20, 20))
        loginWindowToolBarStartBtn = Button(loginWindowToolBar, text="START", command=enterStart, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=6, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(0, 0))
        loginWindowToolBar.pack(side=TOP, anchor=W)

    if window == storeWindow:

        storeWindowToolbar = Frame(storeWindow)
        storeWindowToolBarExitBtn = Button(storeWindowToolbar, text="EXIT", command=exitApp, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=5, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(20, 20))
        storeWindowToolBarStartBtn = Button(storeWindowToolbar, text="START", command=enterStart, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=6, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(0, 0))
        storeWindowToolBarCartBtn = Button(storeWindowToolbar, text="CART", command=enterCart, fg=gallery, bg=carnation, activebackground=christine, activeforeground=gallery, font=("Lato Bold", 10), width=5, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(20, 20))
        storeWindowToolBarLogoutBtn = Button(storeWindowToolbar, text="LOGOUT", command=logoutUser, fg=gallery, bg=carnation, activebackground=christine, activeforeground=gallery, font=("Lato Bold", 10), width=8, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(0, 0))
        storeWindowToolbar.pack(side=TOP, anchor=W)

    if window == cartWindow:

        cartWindowToolbar = Frame(cartWindow)
        cartWindowToolBarExitBtn = Button(cartWindowToolbar, text="EXIT", command=exitApp, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=5, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(20, 20))
        cartWindowToolBarStartBtn = Button(cartWindowToolbar, text="START", command=enterStart, fg=gallery, bg=outerspace, activebackground="black", activeforeground=gallery, font=("Lato Bold", 10), width=6, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(0, 0))
        cartWindowToolBarStoreBtn = Button(cartWindowToolbar, text="STORE", command=enterStore, fg=gallery, bg=carnation, activebackground=christine, activeforeground=gallery, font=("Lato Bold", 10), width=6, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(20, 20))
        cartWindowToolBarLogoutBtn = Button(cartWindowToolbar, text="LOGOUT", command=logoutUser, fg=gallery, bg=carnation, activebackground=christine, activeforeground=gallery, font=("Lato Bold", 10), width=8, height=1, bd=0).pack(side=LEFT, pady=(20, 20), padx=(0, 0))
        cartWindowToolbar.pack(side=TOP, anchor=W)




if __name__ == "__main__":


    # Showing the start window by default
    enterStart()

    # Start Window
    windowSetup(startWindow, 650, 650, "Welcome to Animex - Manga/Anime Store")

    'Widgets'
    startWindowTextHolder = Frame(startWindow, height=650, width=650)
    startWindowMainHeading = Label(startWindowTextHolder, text="ANIMEX", font=("Lato Bold", 44), fg=carnation).place(relx=0.5, rely=0.33, anchor=CENTER)
    startWindowMainText = Label(startWindowTextHolder, text="Anime/Manga Store", font=("Lato", 18), fg=outerspace).place(relx=0.5, rely=0.42, anchor=CENTER)
    startWindowCreator = Label(startWindowTextHolder, text="PARKER PHELPS", font=("Lato", 10), fg=outerspace).place(relx=0.5, rely=0.48, anchor=CENTER)
    startWindowButtons = Frame(startWindow)
    startWindowEnterBtn = Button(startWindowButtons, text="ENTER", font=("Lato", 13), width=7, height=1, bg=carnation, fg=gallery, bd=0, command=enterUserOrLoginOrStore, activebackground=christine, activeforeground=gallery).pack(pady=(15, 15))
    startWindowExitBtn = Button(startWindowButtons, text="EXIT", font=("Lato", 13),  width=6, height=1, bg=outerspace, fg=gallery, bd=0, command=exitApp, activebackground='black', activeforeground=gallery).pack()
    startWindowButtons.place(relx=0.5, rely=0.65, anchor=CENTER)

    startWindowTextHolder.pack()


    # User Window
    windowSetup(userWindow, 650, 650, "Animex - User")
    createToolBar(userWindow)
    userWindowMainHeading = Label(userWindow, text="Create An Account", font=("Lato", 18), fg=outerspace).pack(pady=(100,50))

    inputSet1Frame = Frame(userWindow)
    inputSet1Label = Label(inputSet1Frame, text="USERNAME:", font=("Lato", 12), fg=carnation).pack(anchor=W, pady=(20, 10), padx=(0, 125))
    inputSet1Entry = Entry(inputSet1Frame, width=50)
    inputSet1Entry.pack()
    inputSet1Frame.pack(anchor=CENTER)

    inputSet2Frame = Frame(userWindow)
    inputSet2Label = Label(inputSet2Frame, text="PASSWORD:", font=("Lato", 12), fg=carnation).pack(anchor=W, pady=(20, 10), padx=(0, 125))
    inputSet2Entry = Entry(inputSet2Frame, width=50)
    inputSet2Entry.pack()
    inputSet2Frame.pack(anchor=CENTER)



    userWindowCreateBtn = Button(userWindow, text="CREATE", font=("Lato", 13), width=7, height=1, bg=carnation, fg=gallery, bd=0, command=enterLogin, activebackground=christine, activeforeground=gallery).pack(pady=(40,0))

    # Login Window
    windowSetup(loginWindow, 650, 650, "Animex - Login")
    createToolBar(loginWindow)
    loginWindowMainHeading = Label(loginWindow, text="Sign In", font=("Lato", 18), fg=outerspace).pack(pady=(100,50))

    inputSet3Frame = Frame(loginWindow)
    inputSet3Label = Label(inputSet3Frame, text="USERNAME:", font=("Lato", 12), fg=carnation).pack(anchor=W, pady=(20, 10), padx=(0, 125))
    inputSet3Entry = Entry(inputSet3Frame, width=50)
    inputSet3Entry.pack()
    inputSet3Frame.pack(anchor=CENTER)

    inputSet4Frame = Frame(loginWindow)
    inputSet4Label = Label(inputSet4Frame, text="PASSWORD:", font=("Lato", 12), fg=carnation).pack(anchor=W, pady=(20, 10), padx=(0, 125))
    inputSet4Entry = Entry(inputSet4Frame, width=50)
    inputSet4Entry.pack()
    inputSet4Frame.pack(anchor=CENTER)

    loginWindowBtn = Button(loginWindow, text="LOGIN", font=("Lato", 13), width=7, height=1, bg=carnation, fg=gallery, bd=0, command=loginUser, activebackground=christine, activeforeground=gallery).pack(pady=(40,0))


    # Store Window
    windowSetup(storeWindow, 850, 370, "Animex - Store")
    createToolBar(storeWindow)
    storeProductsLBFrame = Frame(storeWindow)
    storeProductsLB = Listbox(storeProductsLBFrame, width=850, font=("Lato", 13), selectmode=MULTIPLE)
    storeProductsLBScrollBar = Scrollbar(storeProductsLBFrame)
    storeProductsLBScrollBar.config(command=storeProductsLB.yview)
    storeProductsLBScrollBar.pack(side=RIGHT, fill=Y)
    storeProductsLB.config(yscrollcommand=storeProductsLBScrollBar.set)

    productNum = 0
    for product in products:
        productNum = productNum + 1
        productText = str(product.get_itemName()) + " - $ " + str(product.get_itemPrice())
        storeProductsLB.insert(productNum, productText)

    storeProductsLB.pack(side=LEFT, fill=BOTH)
    storeProductsLBFrame.pack(anchor=W, pady=(0, 20), padx=(20, 20))

    storeAddItemsToCartBtn = Button(storeWindow, text="ADD ITEMS TO CART", command=addItemsToCart, font=("Lato", 13), width=19, height=1, bg=carnation, fg=gallery, bd=0, activebackground=christine, activeforeground=gallery).pack()

    # Cart Window
    windowSetup(cartWindow, 850, 850, "Animex - Cart")
    createToolBar(cartWindow)
    cartLBFrame = Frame(cartWindow)
    cartLB = Listbox(cartLBFrame, width=850, font=("Lato", 13), selectmode=MULTIPLE)
    cartLBScrollBar = Scrollbar(cartLBFrame)
    cartLBScrollBar.config(command=cartLB.yview)
    cartLBScrollBar.pack(side=RIGHT, fill=Y)
    cartLB.config(yscrollcommand=cartLBScrollBar.set)
    cartLB.pack(side=LEFT, fill=BOTH)
    cartLBFrame.pack(anchor=W, pady=(0, 20), padx=(20, 20))

    Label(cartWindow, text="TOTAL", font=("Lato", 11)).pack()
    cartTotalLabel = Label(cartWindow, text="$ 0.00", font=("Lato", 11))
    cartTotalLabel.pack()

    cartBtns = Frame(cartWindow)
    cartClearBtn = Button(cartBtns, text="CLEAR", font=("Lato", 13), width=7, height=1, bg=outerspace, fg=gallery, bd=0, command=clearCart, activebackground="black", activeforeground=gallery).pack(pady=(30, 20))
    cartCheckoutBtn = Button(cartBtns, text="CHECKOUT", font=("Lato", 13), width=10, height=1, bg=carnation, fg=gallery, bd=0, command=checkoutCart, activebackground=christine, activeforeground=gallery).pack()
    cartBtns.pack()


    # EXIT PROTOCOLS
    for window in windows:
        window.protocol("WM_DELETE_WINDOW", enterStart)


    startWindow.mainloop()
