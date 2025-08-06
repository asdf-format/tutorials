class PhotoID:
    "Holds Photo ID information"

    def __init__(self, last_name, first_name, photo):
        "expects a monochromatic numpy array for photo"
        self.last_name = last_name
        self.first_name = first_name
        self.photo = photo

    def name(self):
        return self.last_name + ', ' + self.first_name
