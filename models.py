import random


class SlotMachine:
    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1
    ROWS = 3
    COLS = 3

    symbol_count = {
        "A": 8,
        "B": 10,
        "C": 12,
        "D": 14
    }

    symbol_value = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []

        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += self.symbol_value[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines

    def get_slot_machine_spin(self):
        all_symbols = []
        for symbol, count in self.symbol_count.items():
            for _ in range(count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(self.COLS):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.ROWS):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)

            columns.append(column)

        return columns

    def print_slot_machine(self, columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" | ")
                else:
                    print(column[row], end="")
            print()

    def spin(self, lines, bet):
        total_bet = lines * bet

        if total_bet > self.balance:
            return None, None, None, "Нямате достатъчно средства."

        slots = self.get_slot_machine_spin()
        winnings, winning_lines = self.check_winnings(slots, lines, bet)
        self.balance += winnings - total_bet

        return slots, winnings, winning_lines, None

    def get_balance(self):
        return self.balance