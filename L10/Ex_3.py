class Cell:
    cells: int

    def __init__(self, cells: int) -> None:
        self.cells = cells

    def __add__(self, other: 'Cell'):
        return Cell(self.get_size() + other.get_size())

    def __sub__(self, other: 'Cell'):
        if self.get_size() < other.get_size():
            raise ValueError("Cells can't be < 0")

        return Cell(self.get_size() - other.get_size())

    def __mul__(self, other: 'Cell'):
        return Cell(self.get_size() * other.get_size())

    def __floordiv__(self, other: 'Cell'):
        return Cell(self.get_size() // other.get_size())

    def get_cells(self) -> str:
        return str(self).replace("Cell(", "").replace(")", "")

    def get_size(self) -> int:
        return self.get_cells().count("*")

    def __str__(self) -> str:
        return f"Cell({'*'*self.cells})"

    def make_order(self, split_cell) -> str:
        '''Ordering cells to cube the size eq split_cell*split_cell'''
        if split_cell == 0:
            raise ValueError("can't split cells by 0")

        if split_cell >= self.get_size():
            return self.get_cells()

        size = self.get_size()

        return "".join([f"{x}\n" if i % split_cell == 0 and i != size else x
                        for i, x in enumerate(self.get_cells(), start=1)])