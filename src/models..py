class Exercise:
    def __init__(self, name, sets, reps, date=None):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.date = date or 'Vandaag'

    def __str__(self):
        return f"{self.name}: {self.sets} sets van {self.reps} reps op {self.date}"
