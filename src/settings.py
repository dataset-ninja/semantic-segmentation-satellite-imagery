from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Semantic Segmentation Satellite Imagery"
PROJECT_NAME_FULL: str = "Semantic Segmentation with PyTorch Satellite Imagery"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0(source_url="https://figshare.com/articles/dataset/train_images_jpg/19961336?backTo=/collections/semantic_segmentation_satellite_imagery/6026765")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Domain.Geospatial(),
    Industry.SearchAndRescue(is_used=False),
    Industry.Environmental(is_used=False),
]
CATEGORY: Category = Category.Aerial(
    extra=[Category.Safety(), Category.Environmental(), Category.Satellite()]
)

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = "2022-06-02"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://figshare.com/collections/_/6026765"
    
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 861154
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/semantic-segmentation-satellite-imagery"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "train_masks.zip": "https://figshare.com/ndownloader/articles/19961426/versions/1",
    "train_images.zip": "https://figshare.com/ndownloader/articles/19961336/versions/1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "background": [230, 25, 75],
    "property roof": [60, 180, 75],
    "secondary structure": [255, 225, 25],
    "swimming pool": [0, 130, 200],
    "vehicle": [245, 130, 48],
    "grass": [145, 30, 180],
    "trees / shrubs": [70, 240, 240],
    "solar panels": [240, 50, 230],
    "chimney": [210, 245, 60],
    "street light": [250, 190, 212],
    "window": [0, 128, 128],
    "satellite antenna": [220, 190, 255],
    "garbage bins": [170, 110, 40],
    "trampoline": [255, 250, 200],s
    "road / highway": [128, 0, 0],
    "under construction / in progress status": [170, 255, 195],
    "power lines & cables": [128, 128, 0],
    "water tank / oil tank": [255, 215, 180],
    "parking area - commercial": [0, 0, 128],
    "sports complex / arena": [128, 128, 128],
    "industrial site": [230, 25, 75],
    "dense vegetation / forest": [255, 20, 147],
    "water body": [255, 225, 25],
    "flooded": [0, 130, 200],
    "boat": [245, 130, 48],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"GitHub":"https://github.com/JenAlchimowicz/Semantic-segmentation-with-PyTorch-Satellite-Imagery"}

BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = "https://doi.org/10.6084/m9.figshare.c.6026765.v1"
AUTHORS: Optional[List[str]] = None
AUTHORS_CONTACTS: Optional[List[str]] = None


ORGANIZATION_NAME: Optional[Union[str, List[str]]] = None
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,        
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
