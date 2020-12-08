from Model import Model

class User(Model):

    def __init__(self):
        super().__init__("user",["nama","alamat"])

    