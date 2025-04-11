pet_name = input()
type_of_pet = input()
age = int(input())
name = input()

pets = {
    pet_name:{
        'Вид питомца': type_of_pet,
        'Возраст питомца': age,
        'Имя владельца': name
    }
}
print("Это", pets[pet_name]["Вид питомца"], end=' ')
print("по кличке", f'"{pet_name}"',end='.')
print("Возраст питомца:", pets[pet_name]["Возраст питомца"], end='.')
print("Имя владельца:", pets[pet_name]["Имя владельца"], end=' ')