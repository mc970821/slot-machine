from models import SlotMachine


def get_deposit():
    while True:
        amount = input("Каква сума искате да внесете? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Сумата трябва да е по-голяма от 0.")
        else:
            print("Моля, въведете число.")


def get_number_of_lines(machine):
    while True:
        lines = input(f"На колко линии искате да залагате (1-{machine.MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= machine.MAX_LINES:
                return lines
            else:
                print("Въведете валиден брой линии.")
        else:
            print("Моля, въведете число.")


def get_bet(machine):
    while True:
        amount = input(f"Каква сума искате да заложите на всяка линия (между ${machine.MIN_BET} и ${machine.MAX_BET})? $")
        if amount.isdigit():
            amount = int(amount)
            if machine.MIN_BET <= amount <= machine.MAX_BET:
                return amount
            else:
                print(f"Сумата трябва да е между ${machine.MIN_BET} и ${machine.MAX_BET}!")
        else:
            print("Моля, въведете число.")


def main():
    machine = SlotMachine()

    deposit_amount = get_deposit() 
    machine.deposit(deposit_amount)

    while True:
        print(f"\nТекущ баланс: ${machine.get_balance()}")

        if machine.get_balance() < machine.MIN_BET:
            print("Балансът ви е недостатъчен за игра.")
            answer = input("Искате ли да направите нов депозит? Изберете y(за да) или n(за не): ")

            if answer.lower() == "y":
                deposit_amount = get_deposit()
                machine.deposit(deposit_amount)
                continue
            else:
                break
        answer = input("Изберете: p (за игра), d (за депозит), q (за изход): ")

        if answer.lower() == "q":
            break

        elif answer.lower() == "d":
            deposit_amount = get_deposit()
            machine.deposit(deposit_amount)
            continue

        elif answer.lower() != "p":
            print("Невалиден избор.")
            continue

        lines = get_number_of_lines(machine)

        if lines * machine.MIN_BET > machine.get_balance():
            print("Нямате достатъчно баланс за този брой линии.")
            continue

        while True:
            bet = get_bet(machine)
            total_bet = lines * bet

            if total_bet > machine.get_balance():
                print(f"Нямате достатъчно пари. Вашият баланс е ${machine.get_balance()}.")
            else:
                break

        print(f"Залагате ${bet} на {lines} линии. Обща сума на залога: ${total_bet}")

        slots, winnings, winning_lines, error = machine.spin(lines, bet)

        if error:
            print(error)
            continue

        machine.print_slot_machine(slots)
        print(f"Спечелихте: ${winnings}")

        if winning_lines:
            print("Печеливша линия:", *winning_lines)
        else:
            print("Няма печеливши линии.")

    print(f"\nНапуснахте играта с ${machine.get_balance()}")


if __name__ == "__main__":
    main()
