from loader.base_loader import BaseLoader
import copy as cp
import numpy as np

class DictLoader(BaseLoader):
    def __init__(self, self, param_dict: dict) -> None:
        self.param_dict = param_dict

    def dict_loader(self, param_array_general: dict, param_array_numbers: dict, param_array_cat: dict):
        dict_loader = cp.deepcopy(param_array_general)

        for key in param_array_general.keys():
            if param_array_general[key]['list_type'] == 'object':
                dict_loader[key]['unique'] = param_array_cat[key]['unique']
                dict_loader[key]['moda'] = param_array_cat[key]['moda']
                dict_loader[key]['top10'] = param_array_cat[key]['top10']
                dict_loader[key]['down10'] = param_array_cat[key]['down10']

                dict_loader[key]['mean'] = np.nan
                dict_loader[key]['std'] = np.nan
                dict_loader[key]['min_value'] = np.nan
                dict_loader[key]['median'] = np.nan
                dict_loader[key]['max_value'] = np.nan

            elif param_array_general[key]['list_type'] in ('float', 'float32', 'float64'):
                dict_loader[key]['unique'] = np.nan
                dict_loader[key]['moda'] = np.nan
                dict_loader[key]['top10'] = np.nan
                dict_loader[key]['down10'] = np.nan

                dict_loader[key]['mean'] = param_array_numbers[key]['mean']
                dict_loader[key]['std'] = param_array_numbers[key]['std']
                dict_loader[key]['min_value'] = param_array_numbers[key]['min_value']
                dict_loader[key]['median'] = param_array_numbers[key]['median']
                dict_loader[key]['max_value'] = param_array_numbers[key]['max_value']

        return dict_loader
