# ~~ ------------------------------------------------ ~~ #
# ~~ ----- Programmer: AJ Cassell (@BrotatoBoi) ----- ~~ #
# ~~ --------- Program Name: Interpre-tato. --------- ~~ #
# ~~ ----------- Date: November/14/2021. ------------ ~~ #
# ~~ - Description: My potato language interpreter. - ~~ #
# ~~ ------------------------------------------------ ~~ #


import os


class Interpreter:
    def __init__(self):
        self.variables = {}

    def set_var(self, varName, varType, value):
        if varType == "number":
            value = int(value)
        elif varType == "decimal":
            value = float(value)
        elif varType == "bool":
            value = bool(value)
        elif varType == "string":
            value = str(value)

        self.variables[varName] = value

    def get_var(self, varName, message=""):
        message+=" "
        if varName in self.variables:
            self.variables[varName] = input(' '.join(message))
        else:
            print(f"ERROR NO VARIABLE NAMED: {varName}")

    def say(self, message):
        inString = False
        output = ''

        for word in message:
            if word in self.variables:
                output += self.variables[word]
            else:
                for char in word:
                    if char == '"':
                        inString = not inString
                    elif inString:
                        output += char

                output += ' '

        print(output)

    def run(self, file):
        print(f"Starting up file {file}")

        os.system('clear' if os.name == 'posix' else 'cls')

        with open(file, 'r') as f:
            for line in f:
                if line.startswith('$'):
                    continue

                else:
                    line = line.split()

                    if line:
                        if line[0] == 'say':
                            self.say(line[1:])
                        
                        elif line[0] == 'set':
                            self.set_var(line[1], line[2], line[3])

                        elif line[0] == 'get':
                            self.get_var(line[1], line[2:])

                        else:
                            print(f"ERROR ON: {line}")


class Main:
    def __init__(self):
        self.interpreter = Interpreter()
        self._isRunning = True

        self.execute()

    def proc_command(self, command):
        if command == "exit":
            self._isRunning = False

        elif command.startswith("run"):
            file = command.split(" ")[1]
            self.interpreter.run(file)

        elif command == "help":
            print("""
            Commands:
            run <file> - Run a potato file.
            exit - Exit the interpreter.
            help - Show this help message.
            """)
        
        else:
            print("Invalid command!")

    def execute(self):
        while self._isRunning:
            cmd = input(">> ")

            self.proc_command(cmd)


if __name__ == "__main__":
    Main()

