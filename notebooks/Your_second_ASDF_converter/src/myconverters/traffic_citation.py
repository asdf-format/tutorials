from .photo_id import PhotoID


class TrafficCitation:
    "Record of a traffic violation"

    def __init__(self, ociffer, violation, date, time, photo_id):
        self.ociffer = ociffer
        self.violation = violation
        self.date = date
        self.time = time
        self.photo_id = photo_id
