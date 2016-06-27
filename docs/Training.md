Training
===

The model has to be trained to be used by the module later.

The data has to be annotated in the following format.

```
WxyZ=Wx'+y'Z|sp_1,sp_2,sp_3
```

Syntax is strict, the train.py script will show the line number of the error in case there is any.

The folder data contains annotated data, in files `ltrc_dataset`, `owndata`, or `combined`.

To run the training script

```
python sandhisplitter/train.py -k DEPTH -s SKIP -i INPUT_TRAINING_FILE\
    -o OUTPUT_MODEL_FILE
```

For example

```
python sandhisplitter/train.py -k 3 -s 1 -i data/owndata \
    -o sandhisplitter/models/model.json
```


