
# Dictionaries (quiz tasks)

# N1-------------------------------------------------------------------

init_keys = ["Ten", "Twenty", "Thirty"]
init_values = [10, 20, 30]


res_dict = dict(zip(init_keys, init_values)) 

print(res_dict)


# N2-------------------------------------------------------------------

new_dict =  {"Thirty":30, "Fourty":40, "Fifty": 50}

def Merge(res_dict, new_dict):
    result = res_dict | new_dict
    return result

out_dict = Merge(res_dict, new_dict)

print (out_dict)


# N3-------------------------------------------------------------------

test_dict = {
    "class": {
        "student":{
            "name":"Mike",
            "marks":{
                "physics": 70,
                "history": 80
            }
        }
    }
}

print()
print(test_dict["class"]["student"]["marks"]["history"])


# N4-------------------------------------------------------------------
print()

name = str.capitalize(input("What's your name?"))
surname = str.capitalize(input("What's your surname?"))
age = input("What's your age?")
country = input("Country?").upper()
city = str.capitalize(input("And last, your city?"))

id_card = {"Name":name, "surname":surname,"age":age, "country":country,"city":city}

print(f"\nusername: {name} {surname}")
print(f"age: {age}")
print(f"adress: {country}, {city}")

print()

# N5-------------------------------------------------------------------

city1 = str.capitalize(input("1st city: "))
population1 = int(input(f"population of {city1}: "))

city2 = str.capitalize(input("2nd city: "))
population2 = int(input(f"population of {city2}: "))

city3 = str.capitalize(input("3rd city: "))
population3 = int(input(f"population of {city3}: "))

city4 = str.capitalize(input("4th city: "))
population4 = int(input(f"population of {city4}: "))


cities = [{city1:population1},{city2:population2}, {city3:population3}, {city4:population4}]

print()

print(cities[0])





