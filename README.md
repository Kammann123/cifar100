# nn-tp3
Work developed in Python using Jupyter Notebooks for the Neural Networks course. The work consists on a Kaggle challenge to classify images from the CIFAR-100 dataset.
The link to the Kaggle competition is https://www.kaggle.com/c/rn2021q1itba-cifar100.

**The winner jupyter notebook is test-09**

## Analysis
Simple jupyter notebook to analyze the dataset.

## Tests
* **test-00**: Base neural network with minor improvements
* **test-01**: TL with ResNet50 val_acc = 0.77
* **test-02**: TL with VGG16 not good results at first, we dropped this path
* **test-03**: Data augmentation (testing different libraries with the model created in test-00 and test-02)
* **test-04**: TL with EfficientNetB0 val_acc = 0.84
* **test-05**: Custom model with data augmentation val_acc = 0.63
* **test-07**: TL with EfficientNetB2 val_acc = 0.85
* **test-09**: TL with EfficientNetB3 val_acc = 0.87
