class BoundException(Exception):
    def __init__(self, msg, boundaries:tuple, index:int) -> None:
        super().__init__(f"{msg} \n Error in list: {boundaries} in tuple number {index}")