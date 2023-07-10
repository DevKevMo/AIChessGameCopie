class Move:
    def __init__(self, initial, final):
        # inital and final are squares
        self.initial = initial
        self.final = final

    # check if final and initial are equal
    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final
