# Data Directory

## Directory structure

```text
data/
├── dset/
│   ├── scene/
│   │   ├── scene_ori/          # Original satellite imagery
│   │   │   ├── l5/
│   │   │   ├── l7/
│   │   │   ├── l8/
│   │   │   ├── l9/
│   │   │   └── s2/
│   │   └── scene_nor/          # Normalized satellite imagery
│   │       ├── l5/
│   │       ├── l7/
│   │       ├── l8/
│   │       ├── l9/
│   │       └── s2/
│   ├── dem/
│   │   ├── dem_ori/            # Original DEMs
│   │   └── dem_nor/            # Normalized DEMs
│   ├── truth/
│   │   ├── truth_gpkg/         # Glacier labels in vector format
│   │   │   ├── l5/
│   │   │   ├── l7/
│   │   │   ├── l8/
│   │   │   ├── l9/
│   │   │   └── s2/
│   │   └── truth_tif/          # Rasterized binary glacier masks
│   │       ├── l5/
│   │       ├── l7/
│   │       ├── l8/
│   │       ├── l9/
│   │       └── s2/
│   ├── dset_split/
│   │   ├── train/
│   │   │   ├── scene/
│   │   │   ├── dem/
│   │   │   └── truth/
│   │   ├── val/
│   │   │   ├── scene/
│   │   │   ├── dem/
│   │   │   └── truth/
│   │   └── val_patch/
│   │       ├── patch_512/      # 512 × 512 validation tensors
│   │       └── patch_1024_null/ # Reserved 1024 × 1024 patch directory
│   └── dset.gpkg               # Dataset locations and split metadata
├── result/                     # Model predictions and evaluation outputs
└── readme.md
```

## Notes

- `scene`: multispectral satellite images.
- `dem`: digital elevation models.
- `truth`: glacier vector labels and binary masks.
- `dset_split`: training data, validation data, and validation patches.
- `result`: model predictions and evaluation results.

Example matching files:

```text
scene/scene_nor/l8/l8_scene_01.tif
dem/dem_nor/l8_scene_01_dem.tif
truth/truth_tif/l8/l8_scene_01_truth.tif
```
