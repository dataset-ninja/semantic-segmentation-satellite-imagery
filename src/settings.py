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
LICENSE: License = License.CC_BY_4_0()
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

HOMEPAGE_URL: str = (
    "https://github.com/JenAlchimowicz/Semantic-segmentation-with-PyTorch-Satellite-Imagery"
)
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
    "Background": [230, 25, 75],
    "Property Roof": [60, 180, 75],
    "Secondary Structure": [255, 225, 25],
    "Swimming Pool": [0, 130, 200],
    "Vehicle": [245, 130, 48],
    "Grass": [145, 30, 180],
    "Trees / Shrubs": [70, 240, 240],
    "Solar Panels": [240, 50, 230],
    "Chimney": [210, 245, 60],
    "Street Light": [250, 190, 212],
    "Window": [0, 128, 128],
    "Satellite Antenna": [220, 190, 255],
    "Garbage Bins": [170, 110, 40],
    "Trampoline": [255, 250, 200],
    "Road/Highway": [128, 0, 0],
    "Under Construction / In Progress Status": [170, 255, 195],
    "Power Lines & Cables": [128, 128, 0],
    "Water Tank / Oil Tank": [255, 215, 180],
    "Parking Area - Commercial": [0, 0, 128],
    "Sports Complex / Arena": [128, 128, 128],
    "Industrial Site": [230, 25, 75],
    "Dense Vegetation / Forest": [255, 20, 147],
    "Water Body": [255, 225, 25],
    "Flooded": [0, 130, 200],
    "Boat": [245, 130, 48],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = "https://doi.org/10.6084/m9.figshare.c.6026765.v1"
AUTHORS: Optional[List[str]] = ["Jedrzej Alchimowicz"]

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
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
