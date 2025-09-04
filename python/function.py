# bakeryList = ["bread", "cake", "donuts", "cookies", "muffins", "strawberry cake"]

# def checkStock(pastry):
#     counter = 0
#     for item in pastry:
#         if item != "strawberry cake":
#             counter += 1
#             print(counter, " loop")
#             continue
#         else:
#             print("yes we are in stock")
# checkStock(bakeryList)


classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", "chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi" ]
def checkAttendance(class_list):
    counter = 0
    for item in class_list:
        if item != "chiemerie":
            counter += 1
            print(counter, " not me")
            continue
        else:
            print("yes i am here")
checkAttendance(classList)


classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", "chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi" ]
def checkAttendance(class_list):
    counter = 0
    for person in class_list:
        if person != "chiemerie":
            counter += 1
            print(f"{person} is not chiemerie ")
            continue
        else:
            print("yes i am here")
checkAttendance(classList)

return