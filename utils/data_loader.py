## author: xin luo, 
## created: 2023.10.14; modify:  2026.8.13; 
## des: data pipeline

import torch
import random
from torchvision.transforms import v2
import torchvision.transforms.v2.functional as F


## build custom transforms
class GaussianNoise(v2.Transform):
    '''
    des: add aussian noise to patch (!no dem) 
    '''
    def __init__(self, mean = 0.0, sigma_max=0.1, p=0.5):
        super().__init__()
        self.mean = mean
        self.sigma_max = sigma_max
        self.p = p
    def transform(self, inpt, params):  # rewrite transform function to update sigma
        patch, pdem, ptruth = inpt[0:-2], inpt[-2:-1], inpt[-1:]
        if torch.rand(1) < self.p:
            self.sigma = torch.rand(1)*self.sigma_max  ## update sigma        
            noise_patch = torch.randn_like(patch) * self.sigma            
            patch = patch + noise_patch
            inpt = torch.cat([patch, pdem, ptruth], dim=0)
        return inpt


class SceneArraySet(torch.utils.data.Dataset):
    '''
    des: scene, dem and truth image reading from the np.array(): read data from memory.
    '''
    def __init__(self, scene_dem_truth_list, transforms=None):
        '''input arrs_scene, arrs_truth are list'''
        self.scene_dem_truth_list = scene_dem_truth_list
        self.transforms = transforms
    def __getitem__(self, index):
        '''load images, dem and truths'''
        scene_dem_truth = self.scene_dem_truth_list[index]
        '''pre-processing (e.g., random crop)'''
        ### Image augmentation
        if self.transforms is not None:
            scene_dem_truth = self.transforms(scene_dem_truth)
        patch_pdem, ptruth = scene_dem_truth[0:-1], scene_dem_truth[-1:]
        return patch_pdem, ptruth
    def __len__(self):
        return len(self.scene_dem_truth_list) 

class PatchPathSet(torch.utils.data.Dataset):
    def __init__(self, paths_valset, transforms=None):
        self.paths_patch_pdem_ptruth = paths_valset
        self.transforms = transforms
    def __getitem__(self, index):
        '''load patches and truths'''
        patch_pdem_ptruth = torch.load(self.paths_patch_pdem_ptruth[index], 
                                   weights_only=False)        
        if self.transforms is not None:
            patch_pdem_ptruth = self.transforms(patch_pdem_ptruth)
        patch_pdem = patch_pdem_ptruth[0:-1]
        truth = patch_pdem_ptruth[-1:]
        return patch_pdem, truth
    def __len__(self):
        return len(self.paths_patch_pdem_ptruth)

