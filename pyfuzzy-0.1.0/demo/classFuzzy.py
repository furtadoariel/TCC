# -*- coding: utf-8 -*-

import sys,os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),os.path.pardir))
import psutil
import fuzzy.OutputVariable
import fuzzy.InputVariable
import fuzzy.defuzzify.Dict
import fuzzy.fuzzify.Dict
import fuzzy.storage.fcl.Reader

class FuzzySystem(object):

	def __init__(self):
		self._conditions = {
		1.0 : "Overload",
		2.0 : "Underload",
		3.0 : "Ok"
		}
		self._my_input = dict(CPU = [], Memory = [])
		self._my_output = dict(Output = 0)
		self._system = fuzzy.storage.fcl.Reader.Reader().load_from_file(
		"fuzzycontrollanguage.fcl" #caminho do arquivo de regras FCL
		)

	def _make_calculate(self):
		self._system.calculate(self._my_input, self._my_output)
		return self._my_output


	def _set_inputs_avg(self, dict_in):
		for x, k in dict_in.iteritems():
			self._my_input[x] = reduce(lambda x, y: x+y, k) / len(k)
			print x, self._my_input[x]

	def _input_dict(self, memory, cpu):
		self._my_input["Memory"] = memory
		self._my_input["CPU"] = cpu
		return self._my_input
