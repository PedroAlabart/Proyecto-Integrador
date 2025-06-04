class User:
    def __init__(self, first_name, middle_initial, last_name, city_id):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.city_id = city_id

    def full_name(self):
        parts = [self.first_name]
        if self.middle_initial:
            parts.append(f"{self.middle_initial}.")
        parts.append(self.last_name)
        return " ".join(parts)