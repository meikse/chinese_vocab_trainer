# chinese_vocab_trainer

Simple Python vocab trainer to learn Chinese in Pinyin and Hanyu.

| terminal                         | interface                         |
|----------------------------------|-----------------------------------|
| <terminal gif> | <img src="https://user-images.githubusercontent.com/75035512/214163526-2c71a321-54f6-4139-a198-87f593d12fb1.png" width="400" /> |

## prerequisites

- python 3.7 or newer

## installation

Simply clone this repository: 
```sh
git clone https://github.com/meikse/chinese_vocab_trainer --b tkinter
```
No extra modules are needed for usage.

## preparation

To simply use the trainer, a `./vocab.csv` shall exist in the root. 
This file should be manually filled with vocabulary that will be learned by the user. Note, only "," should be used as separation indicator!
For that the following pattern must be adhered for one row: 

| level | german | pinyin | hanyu | hints
|-------|--------|--------|-------|--------------------------------------------|
| 1     | hallo  | nIhAo  | 你好  | the direct translation might be "you good" |
| 1     | er     | taa    | 他    | third person singular masculine            |
| 2     | lesen  | du?    | 读    |                                            |
| 1     | nein   | bu!    | 不    | e.g. negative response                     |

(*german* is used here as the target language, but any other language can be used as long es the font encoding is supported)

For simplification purposes, the four different vocal tones in chinese phonetic are mapped to the following symbols/letters to quickly insert words on an english keyboard.

| official | ascii |
|----------|-------|
| á        | a?    |
| à        | a!    |
| ā        | aa    |
| ǎ        | A     |


## usage

The vocab trainer can be used from terminal directly
```sh
python3 term.py -f <file> -l <level>
```
in terminal-mode, one can press `h` to receive further help.
Following actions are possible:

| args | description                                |
|------|--------------------------------------------|
| i    | info for word hints                        |
| c    | change target lang (target, pinyin, hanyu) |
| n    | new vocab for the list                     |
| h    | for this help                              |
| q    | quit this client                           |

to use the trainer with an interface, execute
```sh
python3 interface.py -f <file> -l <level>
```

As already mentioned, the vocabulary file is used by default in the current path `./vocab.csv`, but can be invoked from anywhere else using `-f` with you file name.

The level/lecture can be specified by using argument `-l` from command line.
If no lecture is specified, the first lecture is chosen.


## TODO

- make a simple script to execute either terminal or GUI app
- `c` command in terminal mode is not working properly
- un-specify target language
- at least 2 entries must exist for a level
- beautify GUI
