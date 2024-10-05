# RenPy Dialogue Importer

This tool is a command-line tool for converting two `dialogue.tab` files into a RenPy translation script.

## Usage

### Environment Setup

You can install the dependencies using Poetry or the usual pip from `requirements.txt` or `pyproject.toml`.

### Command Line Arguments

- `file1`: Original dialogue file (.tab file)
- `file2`: Translated dialogue file (.tab file)
- `-o`, `--output`: Output directory name (default: `output`)
- `-la`, `--language`: Output language (default: `japanese`)
- `-s`, `--strings`: Output strings statement (default: `True`)
- `-l`, `--log`: Logging level (default: `INFO`)

### Example Usage

Below is an example of how to use this tool from the command line.

```sh
python main.py original.tab translated.tab -o output_dir -la japanese -s True -l INFO
```
