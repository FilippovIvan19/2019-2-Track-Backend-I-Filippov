import unittest


class TestXO(unittest.TestCase):
    def test_win(self):
        f = Field()
        f.set_symbol('X', 1, 3)
        f.set_symbol('X', 2, 2)
        f.set_symbol('X', 3, 1)
        self.assertEqual(f.win_check(), 'X')
        self.assertFalse(f.end_check())

        f = Field()
        f.set_symbol('X', 1, 3)
        f.set_symbol('X', 1, 2)
        f.set_symbol('X', 1, 1)
        self.assertEqual(f.win_check(), 'X')
        self.assertFalse(f.end_check())

        f = Field()
        f.set_symbol('X', 1, 2)
        f.set_symbol('X', 2, 2)
        f.set_symbol('X', 3, 2)
        self.assertEqual(f.win_check(), 'X')
        self.assertFalse(f.end_check())

        f = Field()
        f.set_symbol('O', 1, 3)
        f.set_symbol('O', 2, 2)
        f.set_symbol('O', 3, 1)
        self.assertEqual(f.win_check(), 'O')
        self.assertFalse(f.end_check())

        f = Field()
        f.set_symbol('O', 1, 3)
        f.set_symbol('O', 1, 2)
        f.set_symbol('O', 1, 1)
        self.assertEqual(f.win_check(), 'O')
        self.assertFalse(f.end_check())

        f = Field()
        f.set_symbol('O', 1, 2)
        f.set_symbol('O', 2, 2)
        f.set_symbol('O', 3, 2)
        self.assertEqual(f.win_check(), 'O')
        self.assertFalse(f.end_check())

    def test_symb_from_bool(self):
        self.assertEqual(symb_from_bool(True), 'X')
        self.assertEqual(symb_from_bool(False), 'O')


class Field:
    def __init__(self):
        self.cells = [[' ' for _ in range(3)] for _ in range(3)]

    def set_symbol(self, ch, x, y):
        self.cells[y - 1][x - 1] = ch

    def safe_set_symbol(self, ch):

        while True:
            try:
                x, y = map(
                    int, input(
                        'enter coordinates to place {}: '.format(ch)
                    ).split()
                )
                if (
                    x - 1 not in range(3) or
                    y - 1 not in range(3) or
                    self.cells[y - 1][x - 1] != ' '
                ):
                    raise Exception()
                break
            except Exception:
                print('try again')

        self.set_symbol(ch, x, y)

    def draw_field(self):
        print(' -------------')
        for line in self.cells:
            print('', *line, sep=' | ', end=' | \n')
            print(' -------------')
        print()

    def win_check(self):
        if (
            self.cells[0][0] == self.cells[1][0] == self.cells[2][0] == 'X' or
            self.cells[0][1] == self.cells[1][1] == self.cells[2][1] == 'X' or
            self.cells[0][2] == self.cells[1][2] == self.cells[2][2] == 'X' or

            self.cells[0][0] == self.cells[0][1] == self.cells[0][2] == 'X' or
            self.cells[1][0] == self.cells[1][1] == self.cells[1][2] == 'X' or
            self.cells[2][0] == self.cells[2][1] == self.cells[2][2] == 'X' or

            self.cells[0][0] == self.cells[1][1] == self.cells[2][2] == 'X' or
            self.cells[2][0] == self.cells[1][1] == self.cells[0][2] == 'X'
        ):
            return 'X'

        if (
            self.cells[0][0] == self.cells[1][0] == self.cells[2][0] == 'O' or
            self.cells[0][1] == self.cells[1][1] == self.cells[2][1] == 'O' or
            self.cells[0][2] == self.cells[1][2] == self.cells[2][2] == 'O' or

            self.cells[0][0] == self.cells[0][1] == self.cells[0][2] == 'O' or
            self.cells[1][0] == self.cells[1][1] == self.cells[1][2] == 'O' or
            self.cells[2][0] == self.cells[2][1] == self.cells[2][2] == 'O' or

            self.cells[0][0] == self.cells[1][1] == self.cells[2][2] == 'O' or
            self.cells[2][0] == self.cells[1][1] == self.cells[0][2] == 'O'
        ):
            return 'O'

        return 0

    def end_check(self):
        end = True
        for line in self.cells:
            for symbol in line:
                if symbol == ' ':
                    end = False
        return end


def symb_from_bool(bool_val):
    if bool_val:
        return 'X'
    else:
        return 'O'


f = Field()
cur_bool_symb = True
f.draw_field()
while not f.win_check() and not f.end_check():
    f.safe_set_symbol(symb_from_bool(cur_bool_symb))
    cur_bool_symb = not cur_bool_symb
    f.draw_field()
result = f.win_check()
if not result:
    print('draw!')
else:
    print('{} win!'.format(result))

if __name__ == '__main__':
    unittest.main()
