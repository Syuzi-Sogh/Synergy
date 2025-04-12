import collections

pets = {}

def create():
    last_id = max(pets.keys(), default = 0)
    new_id = last_id + 1

    new_pet = {}

    print("Введите кличку питомца:", end=' ')
    new_pet['name'] = input()
    print("Введите вид питомца:", end=' ')
    new_pet['type'] = input()
    print("Введите возраст питомца:", end=' ')
    new_pet['age'] = int(input())
    print("Введите имя владельца:", end=' ')
    new_pet['owner_name'] = input()

    for pet in pets.values():
        if pet['type'] == new_pet['type'] and pet['age'] == new_pet['age'] and pet['owner_name'] == new_pet['owner_name'] and pet['name'] == new_pet['name']:
            print("Sorry")
            return

    pets[new_id] = {
        'name': new_pet['name'],
        'type': new_pet['type'],
        'age': new_pet['age'],
        'owner_name': new_pet['owner_name'],
    }

    print(f"Питомец {new_pet['name']} успешно добавлен с ID = {new_id}.")





def read():
    print("Please, print pets ID: ", end=' ')
    id_ = int(input())
    if id_ in pets:
        print("Это", pets[id_]['type'], end=' ')
        print("по кличке " f"'{pets[id_]['name']}'", end='.')
        print("Возраст питомца:", pets[id_]['age'], end='.')
        print("Имя владельца:", pets[id_]['owner_name'])
    else:
        print("Pet isn't in table")

def update():
    print("Please, enter pets ID: ", end=' ')
    id_ = int(input())
    if id_ in pets:
        print("What do you want to update?", end=' ')
        update_ = input()
        if update_ == "name":
            print("Please, enter new name:", end=' ')
            new_name = input()
            pets[id_]['name'] = new_name
        elif update_ == "type":
            print("Please, enter new type:", end=' ')
            new_type = input()
            pets[id_]['type'] = new_type
        elif update_ == "age":
            print("Please, enter new age:", end=' ')
            new_age = int(input())
            pets[id_]['age'] = new_age
        elif update_ == "owner_name":
            print("Please, enter new owner name:", end=' ')
            new_owner_name = input()
            pets[id_]['owner_name'] = new_owner_name
        else:
            print("Wrong input")

def delete():
    print("Please, enter pets ID: ", end=' ')
    id_ = int(input())
    print("Do u want to delete all information?", end=' ')
    answer = input()
    if answer == "yes":
        pets.pop(id_)
        print("Thanks for answer!")
    else:
        pets.pop(id_, None)


while True:
    print("Введите команду:", end=' ')
    command = input()
    if command == "stop":
        break

    if command == 'create':
        create()

    if command == 'read':
        read()

    if command == 'update':
        update()

    if command == 'delete':
        delete()