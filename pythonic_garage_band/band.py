class Band:
    all_bands = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.all_bands.append(self)

    def to_list(self):
        print(all_bands)


class Musician():
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def play_solo(self):
        return "face melting guitar solo"

    def get_instrument(self):
        return "guitar"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
