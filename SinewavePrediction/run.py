# -*- coding: utf-8 -*-


import csv

from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.modelfactory import ModelFactory
import nupic_output

from swarm.model_0.model_params import MODEL_PARAMS



def createModel():
  model = ModelFactory.create(MODEL_PARAMS)
  model.enableInference({
    "predictedField": "sine"
  })
  return model



def runModel(model):
  inputFilePath = "sine.csv"
  inputFile = open(inputFilePath, "rb")
  csvReader = csv.reader(inputFile)
  csvReader.next()
  csvReader.next()
  csvReader.next()

  shifter = InferenceShifter()
  output = nupic_output.NuPICPlotOutput("Sine")

  for row in csvReader:
    
    angle = float(row[0])
    sine  = float(row[1])

    result = model.run({
      "angle": angle,
      "sine": sine
    })

    result = shifter.shift(result)

    output.write(angle, sine, result)

  inputFile.close()
  output.close()


def run():
  model = createModel()
  runModel(model)


if __name__ == "__main__":
  run()
