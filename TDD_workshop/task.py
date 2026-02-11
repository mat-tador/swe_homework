class Task:
    def __init__(self, title, priority):
        """
        Class constructor.
        """
        self.title = title
        self.priority = priority

    def __repr__(self):
        """
        Return a string representation of the task.
        """
        return f"Task(title='{self.title}')"

def create_task(title, priority = None):
    if title == None or title.strip() == "":
        raise ValueError("Title cannot be empty")
    return Task(title, priority)
