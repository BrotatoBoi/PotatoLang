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
        self.__version__ = "V0.2.0"


    def set_var(self, varName, varType, value):
        if varType == "number":
            value = int(value)
        elif varType == "decimal":
            value = float(value)
        elif varType == "yes/no":
            if value == "yes":
                value = True
            elif value == "no":
                value = False
            else:
                print(f"ERROR ON: {value}")

        elif varType == "words":
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
            if word in self.variables and not inString:
                if self.variables[word] == True:
                    output += 'yes '
                elif self.variables[word] == False:
                    output += 'no '
                else:
                    output += str(self.variables[word])+' '
            else:
                for char in word:
                    if char == '"':
                        inString = not inString
                    elif inString:
                        output += str(char)

                output += ' '

        print(output)


    def if_statement(self, statement):
        statementIndex = 0
        condition = []
        ifBlock = []
        elseBlock = []
        
        for word in statement:
            if word == 'then':
                statementIndex = statement.index(word)+1
                break
            else:
                condition.append(word)

        ib = []
        for word in statement[statementIndex:]:
            if word == 'else':
                statementIndex = statement.index(word)+1
                break
            else:
                if word == ";":
                    ifBlock.append(ib)
                    ib = []
                else:
                    ib.append(word)
        ifBlock.append(ib)

        eb = []
        for word in statement[statementIndex:]:
            if word == ';':
                elseBlock.append(eb)
                eb = []
            else:
                eb.append(word)
        elseBlock.append(eb)

        var1 = condition[0]
        operator = condition[1]
        var2 = condition[2]

        if operator == 'equals':
            if self.variables[var1] == self.variables[var2]:
                for line in ifBlock:
                    self.proc_line(line)
            else:
                for line in elseBlock:
                    self.proc_line(line)

    def what_are(self, words):
        keywords = {"say": "outputs some text: say [MESSAGE]",
                    "set": "sets a variable to a value: set [VAR_NAME] [VAR_TYPE] [VAR_VALUE]",
                    "get": "gets a variable: get [VAR_NAME] [MESSAGE]",
                    "clean": "clears the screen: clear",
                    "if": "Checks conditions: if [CONDITION] then [CODE]",
                    "whats": "shows you what these words are, Y'know... this!"}

        operators = {"equals": "checks if two variables equal each other."}

        other = {"$": "conversation starter! Well, it just starts a comment... (Make sure to add a space after it)",
                 ";": "line ender (Add a space before + after it and only useful in if/else)",
                 "then": "word that stops checking conditions and run the code up until the 'else' word",
                 "else": "word that works with if and cannot exist without it, it runs the rest of the line.",
                 "yes": "True statement, On switch, 1 binary, e.g.",
                 "no": "False statement, Off switch, 0 binary, e.g."} 

        for word in words:
            if word in self.variables:
                varType = type(self.variables[word])

                if varType == int:
                    varType = "number"
                
                elif varType == float:
                    varType = "decimal"

                elif varType == bool:
                    varType = "yes/no"

                elif varType == str:
                    varType = "buncha words"

                print(f"{word} is a {varType} with the value of {self.variables[word]}")
            
            elif word in keywords:
                print(f"{keywords[word]} is a keyword that {keywords.get(word)}")

            elif word in operators:
                print(f"{operators[word]} is an operator that {operators.get(word)}")

            elif word in other:
                print(f"{other[word]} is a {other.get(word)}")

            else:
                print(f"{word} is not a keyword, operator, variable or anything else!")    

    def proc_line(self, line):
            if line:
                if line[0] == '$':
                    pass
                elif line[0] == 'say':
                    self.say(line[1:])
                        
                elif line[0] == 'set':
                    self.set_var(line[1], line[2], line[3])

                elif line[0] == 'get':
                    self.get_var(line[1], line[2:])
                        
                elif line[0] == 'clean':
                    os.system('clear' if os.name == 'posix' else 'cls')

                elif line[0] == 'if':
                    self.if_statement(line[1:])

                elif line[0] == 'whats':
                    self.what_are(line[1:])

                elif line[0] == "version":
                    print(f"Version: {self.__version__}")
                           
                else:
                    print(f"ERROR ON: {line}")
            else:
                pass


    def run(self, file):
        print(f"Starting up file {file}")

        with open(file, 'r') as f:
            for line in f:
                self.proc_line(line.split())

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

