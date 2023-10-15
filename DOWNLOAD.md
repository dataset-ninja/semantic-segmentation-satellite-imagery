Dataset **Semantic Segmentation Satellite Imagery** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/k/5/M4/9xP98aAoU1rrBRnbku4oXJM3F2zuAtlKOk9NxtDbWhaqEsSCVJvfWjjQmK1TaO7LAgO3TG95i6m0b4eF1mbM2SDLtczRA5PBnTEVkv8qjAVZB70jOqfJiAFSccj0.tar)

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
