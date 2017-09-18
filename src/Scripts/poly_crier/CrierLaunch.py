#!/usr/bin/env python
import Poly_Chatter
import Poly_Listener
import roslaunch



talker = roslaunch.core.Node('poly_crier','Poly_Chatter.py')
listener = roslaunch.core.Node('poly_crier','Poly_Listener.py')

launch= roslaunch.scriptapi.ROSLaunch()
launch.start()

process1 = launch.launch(talker)
print(process.is_alive())


process2 = launch.launch(listener)
print(process.is_alive())



