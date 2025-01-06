# Kidney-Disease-Classifciation-MLflow-DVC


## Worflowws

1. Update Config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

```
## How to run?
```
### STEPS:

Clone the repository

```bash
https://github.com/Calivala-86/Kidney-Disease-Classifciation-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda active cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```






[Documentation](https://mlflow.org/docs/lastes/index.html)

```
##### cmd
- mlflow ui
```
### dagshub
[dagshu](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Calivala-86/Kidney-Disease-Classifciation-Deep-Learning-Project-Mlflow-DVC.mlflow"
MLFLOW_TRACKING_USERNAME=Calivala-86 \
MLFLOW_TRACKING_PASSWORD=72b0a74ee983a0ed9376d093985d5810dc7481 \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Calivala-86/Kidney-Disease-Classifciation-Deep-Learning-Project-Mlflow-DVC.mlflow
export MLFLOW_TRACKING_USERNAME=Calivala-86
export MLFLOW_TRACKING_PASSWORD=72b0a74ee983a0ed936d9093985d5810dc7481
```
