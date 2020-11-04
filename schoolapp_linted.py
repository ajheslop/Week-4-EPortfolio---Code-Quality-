'''
    MScDigital&Technology Solutions-CETM65SoftwareEngineeringPrinciples
    Author: Alan John Heslop
    Student Number: bh83dl
    Date: 11/10/2020
    ---------------------------------------------------------------------------------

    EDUCATION OOP

-SCHOOLDETAILs
- here we want to be able to define the school in which a
student (child) attends and the location of the school
(assuming they could be different)
- CHILD DETAILS
    - here we are able to define the child who is a child of school
    - the basic information will be getting the details of the child.
- Overview
    - Overview's main idea is to be multiple inheritence and have
    it's own details requested (grades and attendance)
    then this will be consolidated as one final string to output
    '''


class School():  # defines a class in python, this is the school class

    '''starter class that provides the child wih a schoolname and location'''
    def __init__(self, schoolname, location):
        self.schoolname = schoolname  # set attributes for the class
        self.location = location  # set attributes for the class
        # print('(Initialized School Class: {})'.format(self.schoolname))
        # simply a debugging statement to see if the schoolname has
        # correctly passed in a string

    def getschoolname(self):  # Defining the method schoolname
        """Return the the variable."""
        return self.schoolname

    def getschoollocation(self):  # Defining the method schoollocation
        """Return the the variable."""
        return self.location

    def __str__(self):  # I am using str to return the school name and location
        return f"School Name: {self.schoolname}.\
            School Location: {self.location}"

    # repr method below, showing 2 options of printing the item
    def __repr__(self):  # I am using the reper
        # method below to pass the same details as the string
        # return f" {self.schoolname}, {self.location}"
        return "school name: {}, \
        Location {}".format(self.schoolname, self.location)

    # Prints using the REPR function too.
    # instantiating the items for printing


sch = School("Royal Grammar School", "Newcastle Upon Tyne")


print("Below is an example of passing __repr__")
print(repr(sch))
print()

# 2nd class about the child attending the School


class Child(School):  # Child class is using inheritance from the School Class
    """Child class stores data about the child"""
    # pylint: disable-msg=too-many-arguments
    def __init__(self, name, age, yeargroup, schoolname, location):
        self.name = name
        self.age = age
        self.yeargroup = yeargroup
        super().__init__(schoolname, location)
        self.__password = 1  # private arrtribute for the users password
        self._pass = 20
        self.word = 3
        self.displaychildname()  # Extract function/method

    def displaychildname(self):
        """ New function to display the child name
        """
        print({self.name})

    def function_password(self):
        """ extract variables concept
        """
        newpass = self.name + str(self.age)
        return newpass()

        # Showing that data is being passed correctly on-screen
        # print('(Initialized Child Class: {})'.format(self.name))
        # print('(Initialized Child Class: {})'.format(self.age))
        # print("{}".format(self.name))

    @staticmethod  # i dont need to access the method
    def resetpassword(self):
        """ Part of my single responsibility concept
        """
        return True

    def getchildname(self):
        """Calling the class variable above"""
        return self.name

    def getchildage(self):
        """Calling the class variable above"""
        return self.age

    def getchildyeargroup(self):
        """Calling the class variable above"""
        return self.yeargroup
# this string is displaying the information

    def __str__(self):
        return f"{self.name} is {self.age} and is \
            currently is yearx  {self.yeargroup} and the \
                school name is {self.location } {super().__str__()}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"
# all the attributes associated with the 't'
# instantiation

class Password():
    pass
"""Part of a single responsibility concept, will hold password details"""

# 4th class will show the attendance, grade and bring back all data


class Overview(Child, School):  # multiple inheritence
    """Overview class will contain inheritence """
    # pylint: disable-msg=too-many-arguments
    def __init__(self, attendance, grade, name, age,
                 yeargroup, schoolname, location):
        self.attendance = attendance
        self.grade = grade
        super().__init__(name, age, yeargroup, schoolname, location)
        # print('(Initialized Overview Class: {})'.format(self.name))

    def getattendance(self):
        """Calling the class variable above"""
        return self.attendance

    def getgrade(self):
        """Calling the class variable above"""
        return self.grade

    # inherited
    # __Str__ informal representation
    def __str__(self):  # STR method to print out an easily readable sentence.
        return f"{self.name}s attendance has been oustanding,\
        acheiving an overall attendance of: {self.attendance}.\
        He is currently Aged: {self.age}\
        and is in YearGroup:  {self.yeargroup}\
        and his overall grade for the year is: {self.grade}\
        - he attends the school\
        in {self.location} and the name of the school is {self.schoolname}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

# Final instantiating
# Person 1


p1 = Overview("80%", "A", "Kieran", 8, 12,
              "Royal Grammar School", "Newcastle Upon Tyne")

print(p1)
print()
# Person 2
p2 = Overview("20%", "B", "Alan Heslop", 31,
              "University", "Sunderland University", "Sunderland")
print(p2)
print()

# access repr string
print()
print("__repr__ output")
print()
print(repr(p1))
print()
# the manual way of inputting the data to the screen,\
# this was the first method to test the data passed

# print(p1.getSchoolName())

# p1.name = "alan"
# p1.age = "12"
# p1.yeargroup = 8
# p1.location = "Newcastle"

# print()
# print(Overview.__bases__)

# returns a list of all the members in the specified object
# print(dir(p1))
