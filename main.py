for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Privet")
    elif i % 3 == 0:
        print("Poka")
    elif i % 5 == 0:
        print("Tut")
    else:
        print(i)
