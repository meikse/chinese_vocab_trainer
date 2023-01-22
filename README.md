# chinese_vocab_trainer

chinese vocable trainer to learn chinese in Pinyin and Hanyu.



The `vocab.csv` contains the data for learning.
following pattern must be adhered for a row: 

| level | german | pinyin | hanyu | hints
|-|-|-|-|-|

The vocabulary file is used by default in the current path `./vocab.csv`, but can be invoked from anywhere else using `-f` with you file name.

The level can be specified by using argument `-l` from command line.


## TODO

- make just one script to execute either terminal or GUI app
