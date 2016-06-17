Testing
===

To test how the program performs with given input data:

```bash
python sandhisplitter/test.py -m MODELFILE \
    -t TESTFILE -u unsplit -s split
```

Example:
```bash
python sandhisplitter/test.py -m sandhisplitter/models/model.json \
    -t data/owndata -u output/unsplit.txt -s output/split.txt
```

The testfile should have the same syntax as the training file.

```
WxyZ=Wx'+y'Z|sp_1,sp_2,sp_3
```


