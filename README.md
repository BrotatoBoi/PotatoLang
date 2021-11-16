# PotatoLangV0.1.5
A custom programming language I am making. It is simple to use and has the extension of <var>.pot</var>

# Usage:
To use my language it is currently only available through the interpreter, which is called <em>'Interpre-tato'</em>.
</br> 
<code>python3 Interpre-tato.py</code>
</br>
<code>run [FILE]</code>

# Documentation
There will be updates so there will be more in the future!

Starting a line with <code>$</code> means it is a comment and gets ignored by the interpreter. (Make sure there is a space after the '$')
</br>
To create a variable use the line has to read: <code>set [VARIABLE NAME] [VARIABLE TYPE] [VALUE]</code>
</br>
To print text to the screen the line should be: <code>say "[MESSAGE]" [VARIABLE]</code>
</br>
To get user input: <code>get [VARIABLE NAME] [MESSAGE]</code>
</br>
You can check variables with the following line: <code>if [CONDITION] then [CODE] else [CODE]</code>


# Notes:
  * You can check the [examples folder](https://github.com/BrotatoBoi/PotatoLang/Examples) for an indepth code usage.

  * You can have the if/else <var>[CODE]</var> block do multiple things if you seperate them with a <var>' ; '</var>

  * The if/else statement is extreamly basic and can only handle one set of conditions and the only operator is <var>'equals'</var>