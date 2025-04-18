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
if age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
    print("Возраст питомца:", pets[pet_name]["Возраст питомца"], "года", end='.')
elif age % 10 == 1:
    print("Возраст питомца:", pets[pet_name]["Возраст питомца"], "год", end='.')
else:
    print("Возраст питомца:", pets[pet_name]["Возраст питомца"], "лет", end='.')

print("Имя владельца:", pets[pet_name]["Имя владельца"], end=' ')