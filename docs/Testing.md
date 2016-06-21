Testing
===

To test how the program performs with given input data:

```bash
python sandhisplitter/test.py -m MODELFILE \
    -t TESTFILE -o output
```

Example:
```bash
python sandhisplitter/test.py -m sandhisplitter/models/model.json \
    -t data/owndata -o output/results.txt
```

The testfile should have the same syntax as the training file.

```
WxyZ=Wx'+y'Z|sp_1,sp_2,sp_3
```


