class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value
        self.initial_values()

    def initial_values(self):
        if not (self.min_value <= self.current <= self.max_value):
            raise ValueError(f"Error: value must be within the range: {self.min_value} to {self.max_value}!")

    def set_current(self, start):
        if not (self.min_value <= start <= self.max_value):
            raise ValueError(f"Error: value must be within the range: {self.min_value} to {self.max_value}!")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError(f"Error: max value must be greater or equal to min!")
        self.max_value = max_max
        # self.current = self.max_value if self.current > self.max_value else None
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError(f"Error: min value must be less or equal to max!")
        self.min_value = min_min
        # self.current = self.min_value if self.current < self.min_value else None
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError(f"Error: max value has been reached!")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError(f"Error: min value has been reached!")

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'




























