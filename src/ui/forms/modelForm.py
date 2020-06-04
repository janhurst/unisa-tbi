from flask_wtf import FlaskForm
from wtforms import SelectField
from ui.api.model_management import ARTIFACTS_DIR
from os import listdir, path
import fnmatch
import json

class ModelForm(FlaskForm):
    
    @staticmethod
    def get():
       
        # enumerate models
        models = {}
        
        # in some odd race conditions the directory might not exist, in which case we just bail
        if not path.exists(ARTIFACTS_DIR):
            return []

        # each directory in the artifacts directory has a pkl file and a metrics.json
        for experiment_dir in listdir(ARTIFACTS_DIR):
            for filename in listdir(path.join(ARTIFACTS_DIR, experiment_dir)):
                if fnmatch.fnmatch(filename, '*.pkl'):
                    name = experiment_dir + '/' + path.splitext(filename)[0]
                    with open(path.join(ARTIFACTS_DIR, experiment_dir) + path.sep + 'metrics.json', 'r') as f:
                        metrics = json.load(f)
                    models[name] = metrics['test_f1']

        # construct choices array
        choices = []
        for key, value in sorted(models.items(), key=lambda x: x[1], reverse=True):
            display = f"{key} (f1: {round(float(value),3)})"
            choices.append((key, display))

        # define a static class
        class F(FlaskForm):
            pass

        # add a field to the static form class
        setattr(F, 'model', SelectField('Model', choices = choices))

        return F()
