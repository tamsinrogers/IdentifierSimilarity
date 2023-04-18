def function(a):
    var = False
    boolean = False
    for element in a:
        if len(element) < 5:
            var = True
        else:
            if len(element) < 10:
                boolean = True
        if var:
            print(element[0])
        elif boolean:
            print(var)
        else:
            print(element[1])
        var = False
        boolean = False

a = ["treble", "bass", "microphone", "amplifier", "guitar", "glasses", "anyone"]
