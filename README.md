# Gym_Equipment_Predictor
Predicts the name of the equipment from the image uploaded. Model is trained to predict one these classes:
`cable_crossover, lat_pull_down, pec_deck, smith_machine, treadmill`


# Steps to run the project-
1. Go to environment.yml and replace `/home/shreya/anaconda3/`in `prefix: ` with anaconda3 path in your system
2. Run command `conda env create --file environment.yml`
3. Run command `conda activate equipPredictor`
4. Download model `equipment_classfication_model.pth` from  https://drive.google.com/drive/u/0/folders/1iWViYdfW0UcMmKGGzAOFcDdEHhYfvrsc
5. Move `equipment_classfication_model.pth` to the path `Gym_Equipment_Predictor > model`
4. Run `python main.py`
