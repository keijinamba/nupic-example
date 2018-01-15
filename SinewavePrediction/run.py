# -*- coding: utf-8 -*-


import csv

from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.modelfactory import ModelFactory
import nupic_output

from swarm.model_0.model_params import MODEL_PARAMS


def createModel():
  '''
  Create nupic.frameworks.opf.model.Model from ModelFactory.

  Return:
    An opf model.
  '''

  model = ModelFactory.create(MODEL_PARAMS)
  model.enableInference({
    "predictedField": "sine"
  })
  return model



def runModel(model, file_name):
  '''
  Run predictions with a given model.

  Args:
    model: Opf model.
  '''

  input_file = open(file_name, "rb")
  csv_reader = csv.reader(input_file)
  csv_reader.next()
  csv_reader.next()
  csv_reader.next()

  shifter = InferenceShifter()
  output = nupic_output.NuPICPlotOutput("Sine", show_anomaly_score=True)

  for row in csv_reader:
    
    angle = float(row[0])
    sine  = float(row[1])

    result = model.run({
      "angle": angle,
      "sine": sine
    })

    result = shifter.shift(result)

    inference     = result.inferences['multiStepBestPredictions'][1]
    anomaly_score = result.inferences['anomalyScore']

    output.write(sine, inference, anomaly_score)

  input_file.close()
  output.close()



if __name__ == "__main__":
  model = createModel()
  runModel(model=model, file_name="sine.csv")
