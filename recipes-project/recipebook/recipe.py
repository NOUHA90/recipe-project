import pandas as pd
class Recipe:
    def __init__(self, df):
        self.df = df

    def get_scored_recipes(self):
        var = pd.DataFrame(self.df.groupby(['recipe_id','name']).sum()['Score'])
        return var.rename_axis(['recipe_id','name']).reset_index()

    def get_moy_scored_recipes(self):
        var = pd.DataFrame(self.df.groupby(['recipe_id','name']).mean()['Score'])
        return var.rename_axis(['recipe_id','name']).reset_index()

        

