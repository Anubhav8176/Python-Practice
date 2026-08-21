def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield
    while True: 
        print(f"Preparing: {order}")
        order = yield


stall = chai_customer()
print(next(stall))

# stall.send("Masala chai")
# stall.send("Ginger chai")