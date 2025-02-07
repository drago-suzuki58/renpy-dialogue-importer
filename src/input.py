from loguru import logger
import csv
from dataclasses import dataclass

@dataclass
class DialogueLine:
    id: str
    character: str
    dialogue: str
    filename: str
    line_number: int
    script: str

class DialogueTab:
    def __init__(self):
        self.original_dialogues = {}
        self.translated_dialogues = {}
        self.original_strings = {}
        self.translated_strings = {}
    
    def load(self, original_filename, translated_filename, language):
        self.load_original(original_filename, language)
        self.load_translated(translated_filename, language)
    
    def load_original(self, filename, language):
        logger.debug(f"Loading original file: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            counter = 1
            for line_number, row in enumerate(reader):
                # ファイルの形式が正しくなく、最後のtabが抜けているときには空文字を最後に追加
                if len(row) < 6:
                    row.append("")
                if row[3].startswith(f"game/tl/{language}/"):
                    renpy_filename = "game/" + row[3][len(f"game/tl/{language}/"):]
                else:
                    renpy_filename = row[3]
                if renpy_filename not in self.original_dialogues:
                    self.original_dialogues[renpy_filename] = {}
                    self.original_strings[renpy_filename] = {}
                # stringsステートメントはIDが空なので上から順番になるように一旦仮IDを振る(でもこれだとどうしてもズレることがある)
                if row[0] == "":
                    row[0] = f"strings_{counter}"
                    self.original_strings[renpy_filename][row[0]] = DialogueLine(row[0], row[1], row[2], renpy_filename, int(row[4]), row[5])
                    counter += 1
                    continue
                self.original_dialogues[renpy_filename][row[0]] = DialogueLine(row[0], row[1], row[2], renpy_filename, int(row[4]), row[5])

    def load_translated(self, filename, language):
        logger.debug(f"Loading translated file: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            counter = 1
            for line_number, row in enumerate(reader):
                # ファイルの形式が正しくなく、最後のtabが抜けているときには空文字を最後に追加
                if len(row) < 6:
                    row.append("")
                if row[3].startswith(f"game/tl/{language}/"):
                    renpy_filename = "game/" + row[3][len(f"game/tl/{language}/"):]
                    #print(renpy_filename)
                else:
                    renpy_filename = row[3]
                if renpy_filename not in self.translated_dialogues:
                    self.translated_dialogues[renpy_filename] = {}
                    self.translated_strings[renpy_filename] = {}
                # stringsステートメントはIDが空なので上から順番になるように一旦仮IDを振る(でもこれだとどうしてもズレることがある)
                if row[0] == "":
                    row[0] = f"strings_{counter}"
                    self.translated_strings[renpy_filename][row[0]] = DialogueLine(row[0], row[1], row[2], renpy_filename, int(row[4]), row[5])
                    counter += 1
                    continue
                self.translated_dialogues[renpy_filename][row[0]] = DialogueLine(row[0], row[1], row[2], renpy_filename, int(row[4]), row[5])

# `translated_dialogues` and `original_dialogues` Example.
#
# {
#     "chapter1.rpy": {
#         "id1": DialogueLine(id="id1", character="character1", dialogue="dialogue1", filename="chapter1.rpy", line_number=1, script="script1"),
#         "id3": DialogueLine(id="id3", character="character1", dialogue="dialogue3", filename="chapter1.rpy", line_number=3, script="script3")
#     },
#     "chapter2.rpy": {
#         "id2": DialogueLine(id="id2", character="character2", dialogue="dialogue2", filename="chapter2.rpy", line_number=2, script="script2")
#     }
# }
