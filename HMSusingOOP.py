# CURRET TIME
def getDate():
    import datetime
    return datetime.datetime.now()

# READING FILE


def readFile(fname):

    print("\n")
    with open(f"{fname}", "r") as f:
        for line in f:
            print(line, end=" ")

# CHOOSE OBJECT


def select(A, s):

    identity = 0
    for e in range(len(A)):

        if e+1 == s:
            identity = A[e]
            break

    return identity


#   SELECT BETWEEN FOOD AND EXERCISE
def ask(temp):
    print(f"\nPlease Provide the Input ?")
    print(f"Press 1 - Food {temp}")
    print(f"Press 2 - Exercise {temp}")

    choice = input("Write Here - ")
    if choice == '1':
        return f"Food {temp}"

    else:
        return f"Exercise {temp}"


# -------------------------CLASS HEALTH Begin from here------------------------------
class Health:

    value = None

    def __init__(self, name=None):
        self.name = name

        self.foodFile = input(f"{self.name} | Enter your Food File name - ")
        self.foodFile = self.foodFile + ".txt"

        self.exerciseFile = input(
            f"{self.name} | Enter your Exercise File name - ")
        self.exerciseFile = self.exerciseFile + ".txt"

        # Create Your Food File
        with open(f"{self.foodFile}", 'a') as f:
            f.write(
                "\n"+f"---------------------{self.name}'s FOOD File---------------------" + "\n")

        # Create Your Exercise File
        with open(f"{self.exerciseFile}", "a") as f:
            f.write(
                f"---------------------{self.name}'s EXERCISE FILE---------------------" + "\n")

        print(f"{self.name} files has been Created")

    def getName(self):
        return self.name

    def getFiles(self):
        return self.foodFile, self.exerciseFile

    def getFoodFileName(self):
        return self.foodFile

    def getExerciseFileName(self):
        return self.exerciseFile

    def writeFoodFile(self):
        print(f"{self.name}   Wrinting")
        with open(f"{self.foodFile}", 'a') as f:
            self.value = input("Write here Food items - ")
            f.write(str(getDate()) + " " + self.value + "\n")

    def writeExerciseFile(self):
        print(f"{self.name} Wrinting")
        with open(f"{self.exerciseFile}", 'a') as f:
            self.value = input("Write here Exericse - ")
            f.write(str(getDate()) + " " + self.value + "\n")


if __name__ == "__main__":

    print("---------------------------Health Management System---------------------------")

    Record = ['Name1', 'Name2', 'Name3']
    print(f"Member are - {Record}")
    for e in range(len(Record)):
        print(
            "\n" + f"{Record[e]} Please maintain your Food File, Exercise File first.")
        Record[e] = Health(f'{Record[e]}')          # Objects Created

    flag = True

    while flag:

        print("\nWhat do you want ?")
        print("Press 1 For INSERT")
        print("Press 2 For RETRIEVE")
        print("Press 0 to EXIT")
        choice = input("Write Here - ")

        if choice == '1':

            if ask("INSERT") == "Food INSERT":

                print("\nList of Members")
                for e in range(len(Record)):
                    print(f"{e+1} - {Record[e].getName()} ")

                q = int(input("Your Input - "))
                target = select(Record, q)

                for e in range(len(Record)):
                    if Record[e] == target:
                        Record[e].writeFoodFile()

            else:

                print("\nList of Members")
                for e in range(len(Record)):
                    print(f"{e+1} - {Record[e].getName()} ")

                q = int(input("Your Input - "))
                target = select(Record, q)

                for e in range(len(Record)):
                    if Record[e] == target:
                        Record[e].writeExerciseFile()

        elif choice == "2":

            if ask("RETRIEVE") == "Food RETRIEVE":

                print("\nList of Members")
                for e in range(len(Record)):
                    print(f"{e+1} - {Record[e].getName()} ")

                q = int(input("Your Input - "))
                target = select(Record, q)

                for e in range(len(Record)):
                    if Record[e] == target:
                        readFile(Record[e].getFoodFileName())

            else:

                print("\nList of Members")
                for e in range(len(Record)):
                    print(f"{e+1} - {Record[e].getName()} ")

                q = int(input("Your Input - "))
                target = select(Record, q)

                for e in range(len(Record)):
                    if Record[e] == target:
                        readFile(Record[e].getExerciseFileName())
        else:
            flag = False

    print("\nYou did a great JOB !")
