# -*- coding: utf-8 -*-

SWARM_DESCRIPTION =  {
  "includedFields": [
    {
      "fieldName": "sine",
      "fieldType": "float",
      "maxValue": 1.0,
      "minValue": -1.0
    }
  ],
  "streamDef": {
    "info": "sine",
    "version": 1,
    "streams": [
      {
        "info": "sine.csv",
        "source": "file://sine.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },
  "inferenceType": "TemporalAnomaly",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "sine"
  },
  "swarmSize": "medium"
}