class Human:
    # Class Variable
    CLASS_NAME = "HUMAN"

    # Constructor
    def __init__(self, human_type):
        self.human_type = human_type

    # Instance Method
    def walk(self):
        # Instance Variable
        human_type = self.human_type

        print(f'{human_type} is walking')

    # Static Method
    @staticmethod
    def print_class_name():
        print('This is a Human Class')

    @classmethod
    def update_human(cls, updated_name):
        cls.CLASS_NAME = updated_name


# Object Creation
male = Human('Male')

# Calling of Instance Method
male.walk()

# Calling of static method
Human.print_class_name()

# Calling of Class Variables
print(Human.CLASS_NAME)
print(male.CLASS_NAME)

Human.update_human('Update Human Name')
print(Human.CLASS_NAME)
