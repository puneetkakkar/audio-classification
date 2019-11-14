# AudioClassification
A dead simple audio classification

![PyPI - Python Version](https://img.shields.io/badge/python-3.1.0-blue.svg)
[![PyPI](https://img.shields.io/badge/pypi-v0.1.3-blue.svg)](https://pypi.org/project/pyaudioclassification/)
## Who is this for? 👩‍💻 👨‍💻
People who just want to classify some audio quickly, without having to dive into the world of audio analysis.
If you need something a little more involved.

### Requirements
* __Python 3__
* Keras
* Tensorflow
* librosa
* NumPy
* Soundfile
* tqdm
* matplotlib

## Quick start
```python
from pyaudioclassification import feature_extraction, train, predict
features, labels = feature_extraction(<data_path>)
model = train(features, labels)
pred = predict(model, <data_path>)
```

Or, if you're feeling reckless, you could just string them together like so:
```python
pred = predict(train(feature_extraction(<training_data_path>)), <prediction_data_path>)
```

A full example with saving, loading & some dummy data can be found [here](https://github.com/puneetkakkar/audio-classification/blob/master/example/test.py).

---

Read below for a more detailed look at each of these calls.

## References
* Large parts of the code (particularly the feature extraction) are based on [mtobeiyf/audio-classification](https://github.com/mtobeiyf/audio-classification)
