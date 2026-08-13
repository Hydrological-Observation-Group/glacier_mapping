## author: xin luo, 
## created: 2026.8.13
## des: utility functions for data processing


import rasterio as rio 

## read scenes
def read_scenes(scene_paths, dem_paths, truth_paths):
  paths_zip = zip(scene_paths, dem_paths, truth_paths)
  scenes_arr = []
  dems_arr = []
  truths_arr = []
  for scene_path, dem_path, truth_path in paths_zip:
      ## 1. read scene, dem and truth images
      with rio.open(scene_path) as src:
        scene_arr = src.read().transpose((1, 2, 0))  # (H, W, C)
      with rio.open(dem_path) as src:
        dem_arr = src.read().transpose((1, 2, 0))  # (H, W, C)
      with rio.open(truth_path) as truth_src:
        truth_arr = truth_src.read(1)  # (H, W)
      scenes_arr.append(scene_arr)
      dems_arr.append(dem_arr)
      truths_arr.append(truth_arr)
  return scenes_arr, dems_arr, truths_arr 

