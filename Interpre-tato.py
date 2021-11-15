# ~~ ------------------------------------------------ ~~ #
# ~~ ----- Programmer: AJ Cassell (@BrotatoBoi) ----- ~~ #
# ~~ --------- Program Name: Interpre-tato. --------- ~~ #
# ~~ ----------- Date: November/14/2021. ------------ ~~ #
# ~~ - Description: My potato language interpreter. - ~~ #
# ~~ ------------------------------------------------ ~~ #


# ~ Run Potato. ~ #
def run(file):
    variables = {}

    # ~ Open the file. ~ #
    with open(file, 'r') as f:
        # ~ Read each line ~ #
        for line in f:
            # ~ Check if the line is a comment. ~ #
            if line.startswith('$'):
                # ~ If it is, skip it. ~ #
                continue
            # ~ If it isn't, split it into a list. ~ #
            line = line.split()

            # ~ Check if the line is not empty. ~ #
            if line:
                if line[0] == 'say':
                    inString = False
                    output = ''
                    message = ' '.join(line[1:]).split(' ')

                    # ~ Loop through the message. ~ #
                    for word in message:
                        # ~ Check if the word is a variable. ~ #
                        if word in variables:
                            # ~ If it is, add it to the output. ~ #
                            output += variables[word]
                        # ~ If it isn't, add it to the output. ~ #
                        else:
                            for char in word:
                                if char == '"':
                                    inString = not inString
                                elif inString:
                                    output += char

                            output += ' '

                    # ~ Print the output. ~ #
                    print(output)

                # ~ Check if the line is a variable. ~ #
                elif line[0] == 'set':
                    # ~ If it is, set the variable. ~ #
                    variables[line[1]] = ' '.join(line[2:])

                # ~ Check if the line is user input. ~ #
                elif line[0] == 'get':
                    # ~ If it is, get the user input. ~ #
                    variables[line[1]] = input(' '.join(line[2:]))

# ~ Main Loop. ~ #
while True:

    # ~ Get command. ~ #
    cmd = input(">> ")

    # ~ Process Command. ~ #
    if cmd == "exit": # ~ Exit Loop. ~
        break
    elif cmd.startswith("run"): # ~ Run a Potato File. ~ #
        file = cmd.split(" ")[1]
        run(file)
    elif cmd == "help":
        print("""
        Commands:
        run <file> - Run a potato file.
        exit - Exit the interpreter.
        help - Show this help message.
        """)
    else:
        print("Invalid command!")
