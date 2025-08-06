class PhotoID:
    "Holds Phot ID information"

    def __init__(self, last_name, first_name, image):
        "expects a monochromatic numpy array for image"
        self.last_name = last_name
        self.first_name = first_name
        self.photo = image

    def name(self):
        return self.last_name + ', ' + self.first_name
