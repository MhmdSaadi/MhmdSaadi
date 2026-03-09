class MyJourney:
    """
    Represents my journey combining athletics and backend development.
    """

    def __init__(self):
        self.primary_focus = "Python Backend Development"
        self.core_values = [
            "Discipline",
            "Innovation",
            "Problem Solving",
            "Performance Optimization"
        ]

    def initial_dev_spark(self):
        return (
            "Started programming as a hobby and later studied Computer Science "
            "for two years at university."
        )

    def athletic_pivot(self):
        sport = "National Gymnastics Team Member"
        degree = "Master's Degree in Sport Science"
        role = "Gymnastics Coach & Fitness Manager (Abu Dhabi)"

        return (
            f"Competed as a {sport}, earned a {degree}, "
            f"and worked professionally as a {role}."
        )

    def current_dev_focus(self):
        return (
            f"Now focused on {self.primary_focus}, using discipline from sports "
            "to build high-performance backend systems with FastAPI and Python."
        )

    def tell_my_story(self):
        print("My Journey\n")

        steps = [
            self.initial_dev_spark(),
            self.athletic_pivot(),
            self.current_dev_focus()
        ]

        for step in steps:
            print(f"- {step}")

        print("\nCore values:", ", ".join(self.core_values))


if __name__ == "__main__":
    profile = MyJourney()
    profile.tell_my_story()
