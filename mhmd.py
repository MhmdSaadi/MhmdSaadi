class MyJourney:
    """
    A class representing my journey from athletics to backend engineering
    and my vision for the future of software: AI-powered systems.
    """

    def __init__(self):
        self.name = "Mohamed Saadi"
        self.primary_focus = "Backend / Full-Stack Development"
        self.current_role = "CIO at Club Manager"
        self.tech_stack = [
            "Python",
            "FastAPI",
            "Next.js",
            "PostgreSQL",
            "Docker"
        ]
        self.core_values = [
            "Discipline",
            "Leadership",
            "Innovation",
            "Problem Solving",
            "Performance Optimization"
        ]

    def initial_dev_spark(self):
        return (
            "My journey into technology started as a curiosity-driven hobby. "
            "I later studied Computer Science at university, where I discovered "
            "my passion for backend development and building systems that solve real problems."
        )

    def athletic_journey(self):
        """
        The sports chapter that shaped my mindset and work ethic.
        """
        sport_achievement = "National Gymnastics Team Member"
        academic_pursuit = "Master's Degree in Sport Science"
        professional_role = "Gymnastics Coach & Fitness Manager in Abu Dhabi"

        return (
            f"My athletic path includes competing as a {sport_achievement}, "
            f"earning a {academic_pursuit}, and taking on leadership roles as a "
            f"{professional_role}. This journey strengthened my discipline, resilience, "
            f"and performance-driven mindset."
        )

    def transition_to_tech(self):
        """
        Returning to software development with a stronger personal and professional mindset.
        """
        return (
            "After building discipline and leadership through sports, I returned to tech "
            "with a stronger vision: to create scalable products, solve real-world problems, "
            "and build systems that perform under pressure."
        )

    def current_work(self):
        return (
            f"Today I work as {self.current_role}, helping build a sports management "
            "SaaS platform used by professional football clubs. "
            f"My main focus is {self.primary_focus} using technologies like "
            f"{', '.join(self.tech_stack)}."
        )

    def future_goal(self):
        return (
            "My long-term goal is to build intelligent software systems powered by AI agents. "
            "I believe AI agents will become the next evolution of backend systems — "
            "autonomous components that can reason, make decisions, and interact with "
            "APIs, databases, and services to solve complex tasks automatically. "
            "I am actively learning how to design and integrate AI agents into "
            "modern backend architectures."
        )

    def tell_my_story(self):
        print(f"{self.name} - My Journey\n")
        print(f"Core values: {', '.join(self.core_values)}\n")

        story_parts = [
            self.initial_dev_spark(),
            self.athletic_journey(),
            self.transition_to_tech(),
            self.current_work(),
            self.future_goal()
        ]

        print("My Story:\n")

        for part in story_parts:
            print(f"- {part}")

if __name__ == "__main__":
    my_profile = MyJourney()
    my_profile.tell_my_story()
