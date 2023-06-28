Dataset **Semantic-segmentation-Satellite-Imagery** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/c/f/KX/AlHpxXoxWO7iKu1K2jPIgAPWbt0usvEMVHszzQhl9gY83fdvdk8VtIof3pS77x2JGmZxG0mNjNYoCPz9qoszKGmKvZzQNY0M6Ufoz1wn7Wmli9yO7qFa6nbIOMEU.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Semantic-segmentation-Satellite-Imagery', dst_path='~/dtools/datasets/Semantic-segmentation-Satellite-Imagery.tar')
```
The data in original format can be downloaded here:

- 🔗[train_masks.zip](https://figshare.com/ndownloader/articles/19961426/versions/1)
- 🔗[train_images.zip](https://figshare.com/ndownloader/articles/19961336/versions/1)
