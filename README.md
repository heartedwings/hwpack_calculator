# hwpack_calculator

シンプルな計算パッケージです。  
本 README はローカル開発環境でのセットアップとビルド手順をまとめています。

> 📄 公開用README（PyPI用）は `README_PYPI.md` を参照してください。

---

## 環境構築（開発者向け）

### 1. Python のインストール

- Python 3.6 以上が必要です。  
- [公式サイト](https://www.python.org/downloads/)からインストールしてください。

### 2. 仮想環境の作成（推奨）

```bash
python -m venv .venv

# 仮想環境の有効化
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows (cmd.exe)
.venv\Scripts\Activate.ps1       # Windows (PowerShell)
```

### 3. 必要パッケージのインストール
```bash
pip install -r requirements.txt
```

## ビルド手順（開発者向け）
```bash
python -m build
```
- dist/ フォルダに .whl と .tar.gz が生成されます。

## インストール方法
### 1. PyPI からインストール（利用者向け・推奨）
PyPI に公開済みのため、以下のコマンドで簡単にインストール可能です。
```bash
pip install hwpack-calculator
```

### 2. ローカルビルド済みパッケージのインストール（開発者向け）
開発や動作確認のためにローカルでビルドしたパッケージを使いたい場合は、次のコマンドを実行してください。
```bash
pip install dist/hwpack_calculator-0.1.0-py3-none-any.whl
```
※ whlファイルはバージョン更新によって変化するので設定要確認。

## 動作確認
本パッケージには、以下の4つの基本的な演算関数が含まれています。

- 加算（add）

  2つの数値を加算します。

- 減算（subtract）

  2つの数値の差を計算します（引き算）。

- 乗算（multiply）

  2つの数値の積を返します（掛け算）。

- 除算（divide）

  第1引数を第2引数で割った結果を返します（0で割る場合は ZeroDivisionError が発生）。


### 使用例
```python
from hwpack_calculator import calculator

result = calculator.add(2, 3)
print(result)  # 5 が表示されます
```

## パッケージ情報
名前：hwpack_calculator

バージョン：0.1.0

ライセンス：MIT

作者：heartedwings

ホームページ：https://github.com/heartedwings/hwpack_calculator

---
このプロジェクトは [MITライセンス](https://opensource.org/licenses/MIT) のもとで公開されています。

© 2025 heartedwings