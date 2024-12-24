class TopDownParser:
    def __init__(self):
        self.grammar = {}
        self.start_symbol = None

    def input_grammar(self):
        print("\u2B07\u2B07 Grammars \u2B07\u2B07")
        self.grammar = {}
        num_non_terminals = int(input("Enter the number of non-terminals: "))
        for _ in range(num_non_terminals):
            non_terminal = input("Enter non-terminal: ").strip()
            num_rules = int(input(f"Enter the number of rules for non-terminal '{non_terminal}': "))
            rules = [input(f"Enter rule number {i + 1} for non-terminal '{non_terminal}': ").strip() for i in range(num_rules)]
            self.grammar[non_terminal] = rules
        self.start_symbol = input("Enter the start symbol: ").strip()

    def is_simple_grammar(self):
        for non_terminal, rules in self.grammar.items():
            for rule in rules:
                for symbol in rule:
                    if symbol.isupper() and symbol != non_terminal:
                        return False
        return True

    def parse_string(self, string, current_symbol=None):
        if current_symbol is None:
            current_symbol = self.start_symbol

        if not string:
            return not current_symbol

        if current_symbol not in self.grammar:
            return string[0] == current_symbol, string[1:]

        for rule in self.grammar[current_symbol]:
            remaining_string = string
            match = True

            for symbol in rule:
                if match:
                    match, remaining_string = self.parse_string(remaining_string, symbol)
                else:
                    break

            if match:
                return True, remaining_string

        return False, string

    def run(self):
        while True:
            self.input_grammar()

            if not self.is_simple_grammar():
                print("The Grammar isn't simple.\nTry again")
                continue

            print("The Grammar is simple.")

            while True:
                print("==============================")
                print("1-Another Grammar.")
                print("2-Another String.")
                print("3-Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    break
                elif choice == 2:
                    string = input("Enter the string to be checked: ").strip()
                    accepted, remaining = self.parse_string(string)

                    if accepted and not remaining:
                        print("Your input string is Accepted.")
                    else:
                        print("Your input string is Rejected.")
                elif choice == 3:
                    return
                else:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    parser = TopDownParser()
    parser.run()
