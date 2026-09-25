def insert_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into databse")
    else :
        raise TypeError("please provide right datatype")

insert_data("aman", 30) 
insert_data("aman", "30") # this will create error [[ but if we don't write type handling code this will not create any error anymore]]

# we have to write everytime type handling code bcoz python is dynamically handle the data type and 
# not raise any error and validation code as well

def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError
        else:
            print(name)
            print(age)
            print("inserted into databse")
    else :
        raise TypeError("please provide right datatype")
update_patient_data("rahul", 24)

# so for avoiding the above we have pydantic