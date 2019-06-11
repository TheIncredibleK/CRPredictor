import os

FILE_NAME = "C2E003_FINAL.txt"
FILE_LOCATION = "Q:\CR\FINAL TEXT FILES"
FULL_FILE_NAME_AND_LOCATION = os.path.join(FILE_LOCATION, FILE_NAME)

PLAYER_NAMES = ["MATT:", "MARISHA:", "LAURA:", "LIAM:", "SAM:", "TRAVIS:", "TALIESIN:", 'ASHLEY:']
LINE_FOR_MATTS_INTRO = "last we left off"



DICTIONARY_OF_SCRIPT = {'MATT:' : [], 'MARISHA:' : [], 'LAURA:' : [], 'LIAM:': [], 'SAM:' : [], 'TRAVIS:' : [], 'TALIESIN:' : [], 'ASHLEY:':[]}

def open_file():
    current_player = "MATT:"
    opened_file = open(FULL_FILE_NAME_AND_LOCATION, 'r')
    for line in opened_file.readlines():
        for name in PLAYER_NAMES:
            if name in line:
                current_player = name

        DICTIONARY_OF_SCRIPT[current_player].append(line)

    for key, value in DICTIONARY_OF_SCRIPT.items():
         list_without_newline_or_apps =  "".join(DICTIONARY_OF_SCRIPT[key]).replace('\n', ' ').replace('\'',  '').split(key)
         list_without_blank_lines = [i for i in list_without_newline_or_apps if i is not ',' and i is not '']
         DICTIONARY_OF_SCRIPT[key] = list_without_blank_lines
    print(1)
    return

def parse_script():
    return

def get_matts_opener():
    return

def get_sams_ad():
    return



open_file()
