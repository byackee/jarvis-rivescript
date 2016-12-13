#!/usr/bin/python
# -*-coding:Utf-8 -*
'''
Created on dec 20215

@author: Alex F

Version 1: 
'''

import rxv
import sys
import simplejson

params=sys.argv[1]
tmp=params.split("_")
arg=tmp[0]
iprx=tmp[1]
model=tmp[2]

if arg=='find':
	receivers = rxv.find()
	print(receivers)
	#rx = receivers[0]
else:
		rx = rxv.RXV("http://192.168.2.55:80/YamahaRemoteControl/ctrl", "RX-V477")
		#syntax=r'[<RXV model_name="RX-V477" ctrl_url="http://192.168.0.13:80/YamahaRemoteControl/ctrl" at 0x76b40950>]'
		template='http://'+iprx+'/YamahaRemoteControl/ctrl'
		
		rx = rxv.RXV(template, model)
		
		if arg=="10":
			rx.input='NET RADIO'
			code='Radio'
		elif arg=="1":
			rx.input="HDMI1"
			code='HDMI1'
		elif arg=="2":
			rx.input="HDMI2"
			code='HDMI2'
		elif arg=="3":
			rx.input="HDMI3"
			code='HDMI3'
		elif arg=="4":
			rx.volume=rx.volume+5
			code='Son monté'
		elif arg=="5":
			rx.volume=rx.volume-5
			code='Son baissé'
		elif arg=="6":
			rx.on = True
			code='RX ON'
		elif arg=="0":
			rx.on = False
			code='RX OFF'
		elif arg=="11":
			code=rx.inputs()
			


		data = simplejson.dumps({"status": code})
		print data
	
		
