# ~~ ------------------------------------------------ ~~ #
# ~~ ----- Programmer: AJ Cassell (@BrotatoBoi) ----- ~~ #
# ~~ --------- Program Name: Interpre-tato. --------- ~~ #
# ~~ ----------- Date: November/14/2021. ------------ ~~ #
# ~~ - Description: My potato language interpreter. - ~~ #
# ~~ ---------------- Version: 0.2.0R1 -------------- ~~ #
# ~~ ------------------------------------------------ ~~ #


# ~ Import Needed Modules ~ #
import os


# ~ Interpreter Class. ~ #
class Interpreter:
    """
        The Interpreter Class.

        Functions:
            __init__: Initialize the Class.
            set_var: Set a variable.
            get_var: Get a user input.
            say: Print output to the screen.
            if_else: If statement.
            what_are: Check what the words are.
            proc_line: Process the line of code.
            run: Run a .pot file.
    """

    # ~ Initialize the Class. ~ #
    def __init__(self):
        """
            Initialize the Class.

            Variables:
                self.variables: The programs variables.
                self.__version__: The interpreter version.

            Logic:
                Create variables.
        """

        # ~ Create variables. ~ #
        self.variables = {}
        self.__version__ = "V0.2.0R1"
        self.keywords = {"say": "outputs some text: say [MESSAGE]",
                         "set": "sets a variable to a value: set [VAR_NAME] [VAR_TYPE] [VAR_VALUE]",
                         "get": "gets a variable: get [VAR_NAME] [MESSAGE]",
                         "clean": "clears the screen: clear",
                         "if": "Checks conditions: if [CONDITION] then [CODE]",
                         "whats": "shows you what these words are, Y'know... this!",
                         "version": "shows the version of the interpreter: version"
                        }

        self.operators = {"equals": "checks if two variables equal each other.",
                          "is-not": "checks if two variables are not equal to each other.",
                          "greater-than": "checks if one variable is greater than another.",
                          "less-than": "checks if one variable is less than another.",
                         }

        self.other = {"$": "conversation starter! Well, it just starts a comment... (Make sure to add a space after it)",
                      ";": "line ender (Add a space before + after it and only useful in if/else)",
                      "then": "word that stops checking conditions and run the code up until the 'else' word",
                      "else": "word that works with if and cannot exist without it, it runs the rest of the line.",
                      "yes": "True statement, On switch, 1 binary, e.g.",
                      "no": "False statement, Off switch, 0 binary, e.g."
                     }

    # ~ Set a variable. ~ #
    def set_var(self, varName, varType, value):
        """
            Set a variable.

            Parameters:
                varName: The name of the variable.
                varType: The type of the variable.
                value: The value of the variable.

            Logic:
                Check the type of the variable.
                Set the value to the correct type.
                Add the variable and value to self->variables.
        """

        # ~ Check the variable type. ~ #
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
                print("ERROR: Invalid value for yes/no.")
                return
        elif varType == "words":
            value = str(value)

        # ~ Set the value to the correct type. ~ #
        self.variables[varName] = value

    # ~ Get user input. ~ #
    def get_var(self, varName, message=""):
        """
            Get user input.

            Parameters:
                varName: The name of the variable.
                message: The message to print.

            Logic:
                Add a space to the end of the message for formatting and set it to a string.
                Check if the variable exists.
                If it does, get the user input.
                If it doesn't, print an error.
        """

        # ~ Add a space to the end of the message for formatting and set it to a string. ~ #
        message = " ".join(message+" ")

        # ~ Check if the variable exists. ~ #
        if varName in self.variables:
            self.variables[varName] = input(message)
        else:
            print(f"ERROR: No variable named {varName}.")

    # ~ Say something. ~ #
    def say(self, message):
        """
            Print output to the screen.

            Parameters:
                message: The message to print.

            Variables:
                inString: Check if it's in a string.
                output: The output to print.

            Logic:
                Create variables.
                Loop through the message.
                Check if the word is a variable.
                If it is, check if it's a boolean.
                If it is, print the correct value.
                If it isn't, print the word.
                If it is not a variable, loop through the word.
                Check if it is a quote.
                If it is set inString to the right value.
        """

        # ~ Create variables. ~ #
        inString = False
        output = ''

        # ~ Loop through the message. ~ #
        for word in message:
            if word in self.variables and not inString:
                if self.variables[word] == True:
                    output += 'yes '
                elif self.variables[word] == False:
                    output += 'no '
                else:
                    output += str(self.variables[word])+' '
            else:
                # ~ Loop through the word. ~ #
                for char in word:
                    if char == '"':
                        inString = not inString
                    elif inString:
                        output += str(char)

                output += ' '

        # ~ Print the output. ~ #
        print(output)

    # ~ If statement. ~ #
    def if_else(self, statement):
        """
            Process the if statement.

            Parameters:
                statement: The statement to process.

            Variables:
                statementIndex: The current index of the word.
                condition: The condition to process.
                ifBlock: The if code to call when condition is satisfied.
                elseBlock: The else code to call when condition is not satisfied.
                temp: A temporary list for if/elseBlocks.

            Logic:
                Create variables.
                Loop through each word in the statement.
                If the word is then, set the current index and break.
                Otherwise, add the word to condition list.
                Loop through each word in the statement at the index.
                If the word is else, set the current index and break.
                Otherwise, check if the word is a line seperator. (;)
                If so, add the temporary list to the ifBlock and clear the temporary list.
                Otherwise, add the word to the temporary list.
                Create condition variables.
                Check if the operator exists.
                If so do the if/else statement.


                THIS FUNCTION CAN BE CLEANED UP A BIT.  
        """

        # ~ Create Variables. ~ #
        statementIndex = 0
        condition = []
        ifBlock = []
        elseBlock = []
        temp = []

        # ~ Loop through each word in the statement. ~ #
        for word in statement:
            # ~ If the word is then, set the current index and break. ~ #
            if word == "then":
                statementIndex = statement.index(word)
                break

            # ~ Otherwise, add the word to condition list. ~ #
            else:
                condition.append(word)

        # ~ Loop through the if code. ~ #
        for word in statement[statementIndex+1:]:
            # ~ If the word is else, set the current index and break. ~ #
            if word == "else":
                statementIndex = statement.index(word)
                break

            # ~ Otherwise, check if the word is a line seperator. (;) ~ #
            elif word == ";":
                # ~ If so, add the temporary list to the ifBlock and clear the temporary list. ~ #
                ifBlock.append(temp)
                temp = []

            # ~ Otherwise, add the word to the temporary list. ~ #
            else:
                temp.append(word)

        # ~ Loop through the else code. ~ #
        for word in statement[statementIndex+1:]:
            # ~ If the word is a line seperator, add the temporary list to the elseBlock and clear the temporary list. ~ #
            if word == ";":
                elseBlock.append(temp)
                temp = []

            # ~ Otherwise, add the word to the temporary list. ~ #
            else:
                temp.append(word)

        # ~ Create condition variables. ~ #
        var1 = condition[0]
        operator = condition[1]
        var2 = condition[2]

        # ~ Check if the operator exists. ~ #
        if operator == "equals":
            if self.variables[var1] == self.variables[var2]:
                for line in ifBlock:
                    self.proc_line(line)
            else:
                for line in elseBlock:
                    self.proc_line(line)

        elif operator == "is-not":
            if self.variables[var1] != self.variables[var2]:
                for line in ifBlock:
                    self.proc_line(line)

            else:
                for line in elseBlock:
                    self.proc_line(line)
                
        elif operator == "greater-than":
            if self.variables[var1] > self.variables[var2]:
                for line in ifBlock:
                    self.proc_line(line)

            else:
                for line in elseBlock:
                    self.proc_line(line)

        elif operator == "less-than":
            if self.variables[var1] < self.variables[var2]:
                for line in ifBlock:
                    self.proc_line(line)

            else:
                for line in elseBlock:
                    self.proc_line(line)

        
    # ~ Check what is the word. ~ #
    def what_is(self, words):
        """
            Check what the word is.

            Parameters:
                words: The words to check

            Variables:
                varType: The type of the variable.

            Logic:
                Loop through each of the words.
                Check if the word is a variable.
                Get the type of the variable and potato-ize it!
                Print the word, type and value of the variable.
                If it is not a variable, check if it is either a keyword, operator, or other known word.
                If it is, print the word and description.
                Otherwise, print it is unknown.
        """

        # ~ Loop through each of the words. ~ #
        for word in words:
            # ~ Check if the word is a variable. ~ #
            if word in self.variables:
                # ~ Get the type of the variable. ~ #
                varType = type(self.variables[word])

                # ~ Potato-ize it! ~ #
                if varType == bool:
                    varType = "yes/no"

                elif varType == int:
                    varType = "number"

                elif varType == str:
                    varType = "buncha words"

                elif varType == float:
                    varType = "decimal"

                # ~ Print the word, type and value of the variable. ~ #
                print(f"{word} is a {varType} with the value of {self.variable[word]}")

            # ~ Check if it is either a keyword, operator, or other known word. ~ #
            elif word in self.keywords:
                print(f"{word} is a {self.keywords[word]}")

            elif word in self.operators:
                print(f"{word} is an {self.operators[word]}")

            elif word in self.other:
                print(f"{word} is {self.other[word]}")

            # ~ Otherwise, print it is unknown. ~ #
            else:
                print(f"{word} is unknown")

    # ~ Process the line. ~ #
    def proc_line(self, line):
        """
            Process the line of code.

            Parameters:
                line: The line of code to process.

            Logic:
                Check if the line is not empty.
                If not empty check the first found word.
                If the word is '$' ignore it (Comment).
                If the word is 'say' process the rest of the line as a string and print it.
                If the word is 'set' create a variable with a name, type and value.
                If the word is 'get' set the user input to the variable name with the rest of the line processed as a string for a message.
                If the word is 'clean' clear the screen.
                If the word is 'if' process the rest of the line as an if/else.
                If the word is 'whats' return information about the following words.
                If the word is 'version' return the print of the Interpreter.
                Otherise, throw an error.
        """

        if line:
            if line[0] == '$':
                pass

            elif line[0] == 'say':
                print(line[1:])

            elif line[0] == 'set':
                self.set_var(line[1], line[2], line[3:])

            elif line[0] == 'get':
                self.get_var(line[1], line[2:])

            elif line[0] == 'clean':
                os.system('clear' if os.name == 'posix' else 'cls')

            elif line[0] == 'if':
                self.if_else(line[1:])

            elif line[0] == 'whats':
                self.what_is(line[1:])

            elif line[0] == 'version':
                print(f"Version: {self.version}")
            
            else:
                print(f"Error: {line} is not a valid command.")

    # ~ Run the program. ~ #
    def run(self, file):
        """
            Run a potato file.

            Parameters:
                file: The file to run.

            Logic:
                Check if the file exists.
                If it does, open the file and read the lines.
                Loop through the lines.
                Process the line.
                Close the file.
        """

        # ~ Check if the file exists. ~ #
        if os.path.exists(file):
            # ~ Open the file and read the lines. ~ #
            with open(file) as f:
                lines = f.readlines()

            # ~ Loop through the lines. ~ #
            for line in lines:
                # ~ Process the line. ~ #
                self.proc_line(line)

        # ~ If the file does not exist, throw an error. ~ #
        else:
            print(f"Error: {file} does not exist.")


# ~ Main Class. ~ #
class Main:
    """
        Main Class.

        Functions:
            __init__: Initialize the Interpreter.
            proc_command: Process the givin command.
            execute: Execute the Interpreter.
    """

    def __init__(self):
        """
            Initialize the main class.

            Variables:
                self.interpreter: The Interpreter.
                self._isRunning: Whether the program is running.

            Logic:
                Create variables.
                Call the main loop.
        """

        # ~ Create variables. ~ #
        self.interpreter = Interpreter()
        self._isRunning = True

        # ~ Call the main loop. ~ #
        self.execute()

    # ~ Process the givin command
    def proc_command(self, command):
        """
            Process the givin command.

            Parameters:
                command: The command to process.

            Logic:
                If the command is 'exit' stop the Interpreter.
                If it starts with 'run', get the file name and run it in the interpreter.
                If the command is 'help' show the commmands.
                Otherwise, tell user that was invalid.
        """

        # ~ If the command is 'exit' stop the Interpreter. ~ #
        if command == 'exit':
            self._isRunning = False

        # ~ If it starts with 'run', get the file name and run it in the interpreter. ~ #
        elif command.startswith('run'):
            file = command[.split(" ")[1]
            self.interpreter.run(file)

        # ~ If the command is 'help' show the commands. ~ #
        elif command == 'help':
            print("""
                Commands:
                    exit: Stop the program.
                    run <file>: Run a file.
                    help: Show this help.
            """)

        # ~ Otherwise, tell user that was invalid. ~ #
        else:
            print(f"Error: {command} is not a valid command.")


# ~ Check if it is the main file. ~ #
if __name__ == '__main__':
    Main()
