# example of variable python will figure out what you are trying to say
# let name = variable; js version
name = "Alex" # string
age = 27 #integer
height = 6 #float
is_student = False # boolean

print(f"name: {name}, age: {age}, height: {height}")
print("Type of age: ", type(name))

#Example of an if statement
age = 35 #integer
if age < 13:
    print ("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")

    # for loops
    for i in range(5):
        if i == 3:
            continue
        print(i)
        
  # List --> array JS
fruits = ["Apple", "banana", "watermelon"]
print(fruits)
fruits.append("date")
print(fruits)
print (fruits[1:3])

# dictionary
student = {
    "name": "Alex",
    "age": 20,
    "courses": ["math","sciences"]
}
print(student["courses"])
(student)["grade"] = "A"
student.update({"email":"amolina555@hotmail.com"})
print(student)

# fuctions
def say_hello():
    print("Hello")
def say_goodbye():
    print("goodbye")
#call the functions
say_hello()
say_goodbye()

#concatenate
print("Hello my name is " + name + " and i have "+ str(age) + " old")

