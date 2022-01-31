# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:44:02 2020

@author: mir6zw
"""

import settings
import datetime

import fpdf

def writeF(fileLog):
    
    length=len(settings.narrative)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.narrative[i])+"\n\n")
    
    length=len(settings.epinephrine_medication_record_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.epinephrine_medication_record_list[i])+"\n\n")
        
    length=len(settings.amiodarone_medication_record_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.amiodarone_medication_record_list[i])+"\n\n")
        
    length=len(settings.sequential_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.sequential_list[i])+"\n\n")
        
    length=len(settings.chest_rise)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.chest_rise[i])+"\n\n")
        
    length=len(settings.bvm_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.bvm_list[i])+"\n\n")
        
    length=len(settings.defib_pad)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.defib_pad[i])+"\n\n")
        
    length=len(settings.intubation_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.intubation_list[i])+"\n\n")
        
    length=len(settings.airway_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.airway_list[i])+"\n\n")
        
    length=len(settings.rosc_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.rosc_list[i])+"\n\n")
        
    length=len(settings.io_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.io_list[i])+"\n\n")
        
        
def writeS(fileLog):
    
    length=len(settings.narrative)
    i=0
    for i in range(length):
        fileLog.write(str(settings.narrative[i])+". ")
    fileLog.write("\n\n")
    
    length=len(settings.sequential_list)
    i=0
    for i in range(length):
        fileLog.write(str(i)+". "+str(settings.sequential_list[i])+"\n\n")
        
def writePDF():
    settings.suggestions.append(str(datetime.datetime.now())[11:19]+": Summary report PDF created!\n----------------\n")
    
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
#    pdf.set_font("Arial", size=12)
    pdf.set_font('Arial', 'BU', 20)
    pdf.set_fill_color(255,255,0)
    pdf.cell(0, 10, 'CARDIAC ARREST RESCUE', 0, 1, 'C')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(60, 8, 'ALBEMERLE COUNTY', 0, 0, 'L')
    pdf.cell(0, 8, 'INITIAL PATIENT CARE REPORT', 0, 1, 'R')
    
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(60, 3, '460 Stagecoach Drive, Suite F', 0, 0, 'L')
    pdf.cell(0, 3, 'PPCR will be available on', 0, 1, 'R')
    
    pdf.cell(60, 3, 'Charlottesville, VA 22902-6489', 0, 0, 'L')
    pdf.cell(0, 3, 'Hospital Bridge within 24 hours', 0, 1, 'R')
    
    pdf.cell(60, 7, 'Phone: (434)296-5833   -  OEMS Agency #00939', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'PATIENT INFORMATION', 1, 1, 'L', True)
    
    pdf.set_font('Arial', '', 14)
    pdf.multi_cell(0, 9, 'NAME: '+str(settings.ptName), 1, 1, 'L')
    pdf.cell(0, 9, 'ADDRESS: ', 1, 1, 'L')
    pdf.cell(90, 9, 'CITY: ', 1, 0, 'L')
    pdf.cell(45, 9, 'STATE: ', 1, 0, 'L')
    pdf.cell(60.4, 9, 'ZIP: ', 1, 1, 'L')
    pdf.cell(90, 9, 'DOB: ', 1, 0, 'L')
    pdf.cell(0, 9, 'SSN: ', 1, 1, 'L')
    pdf.cell(90, 9, 'AGE: ', 1, 0, 'L')
    pdf.cell(0, 9, 'SEX: ', 1, 1, 'L')
    
# =============================================================================
#     length=len(settings.narrative)
#     i=0
#     for i in range(length):
#         pdf.write(5,str(settings.narrative[i])+". ")
#     pdf.ln()
#     pdf.ln()
# 
# =============================================================================
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(255,255,0)
    
    pdf.set_font('Arial', '', 16)
    pdf.cell(0, 8, '', 0, 1, 'C')
    pdf.cell(0, 10, 'ORIGINAL TRANSCRIPTION', 1, 1, 'L', True)
    
    narrativeS='[patient name]:'
    length=len(settings.narrative)
    i=0
    for i in range(length-1):
        narrativeS=narrativeS+str(settings.narrative[i]+". ")
    
    pdf.set_font('Arial', '', 14)
    pdf.multi_cell(0, 7, 'Narrative: '+narrativeS, 1, 1, 'L')
    
# =============================================================================
#     length=len(settings.sequential_list)
#     i=0
#     for i in range(length):
#         pdf.write(5,str(i)+". "+str(settings.sequential_list[i]))
#         pdf.ln()
#         pdf.ln()
# =============================================================================
    
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(255,255,0)
    
    pdf.set_font('Arial', '', 16)
    pdf.cell(0, 8, '', 0, 1, 'C')
    pdf.cell(0, 10, 'SEQUENTIAL INTERVENTIONS', 1, 1, 'L', True)
    
    narrativeSS=''
    length=len(settings.sequential_list)
    i=0
    for i in range(length):
        narrativeSS=narrativeSS+str(settings.sequential_list[i]+". ")
    
    pdf.set_font('Arial', '', 14)
    pdf.multi_cell(0, 7, 'Interventions: \n'+narrativeSS+'\n', 1, 1, 'L')

    pdf.output("Cardiac Arrest Summary for "+str(settings.ptName)+".pdf")
    
    
if __name__=="__main__":    
    
# =============================================================================
#     data=[1,2,3,4,5,6]
#     
#     pdf = fpdf.FPDF(format='letter')
#     pdf.add_page()
# #    pdf.set_font("Arial", size=12)
#     pdf.set_font('Arial', 'BU', 20)
#     
#     for i in data:
#         pdf.write(5,str(i))
#         pdf.ln()
#     pdf.output("testings.pdf")
# =============================================================================

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()    
    pdf.set_font('Arial', 'BU', 20)
    pdf.set_fill_color(255,255,0)
    pdf.cell(0, 10, 'FIRE RESCUE', 0, 1, 'C')
    
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(60, 8, 'ALBEMERLE COUNTY', 0, 0, 'L')
    pdf.cell(0, 8, 'INITIAL PATIENT CARE REPORT', 0, 1, 'R')
    
    pdf.set_font('Arial', 'B', 7)
    pdf.cell(60, 3, '460 Stagecoach Drive, Suite F', 0, 0, 'L')
    pdf.cell(0, 3, 'PPCR will be available on', 0, 1, 'R')
    
    pdf.cell(60, 3, 'Charlottesville, VA 22902-6489', 0, 0, 'L')
    pdf.cell(0, 3, 'Hospital Bridge within 24 hours', 0, 1, 'R')
    
    pdf.cell(60, 7, 'Phone: (434)296-5833   -  OEMS Agency #00939', 0, 1, 'L')
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'PATIENT INFORMATION', 1, 1, 'L', True)
    
    pdf.set_font('Arial', '', 14)
    pdf.multi_cell(0, 9, 'NAME: ', 1, 1, 'L')
    pdf.cell(0, 9, 'ADDRESS: ', 1, 1, 'L')
    pdf.cell(90, 9, 'CITY: ', 1, 0, 'L')
    pdf.cell(45, 9, 'STATE: ', 1, 0, 'L')
    pdf.cell(60.4, 9, 'ZIP: ', 1, 1, 'L')
    pdf.cell(90, 9, 'DOB: ', 1, 0, 'L')
    pdf.cell(0, 9, 'SSN: ', 1, 1, 'L')
    pdf.cell(90, 9, 'AGE: ', 1, 0, 'L')
    pdf.cell(0, 9, 'SEX: ', 1, 1, 'L')
    
    pdf.output("testings.pdf")
        
