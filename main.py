from dotenv import load_dotenv

import src.cli

def main():
    # CLIモードのみ実装済
    src.cli.parse()


if __name__ == "__main__":
    load_dotenv()
    main()
