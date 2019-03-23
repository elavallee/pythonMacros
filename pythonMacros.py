def fLoop(cntExp, exp, gbs=globals()):
    "Fucntion definition for a loop macro."
    for _ in range(eval(cntExp)):
        exec(exp, gbs)

macroLookup = {'loop': fLoop}

def runMacro(aStr):
    "Run a macro."
    args = aStr.split()
    macroLookup[args[0]](*args[1:])

i = 0; runMacro("loop 4 i+=1"); print(i)

runMacro("loop 5 print('Hello_World!')")
