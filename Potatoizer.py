# ~~ -------------------------------------------------------- ~~ #
# ~~ --------  Programmer: AJ Cassell (@BrotatoBoi). -------- ~~ #
# ~~ --------------- Program Name: Potatoizer --------------- ~~ #
# ~~ ---------------- Date: December/08/2021. --------------- ~~ #
# ~~ ------- Description: Interpreter for my Language. ------ ~~ #
# ~~ ------------------- Version: 0.2.2R2. ------------------ ~~ #
# ~~ -------------------------------------------------------- ~~ #


# ~ Inport Necessary Modules ~ #
from os import system, name
from os.path import dirname, join


# ~ Interpreter Class. ~ #
class Potatoizer:
    """
        The Interpreter takes a file and runs it line by line in PotatoLang.

        Functions:
            __init__ : Initialize the Interpreter.
            say : Outputs a message.
            set_var : Sets a variable to a value.
            get_var : Gets a variable.
            whats : Shows what a word is.
            if_else : Checks if a condition is true or false.
            check_condition : Process condition from if_else.
            run_block : Runs a block of code.
            create_block : Creates a block of code.
            parse_string : Parses a string.
            process_line : Processes a line.
            potatoize : Runs the file.
    """
    
    # ~ Initialize the Interpreter. ~ #
    def __init__(self, file):
        """
            Initializes the Interpreter.

            Parameters:
                file : The file to run.

            Variables:
                self.__version__ : The version of the Interpreter.
                self.cwd : The current working directory.
                self.filePath : The path to the file.
                self.info : The information of the file.
                self.file : The file to run.

            Logic:
                Create the Variables.
                Try to set the file if it exists, Otherwise exit.
        """
        
        # ~ Create the Variables. ~ #
        self.__version__ = "V0.2.2R2"
        self.cwd = dirname(__file__)
        self.filePath = join(self.cwd, file)
        self.info = {
            "keywords": {
                "say": "outputs some text: say [MESSAGE]", 
                "set": "sets a variable to a value: set [VAR_NAME] [VAR_TYPE] [VAR_VALUE]", 
                "get": "gets a variable: get [VAR_NAME] [MESSAGE]", 
                "clean": "clears the screen: clear", 
                "if": "Checks conditions: if [CONDITION] then [CODE]", 
                "whats": "shows you what these words are, Y'know... this!", 
                "version": "shows the version of the interpreter: version"
            }, 
            "operators": {
                "equals": "checks if two variables equal each other.",
                "is-not": "checks if two variables are not equal to each other.",
                "greater-than": "checks if one variable is greater than another.",
                "less-than": "checks if one variable is less than another."
            }, 
            "others": {
                "$": "conversation starter! Well, it just starts a comment... (Make sure to add a space after it)",
                ";": "line ender (Add a space before + after it and only useful in if/else)",
                "then": "word that stops checking conditions and run the code up until the 'else' word",
                "else": "word that works with if and cannot exist without it, it runs the rest of the line.",
                "yes": "True statement, On switch, 1 binary, e.g.",
                "no": "False statement, Off switch, 0 binary, e.g."
            },
            "variables": {}
        }

        # ~ Try to set the file if it exists, Otherwise exit. ~ #
        try:
            self.file = open(self.filePath)
        except FileNotFoundError:
            print(f"The file {self.filePath} was not found!")

    # ~ Outputs a message. ~ #
    def say(self, message):
        """
            Outputs a message.

            Parameters:
                message : The message to output.

            Variables:
                output : The message parsed as a string.

            Logic:
                Parse the message.
                Print the message.
        """
        
        # ~ Parse the message. ~ #
        output = self.parse_string(message)

        # ~ Print the message. ~ #
        print(output)

    # ~ Sets a variable to a value. ~ #
    def set_var(self, varName, varType, varValue):
        """
            Sets a variable to a value.

            Parameters:
                varName : The name of the variable.
                varType : The type of the variable.
                varValue : The value of the variable.

            Logic:
                Check what type the variable is and correct it.
                Set the variable to the right variable.
        """
        
        # ~ Check what type the variable is and correct it. ~ #
        if varType == "words":
            varValue = self.parse_string(varValue)
        elif varType == "number":
            varValue = int(varValue[0])
        elif varType == "yes/no":
            if varValue[0] == "yes":
                varValue = True
            elif varValue[0] == "no":
                varValue = False
            else:
                print("Error: Invalid value for yes/no variable.")
                exit()

        elif varType == "decimal":
            varValue = float(varValue[0])
        else:
            print("Error: Invalid variable type: {varType}")
            exit()

        # ~ Set the variable to the right variable. ~ #
        self.info["variables"][varName] = varValue

    def get_var(self, varName, message):
        """
            Gets a variable.

            Parameters:
                varName : The name of the variable.
                message : The message to prompt the user.

            Variables:
                message : The message parsed as a string.

            Logic:
                Parse the message.
                Check if the variable exists.
                Print the message as a prompt and get the variable.
        """
        
        # ~ Parse the message. ~ #
        message = self.parse_string(message)

        # ~ Check if the variable exists. ~ #
        if varName not in self.info["variables"]:
            print(f"Error: Variable {varName} does not exist.")
            exit()

        # ~ Print the message as a prompt and get the variable. ~ #
        self.info["variables"][varName] = input(f"{message}")
            

    # ~ Shows what the words are. ~ #
    def whats(self, words):
        """
            Shows what the words are.

            Parameters:
                words : The words to show.

            Variables:
                word : The word to show in words.
                info : The information of the word.

            Logic:
                Loop through the words.
                Check if the word is a keyword, operator, other or a variable and print what it is.
        """
        
        # ~ Loop through the words. ~ #
        for word in words:
            # ~ Check if the word is a keyword, operator, other or a variable and print what it is. ~ #
            if word in self.info["keywords"]:
                print(self.info["keywords"][word])

            elif word in self.info["operators"]:
                print(self.info["operators"][word])

            elif word in self.info["others"]:
                print(self.info["others"][word])

            elif word in self.info["variables"]:
                value = self.info["variables"][word]

                varType = type(value)

                if varType == str:
                    varType = "some words"
                elif varType == int:
                    varType = "a number"
                elif varType == bool:
                    varType = "yes/no"

                    if value:
                        value = "yes"
                    else:
                        value = "no"

                elif varType == float:
                    varType = "a decimal"
                else:
                    varType = "unknown"

                print(f"{word} is {varType} and has the value of: {value}")

            else:
                print(f"Sorry I dont know what {word} is.")

    def if_else(self, line):
        """
            Process an if/else statement.

            Parameters:
                line : The line to process.

            Variables:
                condition : The condition to check.
                ifBlock : The code to run if the condition is true.
                elseBlock : The code to run if the condition is false.

            Logic:
                Create variables, for the condition, ifBlock and elseBlock.
                Check the condition, if it is true, run the ifBlock, otherwise run the elseBlock.
        """
        
        # ~ Create variables, for the condition, ifBlock and elseBlock. ~ #
        condition = [word for word in line[:line.index("then")]]
        ifBlock = self.create_block(line[line.index("then")+1:line.index("else")])
        elseBlock = self.create_block(line[line.index("else")+1:])
        
        # ~ Check the condition, if it is true, run the ifBlock, otherwise run the elseBlock. ~ #
        if self.check_condition(condition):
            self.run_block(ifBlock)
            pass
        else:
            if elseBlock:
                self.run_block(elseBlock)
                pass

    # ~ Run a code block. ~ #
    def run_block(self, block):
        """
            Run a block of code.

            Parameters:
                block : The block of code to run.

            Variables:
                line : The line to process.
                index : The index of the line.

            Logic:
                Loop through the lines.
                Process the line.
        """
        
        # ~ Loop through the lines. ~ #
        for index, line in enumerate(block):
            # ~ Process the line. ~ #
            self.process_line(index, line)

    # ~ Create a block of code. ~ #
    def create_block(self, line):
        """
            Create a block of code.

            Parameters:
                line : The line to process.

            Variables:
                block : The block of code.
                temp : The temporary block of code.

            Logic:
                Create variables, for the block and temp.
                Loop through each word in the line.
                If the word is a delimiter ';' add the temp array to the block.
                Otherwise, add the word to the temp array.
                Add the temp array to the block.
                Return the block.
        """
        
        # ~ Create variables, for the block and temp. ~ #
        temp = []
        block = []

        # ~ Loop through each word in the line. ~ #
        for word in line:
            # ~ If the word is a delimiter ';' add the temp array to the block. ~ #
            if word == ";":
                block.append(temp)
                temp = []
            # ~ Otherwise, add the word to the temp array. ~ #
            else:
                temp.append(word)

        # ~ Add the temp array to the block. ~ #
        block.append(temp)

        # ~ Return the block. ~ #
        return block
        
    # ~ Check if the condition is true. ~ #
    def check_condition(self, condition):
        """
            Check if the condition is true.

            Parameters:
                condition : The condition to check.

            Variables:
                var1 : The first variable.
                operator : The operator.
                var2 : The second variable.

            Logic:
                Create variables, for the var1, operator and var2.
                Check if the variables exist.
                If so, get their values.
                Compare availables based on the operator.
        """
        
        # ~ Create variables, for the var1, operator and var2. ~ #
        var1 = condition[0]
        operator = condition[1]
        var2 = condition[2]

        # ~ Check if the variables exist. ~ #
        if var1 in self.info["variables"] and var2 in self.info["variables"]:
            # ~ If so, get their values. ~ #
            var1 = self.info["variables"][var1]
            var2 = self.info["variables"][var2]

            # ~ Compare availables based on the operator. ~ #
            if operator == "equals":
                return var1 == var2
            elif operator == "is-not":
                return var1 != var2
            elif operator == "greater-than":
                return var1 > var2
            elif operator == "less-than":
                return var1 < var2
            else:
                print("Error: Invalid operator.")
                exit()

        else:
            print("Error: Invalid variable.")
            exit()

    # ~ Parse a message into a string. ~ #
    def parse_string(self, message):
        """
            Parse a message into a string.

            Parameters:
                message : The message to parse.

            Variables:
                inString : Whether or not the message is in a string.
                output : The output string.

            Logic:
                Create variables, for the inString and output.
                Loop through each word.
                Check if the word is a variable and not in a string, if so, add it's value to output.
                Otherwise, loop through each character.
                If the character is a double quote toggle inString and continue.
                Add the character to output.
                Add space when necessary.
                Return the output.
        """

        # ~ Create variables, for the inString and output. ~ #
        inString = False
        output = ""

        # ~ Loop through each word. ~ #
        for word in message:
            # ~ Check if the word is a variable and not in a string, if so, add it's value to output. ~ #
            if word in self.info["variables"] and not inString:
                output += str(self.info["variables"][word])
            else:
                # ~ Otherwise, loop through each character. ~ #
                for char in word:
                    # ~ If the character is a double quote toggle inString and continue. ~ #
                    if char == "\"":
                        inString = not inString
                        continue

                    # ~ Add the character to output. ~ #
                    output += char

                # ~ Add space when necessary. ~ #
                if message.index(word) != len(message)-1 or len(message) != 1:
                    output+=" "

        # ~ Return the output. ~ #
        return output

    # ~ Process a line of code. ~ #
    def process_line(self, index, line):
        """
            Process a line of code.

            Parameters:
                index : The index of the line.
                line : The line to process.

            Logic:
                Check if the line has content.
                If so, check the content.
                If the line starts with $ (shh) ignore it.
                If the line starts with set, set the variable.
                If the line styarts with get, get the variable.
                If the line starts with say, say the message.
                If the line starts with wash, clear the screen.
                If the line starts with if, process an if/else statement.
                If the line starts with whats, print what the words mean.
                If the line starts with version, show the Interpreter version.
        """
        
        # ~ Check if the line has content. ~ #
        if line[0] != '':
            # ~ Comment. ~ #
            if line[0] == "$":
                pass

            # ~ Say a message. ~ #
            elif line[0] == "say":
                self.say(line[1:],)
            
            # ~ Set a variable. ~ #
            elif line[0] == "set":
                self.set_var(line[1], line[2], line[3:])
            
            # ~ Get a variable. ~ #
            elif line[0] == "get":
                self.get_var(line[1], line[2:])
            
            # ~ Clear the screen. ~ #
            elif line[0] == "wash":
                system("clear" if name == "posix" else "cls")
            
            # ~ If statement. ~ #
            elif line[0] == "if":
                self.if_else(line[1:])
            
            # ~ What's the meaning of the word? ~ #
            elif line[0] == "whats":
                self.whats(line[1:])
            
            # ~ Show the version. ~ #
            elif line[0] == "version":
                print(self.__version__)
            
            # ~ Invalid command. ~ #
            else:
                print(f"Error on Line {index}: {line}")
                exit()
        else:
            pass


    # ~ Run a potato file. ~ #
    def potatoize(self):
        """
            Run a potato file.

            Variables:
                file : The file to run.
                index : The index of the line.
                line : The line to process.

            Logic:
                With the potato file, process each line.
        """
        
        # ~ With the potato file, process each line. ~ #
        with self.file as file:
            for index, line in enumerate(file):
                self.process_line(index+1, line.replace('\n', '').split(" "))
                