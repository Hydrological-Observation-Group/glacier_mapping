'''
author: xin luo
create: 2025.12.4, modify: 2026.8.13
des: configuration file for notebooks.
'''

from glob import glob

## directories/files
dir_tra_scene = 'data/dset/dset_split/train/scene'
dir_tra_dem = 'data/dset/dset_split/train/dem'
dir_tra_truth = 'data/dset/dset_split/train/truth'
dir_result = 'data/result'

paths_tra_scene = sorted(glob(dir_tra_scene + '/*.tif'))
paths_tra_dem = sorted(glob(dir_tra_dem + '/*.tif'))
paths_tra_truth = sorted(glob(dir_tra_truth + '/*.tif'))



