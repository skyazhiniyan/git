people = {
    "name" : 'name',
    "details" : 'details'
}
print("welcome to the people welfare system")

name = input("enter the people name:")
people['name'] = name
details = input("enter the details of the people:")
people['details'] = details
while True:
    name = input("enter the name of the person you want to search:")
    if name == people['name']:
        print("the details of the person is:", people['details'])
    else:
        print("person not found")
        break
