import glob 
import pandas as pd

class Data:

    def __init__(self, path):
    #C:/Users/utilisateur/anaconda3/recipes-project/data/csv/
        self.path = path

    def list_data(self):
        list_data = []
        files = glob.glob(f"{self.path}*.csv")
        for f in files :
            data_file = pd.read_csv(f, sep = ';').dropna(axis='columns', how='all')
            list_data.append(data_file)
        return list_data
    
    def get_ingredient(self, list_data):
        return list_data[0]

    def get_recipe_items(self, list_data):
        return list_data[1]
    
    
    def get_recipe(self, list_data):
        return list_data[2]
    
    def get_merge_ordered_data(self, recipe, ingredient, recipe_items):
        t = pd.merge_ordered(recipe, ingredient, fill_method="ffill", left_by="ingredient_id")
        return pd.merge_ordered(t, recipe_items, fill_method="ffill", left_by="recipe_id")

    def get_data(self):
        list_data = self.list_data()
        ing = self.get_ingredient(list_data)
        rec_item = self.get_recipe_items(list_data)
        rec = self.get_recipe_items(list_data)
        return {"ingredient": dict(ing),
                "recipe": dict(rec),
                "recipe_items": dict(rec_item)}





