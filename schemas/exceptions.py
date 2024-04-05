class ObjectIdException(ValueError):
    def __init__(self):
        super().__init__("provided _id should be a valid ObjectId. (12-byte input or 24-character hex string)")