# Decorator to format report
def format_report(func):
    def wrapper(*args, **kwargs):
        print("\n" + "*" * 40)
        print("      STUDENT PROGRESS REPORT")
        print("*" * 40)
        func(*args, **kwargs)
        print("*" * 40)
    return wrapper


class StudentReport:
    templates = {
        "Semester": "Semester Report",
        "Annual": "Annual Report"
    }

    def __init__(self, student_name, grade, template):
        self.student_name = student_name
        self.grade = grade
        self.template = template

    # Class method
    @classmethod
    def add_template(cls, name, value):
        cls.templates[name] = value

    # Magic method
    def __str__(self):
        return (f"Student Name : {self.student_name}\n"
                f"Grade        : {self.grade}\n"
                f"Template     : {self.templates.get(self.template, 'Not Available')}")

    @format_report
    def display(self):
        print(self)


# Driver Code
StudentReport.add_template("Monthly", "Monthly Progress Report")

report = StudentReport(
    "Khushi",
    "A+",
    "Monthly"
)

report.display()