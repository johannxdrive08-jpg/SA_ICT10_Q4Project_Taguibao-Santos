from pyscript import display, document


# Define
class Classmate:
    def __init__(self, classmate, section, favorite_subject):
        self.classmate = classmate
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.classmate} from {self.section}. My favorite subject is {self.favorite_subject}."


# Stores classmates
classmates = [
    Classmate("Robert", "Emerald", "Social Studies"),
    Classmate("James", "Sapphire", "Music"),
    Classmate("Brian", "Ruby", "Science"),
    Classmate("Jeff", "Topaz", "English"),
    Classmate("Eddie", "Amethyst", "Math")
]

#Do note these are classmates I made up...

# Add classmate
def add_classmate(e):
    classmate = document.getElementById("classmate").value
    section = document.getElementById("section").value
    favsubject = document.getElementById("favsubject").value

    new_student = Classmate(classmate, section, favsubject)
    classmates.append(new_student)

    display(f"{classmate} added successfully!\n", append=True, target='output')


# Display classmate
def show_classmates(e):
    document.getElementById('output').innerHTML = " "

    for student in classmates:
        intro = student.introduce()
        display(intro + "\n", target='output')