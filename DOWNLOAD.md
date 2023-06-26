Please visit dataset [homepage](https://github.com/JenAlchimowicz/Semantic-segmentation-with-PyTorch-Satellite-Imagery) to download the data. 

Afterward, you have the option to download it in the universal supervisely format by utilizing the *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Semantic-segmentation-Satellite-Imagery', dst_path='~/dtools/datasets/Semantic-segmentation-Satellite-Imagery.tar')
```
