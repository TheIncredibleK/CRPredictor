import os

FILE_NAME = "C2E003_FINAL.txt"
FILE_LOCATION = os.path.join(os.getcwd(), 'data','all')
CORPUS_FILE_LOCATION = os.path.join(os.getcwd(), 'data','full')
FULL_FILE_NAME_AND_LOCATION = os.path.join(FILE_LOCATION, FILE_NAME)
FULL_CORPUS_FILE = os.path.join(CORPUS_FILE_LOCATION, "all.txt")
ALL_LINES = []
PLAYER_NAMES = ["MATT:", "MARISHA:", "LAURA:", "LIAM:", "SAM:", "TRAVIS:", "TALIESIN:", 'ASHLEY:']
POTENTIAL_PLAYERS = []
LINE_FOR_MATTS_INTRO = "last we left off"



DICTIONARY_OF_SCRIPT = {'MATT:' : [], 'MARISHA:' : [], 'LAURA:' : [], 'LIAM:': [], 'SAM:' : [], 'TRAVIS:' : [], 'TALIESIN:' : [], 'ASHLEY:':[]}

def open_file(file_name):
    current_player = "MATT:"
    opened_file = open(file_name, 'r')
    for line in opened_file.readlines():
        ALL_LINES.append(line)
        if(line.__contains__(':')):
            POTENTIAL_PLAYERS.append(line.split(":")[0])
        for name in PLAYER_NAMES:
            if name in line:
                current_player = name

        DICTIONARY_OF_SCRIPT[current_player].append(line)

    print("Finished Reading file : {}".format(file_name))
    return

def clean_dictionary():
    for key, value in DICTIONARY_OF_SCRIPT.items():
         list_without_newline_or_apps =  "".join(DICTIONARY_OF_SCRIPT[key]).replace('\n', ' ').replace('\'',  '').split(key)
         list_without_blank_lines = [i for i in list_without_newline_or_apps if i is not ',' and i is not '']
         DICTIONARY_OF_SCRIPT[key] = list_without_blank_lines

def parse_script():
    return

def get_matts_opener():
    return

def get_sams_ad():
    return

def read_all_files():
    all_files = [l for l in os.listdir(FILE_LOCATION) if l.__contains__('FINAL')][:-4][-1:]
    for file in all_files:
        file_name = os.path.join(FILE_LOCATION, file)
        open_file(file_name)
    print("Finished reading files from dir {}".format(FILE_LOCATION))
    print("Cleaning Dictionary")
    clean_dictionary()
    print("Dictionary Cleaned")
    print("Exporting entirity of CR into single txt file")
    entire_corpus_file = os.path.join(FILE_LOCATION, "all.txt")
    with open(entire_corpus_file, 'w') as f:
        f.writelines([l for l in ALL_LINES])

    print("Finished")



print(1)
read_all_files()
print(2)
