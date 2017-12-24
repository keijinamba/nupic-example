# -*- coding: utf-8 -*-

import os
import pprint as pp

from nupic.swarming import permutations_runner
from swarm_description import SWARM_DESCRIPTION



def swarm(output_dir):
  '''
  Run swarming.

  Args:
    output_dir: a directory name for swarm results.
  '''
  
  swarm_dir = os.path.abspath(output_dir)
  if not os.path.exists(swarm_dir):
    os.mkdir(swarm_dir)
  
  f = open(os.path.join(swarm_dir, '__init__.py'), 'w')
  f.close()

  model = permutations_runner.runWithConfig(
    SWARM_DESCRIPTION,
    {"maxWorkers": 4, "overwrite": True},
    outputLabel = "sine",
    outDir = swarm_dir,
    permWorkDir = swarm_dir
  )

  f = open(os.path.join(swarm_dir, "model_0", '__init__.py'), 'w')
  f.close()

  return model



if __name__ == "__main__":

  result = swarm("swarm")
  print("Swarming results:")
  pp.pprint(result)
