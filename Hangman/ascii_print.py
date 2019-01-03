def print_hangman(guesses):
    if guesses == 4:
        print "+---------+    ";
        print " |             ";
        print " |             ";
        print " |             ";
        print " |             ";
        print "====           ";
    elif guesses == 3:
        print "+---------+    ";
        print "|         |    "
        print "|              "
        print "|              "
        print "|              "
        print "====           ";

    elif guesses == 2:
        print "+---------+    ";
        print "|         |    "
        print "|         O    "
        print "|              "
        print "|              "
        print "|              "
        print "====            ";

    elif guesses == 1:
        print "+---------+    ";
        print "|         |    "
        print "|         O    "
        print "|        /|\\  "
        print "|              "
        print "|              "
        print "====            ";
    elif guesses == 0:
        print "+---------     ";
        print "|         |    "
        print "|         O    "
        print "|        /|\\  "
        print "|        / \\  "
        print "|              "
        print "====            "




