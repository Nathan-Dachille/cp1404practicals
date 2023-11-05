"""Project Class for Project Management Program Exercise."""


class Project:
    """Stores Project data."""
    def __init__(self, name, start_date, priority=1, cost_estimate=10.1, completion_percentage=0):
        """Initialise Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Returns string representing Project data."""
        return (f"{self.name}, start:{self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%")

    def is_completed(self):
        return self.completion_percentage == 100
