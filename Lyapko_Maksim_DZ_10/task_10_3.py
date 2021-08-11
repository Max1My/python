class Cell:
    def __init__(self,count_1):
        self.count_1 = int(count_1)
    def __add__(self, other):
        return Cell(self.count_1 + other.count_1)
    def __sub__(self,other):
        result_of_sub = self.count_1 - other.count_1
        if result_of_sub > 0:
            return Cell(result_of_sub)
        else:
            return f"Разница меньше нуля"
    def __mul__(self, other):
        return Cell(self.count_1 * other.count_1)
    def __floordiv__(self, other):
        return Cell(self.count_1 // other.count_1)
    def __truediv__(self, other):
        return Cell(self.count_1 / other.count_1)
    def __str__(self):
        return f"{self.count_1} cells long"
    def make_order(self,amount_of_cells_in_row):
        rows_amount, add_to_last_row = \
            divmod(self.count_1, amount_of_cells_in_row)

        cell_as_string = ''
        for _ in range(rows_amount):
            cell_as_string += f'{"*" * amount_of_cells_in_row}\n'

        return cell_as_string.rstrip() + '*' * add_to_last_row

if __name__ == '__main__':
    count_1 = Cell(54)
    count_2 = Cell(32)
    count_cell_add = count_1 + count_2
    print(count_cell_add)
    count_cell_sub = count_1 - count_2
    print(count_cell_sub)
    count_cell = count_1 * count_2
    print(count_cell)
    count_cell_div = count_1 // count_2
    print(count_cell_div)
    print(count_1 / count_2)
    print(count_cell_add.make_order(10))
    print(count_cell_sub.make_order(3))
    print(count_cell_div.make_order(5))
