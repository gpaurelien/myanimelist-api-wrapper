from .items.items import Items

class Mal:
    """
    This class is built to connect with the myanimelist API.
    """
    def __init__(self):
        self.items = Items()