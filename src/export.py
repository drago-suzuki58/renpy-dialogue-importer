from loguru import logger
import re
import datetime
import os

import src.input

def exporter(dialogue: src.input.DialogueTab, args):
    try:
        if dialogue.original_dialogues == {} or dialogue.translated_dialogues == {}:
            raise ValueError("Dialogue file is empty")
    except ValueError as e:
        logger.error(e)
        return
    
    writer(dialogue, args.output, args.language, args.strings)
    return

def writer(dialogue: src.input.DialogueTab, output_dir, language, strings):
    def file_init():
        content = []
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        content.append(f"# TODO: Translation updated at {now_time}\n")
        content.append(f"# This Translation converted by third party tool.\n")
        content.append(f"\n")
        return content

    def write(output_filename, content):
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        with open(output_filename, "w", encoding="utf-8") as f:
            # まとめて書き込み
            f.writelines(content)

    def append_normal(renpy_filename, content):
        for id in dialogue.translated_dialogues[renpy_filename]:
            try:
                original_filename = normalize_path(renpy_filename)
                original_dialogue = dialogue.original_dialogues[original_filename][id]
                translated_dialogue = dialogue.translated_dialogues[renpy_filename][id]
            except KeyError:
                original_filename = normalize_path(renpy_filename)
                logger.warning(f"Original dialogue not found: {original_filename} {id}")
                continue
            original_content = dialogue_convert(original_dialogue.dialogue, original_dialogue.script)
            translated_content = dialogue_convert(translated_dialogue.dialogue, translated_dialogue.script)
            
            content.append(f"# {translated_dialogue.filename}:{translated_dialogue.line_number}\n")
            content.append(f"translate {language} {translated_dialogue.id}:\n")
            content.append(f"\n")
            content.append(f"    # {original_content}\n")
            content.append(f"    {translated_content}\n")
            content.append(f"\n")
        return content
    
    def append_strings(renpy_filename, content):
        for id in dialogue.translated_strings[renpy_filename]:
            try:
                original_filename = normalize_path(renpy_filename)
                original_dialogue = dialogue.original_strings[original_filename][id]
                translated_dialogue = dialogue.translated_strings[renpy_filename][id]
            except KeyError:
                logger.warning(f"Original dialogue not found: {renpy_filename} {id}")
                continue

            content.append(f"    # {original_dialogue.filename}:{original_dialogue.line_number}\n")
            content.append(f"    old \"{original_dialogue.dialogue}\"\n")
            content.append(f"    new \"{translated_dialogue.dialogue}\"\n")
            content.append(f"\n")
        return content

    def strings_init(content):
        print("strings append")
        content.append(f"translate {language} strings:\n")
        return content

    def dialogue_convert(dialogue, renpy_script):
        if renpy_script == "":
            return f"\"{dialogue}\""
        elif renpy_script == "[what]":
            return re.sub(r"\[what\]", f"\"{dialogue}\"", renpy_script)
        else:
            return re.sub(r"\[what\]", dialogue, renpy_script)

    def remove_game_prefix(renpy_filename):
        prefix = "game/"
        if renpy_filename.startswith(prefix):
            return renpy_filename[len(prefix):]
        return renpy_filename

    def normalize_path(renpy_filename):
        pattern = f"game/tl/{language}/"
        if renpy_filename.startswith(pattern):
            return "game/" + renpy_filename[len(pattern):]
        return renpy_filename

    def start():
        for renpy_filename in dialogue.translated_dialogues:
            content = file_init()
            content = append_normal(renpy_filename, content)
            if strings and dialogue.translated_strings[renpy_filename] != {}:
                content = strings_init(content)
                content = append_strings(renpy_filename, content)
            outputname = remove_game_prefix(normalize_path(renpy_filename))
            write(f"{output_dir}/{outputname}", content)
    
    logger.debug("Exporting...")
    start()