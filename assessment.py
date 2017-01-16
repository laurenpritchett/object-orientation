"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1. Encapsulation: Classes combine data and functionality.
   2. Abstraction: Methods can be used without knowing their inner mechanics.
   3. Polymorphism: Classes facilitate the creation of different types of things
   with shared and unique attributes.

2. What is a class?

   A class is a Type of thing. Most classes inherit from the built-in object class.

3. What is an instance attribute?

   An instance attribute is data that belongs to an individual occurrence of a
   class.


4. What is a method?

   A method is a function defined on a class that always take at least one parameter,
   self (referring to the instance a method is called on). When the method is called,
   the self parameter is assumed and does not need to be explicitly passed.

   For example: fluffy.lick()

5. What is an instance in object orientation?

   An instance is an individual occurrence of a class. It is an object.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute given to every instance of a class,
   whereas an instance attribute applies to a single instance. Class attributes
   can sometimes have placeholder values like None.

   If I were creating a Dog class, I would add a class attribute leg_count and
   set it to 4. If I wanted to instantiate a disabled dog, I would replace the
   class attribute leg_count = 4 with an instance attribute leg_count = 3.

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question
        user_answer = raw_input(" > ")
        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        score = 0
        for question in self.questions:
            accurate = question.ask_and_evaluate()
            if accurate:
                score += 1
        return float(score)/len(self.questions)


class Quiz(Exam):

    def administer(self):
        percentage = super(Quiz, self).administer()
        if percentage > 0.50:
            return True
        else:
            return False


def take_test(exam, student):
    student.score = exam.administer()
    print "{} scored {:.2f} on the {}.".format(student.first_name, student.score, exam.name)


def example():
    exam = Exam('midterm')
    exam.add_question('How many continents are there?', '7')
    exam.add_question('What is 2^3?', '8')
    exam.add_question('How many states are there in the US?', '50')

    francesca = Student('Francesca', 'Ruiz', '22 Daisy Ct')

    take_test(exam, francesca)

# example_quiz() wasn't explicitly asked for in the instructions, but I used it to
# verify that the administer method on quizzes returns "True" or "False".

# def example_quiz():
#     quiz = Quiz('pop quiz')
#     quiz.add_question('How many continents are there?', '7')
#     quiz.add_question('What is 2^3?', '8')
#     quiz.add_question('How many states are there in the US?', '50')

#     return quiz.administer()
