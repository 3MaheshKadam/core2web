class VotingErr(Exception):
    def __init__(self, message):
        super().__init__(message)

def voting(name, age):
    if age < 18:
        raise VotingErr("Not eligible to vote.")
    else:
        print("You are eligible to vote.")

print("Start code")
name = input("Enter your name")

try:
    age = int(input("Enter age"))
except ValueError:
    print("Add integer data")
    age = int(input("Enter your age:"))

try:
    voting(name, age)
except VotingErr as err:
    print(err)

print("End code")
