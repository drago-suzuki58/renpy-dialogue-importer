from loguru import logger
import argparse
import sys
from dotenv import load_dotenv

import src.input
import src.export

def parse():
    # コマンドライン引数のパーサーを設定
    parser = argparse.ArgumentParser(description="Convert two dialogue files into a RenPy translation script.")
    parser.add_argument("file1", help="Original dialogue file(.tab file)")
    parser.add_argument("file2", help="Translated dialogue file(.tab file)")
    parser.add_argument("-o", "--output", default="output", help="Output dir name (Default: output.csv)")
    parser.add_argument("-la", "--language", default="japanese", help="Output language (Default: japanese)")
    parser.add_argument("-s", "--strings", default=True, help="Output strings statement (Default: True)")
    parser.add_argument("-l", "--log", default="INFO", help="Logging Level (Default: INFO)")


    # 引数が異なる場合はヘルプとともに終了
    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        print("Invalid argument")
        parser.print_help()
        sys.exit(1)
    except SystemExit:
        print("Invalid argument")
        parser.print_help()
        sys.exit(1)

    # ログの設定
    logger.remove()
    logger.add(sys.stderr, level=args.log)
    logger.add("log/app_{time}.log", rotation="1 week")
    logger.debug(f"file1: {args.file1} file2: {args.file2} output: {args.output}")
    return args


def main():
    args = parse()
    
    dialogue = src.input.DialogueTab()
    dialogue.load(args.file1, args.file2, args.language)
    
    exporter = src.export.exporter(dialogue, args)


if __name__ == "__main__":
    load_dotenv()
    main()