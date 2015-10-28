#!/usr/bin/env python
import sys,os
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),os.path.pardir))
import psutil
try:
	import fuzzy.OutputVariable
	import fuzzy.InputVariable
	import fuzzy.defuzzify.Dict
	import fuzzy.fuzzify.Dict
	import fuzzy.storage.fcl.Reader
	print "import ok"
except:
    print "not ok"

try:
	system = fuzzy.storage.fcl.Reader.Reader().load_from_file(sys.argv[1])
	print "yep"
except:
	print "nein"
my_input = {
	"Memory" : 0.0,
	"CPU" : 0.0	
}


my_output = {
	"Output" : 0
}
my_input["Memory"] = 50
my_input["CPU"] = 60

conditions = {
	1.0 : "Realocate",
	2.0 : "Distribuition",
	3.0 : "Do_noting"
}



system.calculate(my_input, my_output)
teste = my_output["Output"]
print conditions[teste]
