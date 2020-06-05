from os import listdir, mkdir, remove, rename, sep, path
import shutil
import fnmatch
from zipfile import ZipFile
import neptune
from neptune.exceptions import MissingApiToken, MissingProjectQualifiedName
from flask import Blueprint, abort, jsonify
import pickle
import numpy as np
import pandas as pd
import json
from os import environ, getenv
from time import sleep
from flask import url_for, redirect

if "ARTIFACTS_DIR" in environ:
    ARTIFACTS_DIR = getenv('ARTIFACTS_DIR')
else:
    ARTIFACTS_DIR = 'artifacts'

# create the blueprint
bp = Blueprint('model_management', __name__, url_prefix='/api/models')

@bp.route('/available')
def get_available_models():
    """ Get a list of the model files that have been downloaded """
    models = []
    # get a list of the pkl files that have been downloaded from neptune
    try:
        for experiment_dir in listdir(ARTIFACTS_DIR):
            for filename in listdir(path.join(ARTIFACTS_DIR,experiment_dir)):
                if fnmatch.fnmatch(filename, '*.pkl'):
                    models.append(experiment_dir + '/' + path.splitext(filename)[0])
        return jsonify(models)
    except:
        return abort(404)

@bp.route('/update')
def update_models():
    """ Download models that are tagged with 'prod' from neptune """
    # remove the models dir if it exists
    try:
        shutil.rmtree(ARTIFACTS_DIR)
        sleep(1)
        mkdir(ARTIFACTS_DIR)
    except (FileNotFoundError):
        pass
    
    # connect to neptune
    try:
        project = neptune.init()
    except (MissingProjectQualifiedName):
        return 'NEPTUNE_PROJECT environment variable is missing'
    except (MissingApiToken):
        return 'NEPTUNE_API_TOKEN environment variable is missing'
    except (Exception) as e:
        return e.args[0]

    # for each model that is in prod, download the artifacts (which should just be a pkl)
    # grab the experiments
    experiments = project.get_experiments(tag='prod')

    # get the artifact for each experiment, and unzip it
    for experiment in experiments:
        artifact_dir = path.join(ARTIFACTS_DIR, experiment.id)
        experiment.download_artifacts(destination_dir=artifact_dir)
        
        # the downloaded artifact will be in a zip file, so lets extract it
        with ZipFile(artifact_dir + sep + 'output.zip') as zip_ref:
            zip_ref.extractall(path=artifact_dir)
            sleep(0.25) # delay a little as sometimes ZipFile.extractall doesn't report well on windows
        
        # cleanup after the zip extraction
        for filename in listdir(path.join(artifact_dir, 'output')):
            if fnmatch.fnmatch(filename, '*.pkl'):
                rename(path.join(artifact_dir,'output', filename), path.join(artifact_dir,filename))
                shutil.rmtree(path.join(artifact_dir,'output'))
        
        remove(path.join(artifact_dir,'output.zip'))

        # grab the metrics
        logs = experiment.get_logs()
        metrics = {}
        for key, value in logs.items():
            metrics[key] = value['y']

        with open(artifact_dir + sep + 'metrics.json', 'w') as f:
            json.dump(metrics, f)

    return redirect(url_for('case.newCase'))

@bp.route('/registered')
def get_registered_models():
    """ Get metadata about production models from Neptune """
    # connect to neptune
    try:
        project = neptune.init()
    except (MissingProjectQualifiedName):
        return 'NEPTUNE_PROJECT environment variable is missing'
    except (MissingApiToken):
        return 'NEPTUNE_API_TOKEN environment variable is missing'
    except (Exception) as e:
        return e.args[0]

    # get all the experiments that are tagged as "prod"
    experiments = project.get_experiments(tag='prod')

    # pull the id, name, and test dataset scores metrics
    experiment_metadata = []
    for experiment in experiments:
        logs = experiment.get_logs()
        metadata = {
            'id': experiment.id,
            'name': experiment.name,
        }
        for key, value in logs.items():
            if key.startswith('test'):
                metadata[key] = value.y
        experiment_metadata.append(metadata)
    
    return jsonify(experiment_metadata)
