import pandas as pd
from data import Data

class Ingredient(Data):

    def __init__(self, _data):
        # super().__init__()
        self._data = _data
        
    
    def get_with_popularities(self, _data, feature_1, feature_2, feature_3):
        var = pd.DataFrame(_data.groupby([feature_1, feature_2]).count()[feature_3])
        var = var.rename_axis([feature_1, feature_2]).reset_index()
        var = var.rename(columns={'ingredient_id': 'occurrence'})
        var['apparition'] = [1 if O > 1 else 0 for O in var['occurrence']]
        _data['occurrence'] = var['occurrence']
        _data['apparition'] = var['apparition']
        return _data
