#!/usr/bin/env python
import sys,os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),os.path.pardir))
import psutil
import fuzzy.OutputVariable
import fuzzy.InputVariable
import fuzzy.defuzzify.Dict
import fuzzy.fuzzify.Dict
import fuzzy.storage.fcl.Reader
system = fuzzy.storage.fcl.Reader.Reader().load_from_file(sys.argv[1])





my_input = {
	"Memory" : [],
	"CPU" : []
}


my_output = {
	"Output" : 0
}
my_input["Memory"].append(70)
my_input["Memory"].append(70)
my_input["Memory"].append(70)
my_input["Memory"].append(70)
my_input["CPU"].append(80)
my_input["CPU"].append(80)
my_input["CPU"].append(80)
my_input["CPU"].append(80)


#funcao para fazer a media da lista de entradas
for x, k in my_input.iteritems():
	print x, reduce(lambda x, y: x + y, k) / len(k)

conditions = {
	1.0 : "Realocate",
	2.0 : "Distribuition",
	3.0 : "Do_nothing"
}



system.fuzzify(my_input)#, my_output)
system.defuzzify(my_output)
print my_output
#teste = my_output["Output"]
#print conditions[teste]
