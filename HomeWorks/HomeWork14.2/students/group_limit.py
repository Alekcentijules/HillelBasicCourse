class GroupLimitError(Exception):
    def __init__(self, text="The limit of 10 students has been exceeded! Please, keep the number of students up to the specified limit"):
        super().__init__(text)












