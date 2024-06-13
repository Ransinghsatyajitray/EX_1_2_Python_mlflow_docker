# EX_1_2_Python_mlflow_docker
Configuring Mlflow to track Hyperparameter from different Experiments and  Create a FastAPI/ Flask API to deploy your model using docker


1. Create a new virtual environment
conda create -n venv python=3.10.14 -y
2. Checkout the created virtual environment
conda env list
3. Activate the virtual environment
conda activate venv 
4. Install all the packages present in the requirements file
pip install -r requirements.txt


5. To check the python version -> python --version


# MLFLOW

Experiment tracking and hypothesis testing persistence
Code structuring for better reproducibility
Model packaging and dependency management.
Evaluating hyperparameter parameter tuning selection boundaries
Comparing the results of model retraining over time.
Reviewing and selecting optimal model for deployment
Manage the lifecycles of the trained models , both pre and post deployment
Deploy models securely to production environments
Audit and review candidate models prior to deployments
Manage deployment dependencies
Reviewing the outcomes of the experimentation and modeling activities
Collaborating with teams to ensure that modeling objectives align with the business goals.


# why in multi class classification average = "weighted" taken in performance calculation
Averaged Precision/Recall...: You combine the per-class precision/recall.. scores into a single metric. This is where the average parameter in precision_score or other scores comes in. This takes in to account class imbalance, This gives more weight to the precision/recall .. of classes that have a larger number of instances, reflecting their importance in your dataset.

# Evidently AI -> The open source ML Observability platform
Evaluate , test and monitor ML Models from validation to production.
It helps in understanding the data quality, data drift , model performance.
