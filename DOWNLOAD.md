Dataset **Semantic Segmentation Satellite Imagery** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/w/M/NQ/vSlg3VQNIJMGBCq3udLgBoyBDG1FcdCxXc6QUYk3Q6YsfH4QGSe3KpBpdmT6uSTfvm4zpFhMz4AOlJfKAYPG0Jwm8EWpmZ4d6d2vW49wTbHGHl8SyntHgjTbJBtO.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Semantic Segmentation Satellite Imagery', dst_path='~/dtools/datasets/Semantic Segmentation Satellite Imagery.tar')
```
The data in original format can be downloaded here:

- 🔗[train_masks.zip](https://figshare.com/ndownloader/articles/19961426/versions/1)
- 🔗[train_images.zip](https://figshare.com/ndownloader/articles/19961336/versions/1)
