class WanException(Exception):

    def __init__(self):
        super().__init__("Nó wan já foi adicionado e não pode ser adicionado novamente.")