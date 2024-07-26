class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        raise NotImplementedError(f"derived classes need to override this method")