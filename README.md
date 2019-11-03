# Transliterator

> A multilingual to-English transliterator currently supporting Hungarian, Russian, and Yiddish.

## Setup 

- Get prerequisites with `pip3 install unidecode`
- Download with `git clone https://github.com/a11ce/transliterator.git`

## Usage

`transliterator.py` reads from standard input, so you can:
- Run `python3 transliterator.py <language>.tl` then type your text.
- Run `cat file.txt | python3 transliterator.py <language>.tl`
- (On macOS) `pbpaste | python3 transliterate.py <language>.tl` to transliterate your clipboard.

## .tl files
- Each line is `in: out`.
- The input and output may be any length as long as they are seperated by a colon and space.
- Substitutions are performed from top to bottom, and latter substitutions may operate on the result of former ones. For example, in a hypothetical example language where both 'ū' and 'ūū' may be transliterated as oo, the rule `oooo: oo` could be added (after `ū: oo`). In this case, it would be just as simple to add `ūū: oo` before the single ū rule, but in other cases (i.e. languages with multiple letters that may transliterate to the same text) the ability to operate on partially transliterated text in this way may be very useful. 

---

All contributions are welcome by pull request or issue.

Transliterator is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.