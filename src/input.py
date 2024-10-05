from loguru import logger
import csv

class DialogueLine:
    def __init__(self, id, character, dialogue, filename, line_number, script):
        self.id = id
        self.character = character
        self.dialogue = dialogue
        self.filename = filename
        self.line_number = line_number
        self.script = script

class DialogueTab:
    def __init__(self):
        self.original_dialogues = {}
        self.translated_dialogues = {}
    
    def load(self, original_filename, translated_filename):
        self.load_original(original_filename)
        self.load_translated(translated_filename)
    
    def load_original(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            counter = 1
            for line_number, row in enumerate(reader):
                # stringsステートメントはIDが空なので上から順番になるように一旦仮IDを振る(処理は今度実装)
                if row[0] == "":
                    row[0] = f"strings_{counter}"
                    counter += 1
                # ファイルの形式が正しくなく、最後のtabが抜けているときには空文字を最後に追加
                if len(row) <= 6:
                    row.append("")
                self.original_dialogues[row[0]] = DialogueLine(row[0], row[1], row[2], row[3], row[4], row[5])
    
    def load_translated(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            next(reader)
            counter = 1
            for line_number, row in enumerate(reader):
                # stringsステートメントはIDが空なので上から順番になるように一旦仮IDを振る(処理は今度実装)
                if row[0] == "":
                    row[0] = f"strings_{counter}"
                    counter += 1
                # ファイルの形式が正しくなく、最後のtabが抜けているときには空文字を最後に追加
                if len(row) <= 6:
                    row.append("")
                self.translated_dialogues[row[0]] = DialogueLine(row[0], row[1], row[2], row[3], row[4], row[5])