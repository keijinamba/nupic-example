#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from collections import deque
from abc import ABCMeta, abstractmethod
from nupic.data.inference_shifter import InferenceShifter
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

WINDOW = 420


class Graph(object):


  def __init__(self, params):

    self.setParams(params)

    plt.ion()
    plt.figure(figsize=self.figsize)

    gs = gridspec.GridSpec(2, 1, height_ratios=[3,1])

    plt.title(self.title)
    plt.ylabel(self.y_label)

    self.actual_history      = deque([0.0] * WINDOW, maxlen=WINDOW)
    self.predicted_histories = [ deque([0.0] * WINDOW, maxlen=WINDOW) for i in range(self.prediction_num) ]
    
    if self.anomaly:
      self.anomaly_score = deque([0.0] * WINDOW, maxlen=WINDOW)
      plt.subplot(gs[0])
    
    self.actual_line,     = plt.plot(range(WINDOW), self.actual_history)
    self.predicted_lines = [ plt.plot(range(WINDOW), history)[0] for history in self.predicted_histories ]

    plt.legend(tuple(['actual'] + self.line_labels), loc=3)

    if self.anomaly:
      plt.subplot(gs[1])
      self.anomaly_score_line, = plt.plot(range(WINDOW), self.anomaly_score, 'r-')
      plt.legend(tuple(['anomaly score']), loc=3)

    y_lim_init = self.y_lim if self.y_lim is not "auto" else (0, 0)
    
    self.actual_line.axes.set_ylim(y_lim_init)
    [ line.axes.set_ylim(y_lim_init) for line in self.predicted_lines ]
    if self.anomaly:
      self.anomaly_score_line.axes.set_ylim(y_lim_init)



  def write(self, value, inferences, anomaly_score = None):
    self.append(value, inferences, anomaly_score)

    self.actual_line.set_ydata(self.actual_history)
    [ line.set_ydata(self.predicted_histories[i]) for i, line in enumerate(self.predicted_lines) ]
    
    if self.anomaly:
      self.anomaly_score_line.set_ydata(self.anomaly_score)
    
    if self.y_lim == "auto":
      self.updateYLim()
    
    plt.pause(0.001)
  

  def append(self, value, inferences, anomaly_score = None):
    if inferences is None:
      return
    
    if not isinstance(inferences, list):
      inferences = [inferences]
    
    self.actual_history.append(value)
    [ history.append(inferences[i]) for i, history in enumerate(self.predicted_histories) ]
    
    if not self.anomaly:
      return
    
    if anomaly_score is None:
      return

    self.anomaly_score.append(anomaly_score)
  

  def updateYLim(self):
    lim_actual    = min(self.actual_history) - 1.0, max(self.actual_history) + 1.0
    lim_predictions = [ (min(history) - 1.0, max(history) + 1.0) for history in self.predicted_histories ]

    self.actual_line.axes.set_ylim(lim_actual)
    [ line.axes.set_ylim(lim_predictions[i]) for i, line in enumerate(self.predicted_lines) ]

  
  
  def setParams(self, params):
    self.title          = params['title']          if 'title'          in params else ''
    self.figsize        = params['figsize']        if 'figsize'        in params else (14, 10)
    self.line_labels    = params['line_labels']    if 'line_labels'    in params else ['predicted']
    self.y_label        = params['y_label']        if 'y_label'        in params else 'Y'
    self.y_lim          = params['y_lim']          if 'y_lim'          in params else (-1, 1)
    self.prediction_num = params['prediction_num'] if 'prediction_num' in params else 1
    self.anomaly        = params['anomaly']        if 'anomaly'        in params else False


  def close(self):
    plt.ioff()
    plt.show()
