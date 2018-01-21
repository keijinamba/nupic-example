# Sine wave prediction

## Preprocess

Install Mysql for swarming.(OS: MacOS)
```sh
mysql.server start
```

Generate sine wave data.
```sh
python generate_data.py
```

## Run

１）Swarming + Model
```sh
# Run the swarming to get good parameters.
python swarm.py

# Run the model.
python run.py
```

２）NetworkAPI
```sh
python network.py
```