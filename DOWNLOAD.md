Dataset **Semantic Segmentation Satellite Imagery** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/H/Y/3e/rUJyZ8v8mnMOo7lEjtLetmzLhuyWvrVIiO36Jnt4apwARIHzx2SE21wtnpm3y6j3tA2MgYuMPReBYluHOcHNv19C8LLyk2e0YQN9cohV67IBWjwQRgCiVAjha45O.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Semantic Segmentation Satellite Imagery', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [train_masks.zip](https://figshare.com/ndownloader/articles/19961426/versions/1)
- [train_images.zip](https://figshare.com/ndownloader/articles/19961336/versions/1)
