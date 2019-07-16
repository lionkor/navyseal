running = True

while running:

    text = ""
    mode = -1

    while len (text) <= 0:
        text = input ("Enter text: ")

    while mode != 1 and mode != 2 and mode != 3:
        try:
            mode = int (input ("Choose mode: \n    1. NavySeal to Normal\n    2. Normal to NavySeal\n    3. Exit\nMode [1,2]: "))
        except Exception:
            mode = -1

    if mode == 3:
        running = False

    result = ""

    nato = {
        "A" : "Alfa", 
        "B" : "Bravo", 
        "C" : "Charlie", 
        "D" : "Delta", 
        "E" : "Echo", 
        "F" : "Foxtrot", 
        "G" : "Golf", 
        "H" : "Hotel", 
        "I" : "India", 
        "J" : "Juliett", 
        "K" : "Kilo", 
        "L" : "Lima", 
        "M" : "Mike", 
        "N" : "November", 
        "O" : "Oscar", 
        "P" : "Papa", 
        "Q" : "Quebec", 
        "R" : "Romeo", 
        "S" : "Sierra", 
        "T" : "Tango", 
        "U" : "Uniform", 
        "V" : "Victor", 
        "W" : "Whiskey", 
        "X" : "X-ray", 
        "Y" : "Yankee", 
        "Z" : "Zulu"
    }

    if mode == 1:
        for word in text.split (" "):
            result += word.strip()[0]
            if "." in word:
                result += " "

    elif mode == 2:
        for c in text:
            c = c.upper ()
            if c == " ":
                result += "."
            else:
                result += " " + nato[c]
        result += "."

    print (result.strip ())


