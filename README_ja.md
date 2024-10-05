# RenPy Dialogue Importer

このツールは、2つの`dialogue.tab`ファイルからRenPy翻訳スクリプトに変換するためのコマンドラインツールです。

## 使用方法

### 環境構築

Poetryまたは通常のpipを用いて`requirements.txt`や`pyproject.toml`よりインストールが可能です。

### コマンドライン引数

- `file1`: オリジナルの対話ファイル（.tabファイル）
- `file2`: 翻訳された対話ファイル（.tabファイル）
- `-o`, `--output`: 出力ディレクトリ名（デフォルト: `output`）
- `-la`, `--language`: 出力言語（デフォルト: `japanese`）
- `-s`, `--strings`: 出力文字列ステートメント（デフォルト: `True`）
- `-l`, `--log`: ロギングレベル（デフォルト: `INFO`）

### 使用例

以下に、コマンドラインからこのツールを使用する例を示します。

```sh
python main.py original.tab translated.tab -o output_dir -la japanese -s True -l DEBUG
```
