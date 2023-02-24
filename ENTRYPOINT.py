# REQUIRED IMPORTS:
import json
import random
import os
import sys

# GET(): SELECTS A RANDOM OBJECT FROM THE JSONC DATABASE (IF IT'S RUNNING IN DOCKER CONTAINER OR GITHUB ACTIONS USES THE LOCAL FILE OTHERWISE USES THE REMOTE FILE). PARSES IT. FORMATS IT IN A 'QUOTE (AUTHOR)' STYLE (IF THE AUTHOR IS NULL IT DOESN'T GET PRINTED). THEN PRINTS IT.
def GET_RANDOM(GMS7_COMPATIBLE: bool = False):
    QUOTE = None # SET THE QUOTE TO NONE
    # IF THE JSONC DATABASE IS RUNNING IN DOCKER CONTAINER OR GITHUB ACTIONS USES THE LOCAL FILE OTHERWISE USES THE REMOTE FILE.
    PATH: str = '/DATABASE.jsonc' if os.path.exists('/DATABASE.jsonc') else 'DATABASE.jsonc' if os.path.exists('DATABASE.jsonc') else None # SET THE PATH TO THE DATABASE
    if PATH is not None: # IF THE LOCAL DATABASE EXISTS
        with open(PATH, 'r') as DATA: # OPEN THE DATABASE
            DATABASE = json.load(DATA) # LOAD THE DATABASE
    else: # IF THE LOCAL DATABASE DOESN'T EXIST
        raise FileNotFoundError('DATABASE NOT FOUND') # RAISE A FILE NOT FOUND ERROR
    while (QUOTE is None or (GMS7_COMPATIBLE is True and len(QUOTE) > 160)): # WHILE THE QUOTE IS NONE OR THE QUOTE IS LONGER THAN 160 CHARACTERS AND THE GMS7_COMPATIBLE ARGUMENT IS TRUE
        OBJECT = random.choice(DATABASE) # SELECT A RANDOM OBJECT FROM THE DATABASE
        if OBJECT.keys().__contains__('AUTHOR'): # IF THE AUTHOR IS NOT NULL
            # IF THE AUTHOR IS NOT NULL: PRINT THE QUOTE AND THE AUTHOR
            QUOTE = f'{OBJECT["QUOTE"]} ({OBJECT["AUTHOR"]})' # SET THE QUOTE TO THE QUOTE AND THE AUTHOR
        else: # IF THE AUTHOR IS NULL
            # IF THE AUTHOR IS NULL: PRINT ONLY THE QUOTE
            QUOTE = f'{OBJECT["QUOTE"]}' # SET THE QUOTE TO THE QUOTE
    print(QUOTE) # PRINT THE QUOTE
    return QUOTE # RETURNS THE QUOTE
    
# MAIN(): CALLS GET() AND PRINTS THE RESULTS.
if __name__ == "__main__":
    if len(sys.argv) == 2: # IF TWO ARGUMENTS ARE PROVIDED: USE THE SECOND ARGUMENT AS THE GMS7_COMPATIBLE ARGUMENT.
        _ = GET_RANDOM(GMS7_COMPATIBLE=sys.argv[1]) # RUNS THE GET() FUNCTION AND PRINTS THE RESULTS.
    elif len(sys.argv) == 1: # IF ONE ARGUMENT IS PROVIDED: USE THE DEFAULT ARGUMENTS.
        _ = GET_RANDOM() # RUNS THE GET() FUNCTION AND PRINTS THE RESULTS.
    else: # IF MORE THAN THREE ARGUMENTS ARE PROVIDED: RAISE A SYNTAX ERROR.
        raise SyntaxError('TOO MANY ARGUMENTS') # RAISE A SYNTAX ERROR