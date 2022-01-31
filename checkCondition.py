# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 02:31:45 2020

@author: mir6zw
"""
#import threading

import settings

#import threads
import cardiac_CPR_BVM
import defibVIFIB
import airway_chest
import vascular_rosc
import epinephrine
import flush_med_dilute

#import string
#from Tkinter import *
#import tkMessageBox
        
def check_condition(string):

    if('not cardiac arrest' in string or 'not a cardiac arrest' in string):
        defibVIFIB.not_cardiac("Not Cardiac Arrest Case!")
    elif('not ventricular fibrillation' in string or 'not a ventricular fibrillation' in string):
        defibVIFIB.not_VFIB("Not VFIB Case!")
#----------------------------------------------------------
    elif ('is in cardiac arrest' in string):
        cardiac_CPR_BVM.cardiac_arrest_found("Cardiac Arrest Case!")
        return 0
    elif ('starting compressions' in string):
        cardiac_CPR_BVM.CPR_protocols("Compression starting!")
        return 0
#----------------------------------------------------------        
    elif ('start bvm' in string):
        cardiac_CPR_BVM.start_CPR_BVM_DX("BVM Started-", string)
        return 0
#----------------------------------------------------------        
    elif ('chest rise' in string):
        airway_chest.chest_rise_airway_breathing("Chest Rise Found",string)
        return 0          
#----------------------------------------------------------    
    elif ('defibrillation pads attached' in string):
        defibVIFIB.defibrillation_pads("Defibrillation Pads Attached-")
        return 0
    elif ('is in ventricular fibrillation' in string):
        defibVIFIB.VFIB("VFIB-")
        return 0
    elif ('defibrillate at 120 Joules' in string or 'defibrillating at 120 joules' in string):
        defibVIFIB.defibrillation_protocols120("First DEFIB 120 Joules")
        return 0
    elif ('defibrillate at 150 joules' in string or 'defibrillating at 150 joules' in string):
        defibVIFIB.defibrillation_protocols150("Second DEFIB 150 Joules")
        return 0
    elif ('defibrillate at 200 joules' in string or 'defibrillating at 200 joules' in string):
        defibVIFIB.defibrillation_protocols200("Second DEFIB 150 Joules")
        return 0
#----------------------------------------------------------    
    elif ('no rosc' in string):
        vascular_rosc.ROSC_no_protocols("No ROSC")
        return 0
#----------------------------------------------------------    
    elif ('start an iv' in string):
        vascular_rosc.vascular_access("Vascular Access")
        return 0
    elif ('try for intubation' in string):
        vascular_rosc.vascular_access_intubation("Intubation Attempt")
        return 0
#----------------------------------------------------------    
    elif ('airway is secured' in string):
        airway_chest.airway_breathing_protocols("Airway started",string)
        return 0
#-----------------------------------------------------------
    elif ('io is in place' in string):
        airway_chest.circulation_IO_protocols("IO start protocol", string)
        return 0
#-----------------------------------------------------------
    elif ('how do you dilute' in string and 'amiodarone' in string):
        flush_med_dilute.dilute_amiodarone("Dilute Amiodarone")
        return 0
#---------------------------------------------------------- 
        
    elif ('post medication flush' in string):
        flush_med_dilute.post_medication_flush("Post medication check")
        if('amiodarone' in string):
            flush_med_dilute.med_details_amiodarone(string)
        return 0
#----------------------------------------------------------
        
    elif ('epinephrine' in string):
        if(settings.epinephrine_flag==0):
            epinephrine.epinephrine_sequence_protocols("Epinephrine protocol")
            settings.epinephrine_flag=1
        flush_med_dilute.med_details_epinephrine(string)
        return 0
    
    elif ('amiodarone' in string):
        flush_med_dilute.med_details_amiodarone(string)

#----------------------------------------------------------  

# =============================================================================
#     elif ('medication cross check' in string):
#         #medication_cross_check("Medication Cross Check")
#         print("YO!")
#         return 1
# =============================================================================
#----------------------------------------------------------        
    elif ('have rosc' in string):
        vascular_rosc.ROSC_yes_protocols("ROSC found")
        return 0
#----------------------------------------------------------
#----------------------------------------------------------   
    else:
        #print("No Match Keyword!")
        return 0

