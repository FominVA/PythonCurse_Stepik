class Testpaper:
    def __init__(self, theme, answer, percentage):
        self.theme = theme
        self.answer = answer
        self.pass_percentage = int(percentage.strip('%'))


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, test, student_answers):
        correct = sum(1 for a, b in zip(test.answer, student_answers) if a == b)
        total = len(student_answers)
        score_percent = round((correct / total) * 100) if total > 0 else 0

        status = "Passed!" if score_percent >= test.pass_percentage else "Failed!"
        result_string = f"{status} ({score_percent}%)"

        if self.tests_taken == "No tests taken":
            self.tests_taken = {}

        self.tests_taken[test.theme] = result_string


paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student1 = Student()
student2 = Student()

student1.take_test(paper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(paper2, ['1C', '2D', '3A', '4C'])
student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

print(student1.tests_taken)
print(student2.tests_taken)


