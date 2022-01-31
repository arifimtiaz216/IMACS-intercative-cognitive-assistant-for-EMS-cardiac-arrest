import nltk

import threading
import os

import xlrd

from Tkinter import *
import tkMessageBox

my_path=os.getcwd()
fileLoc = os.path.join(my_path, "Intervention Safety Sheet.xlsx")

#fileLoc="C:\Users\Arif\Desktop\mycode8-filter\Intervention Safety Sheet.xlsx"
#print (hello)
print "Select the intervention from below: \n \n1.12-lead ecg \n2.acetaminophen (tylenol) \n3.adenosine (adenocard) \n4.aed \n5.albuterol \n6.alteplase (activase) \n7.amiodarone (bolus) \n8.amiodarone (drip) \n9.antibiotics \n8.aspirin \n9.assist ventilation (bvm) \n10.atropine \n11.bleeding controlled \n12.blood \n13.burn sheet \n14.calcium chloride \n15.capnography (1) first reading 16.capnography (2) second reading \n17.capnography (3) final reading \n18.cardiac monitor \n19.chest decompression \n20.cold pack \n21.confirm time \n22.cpap \n23.cpr \n24.cricothyrotomy \n25.cyanokit 5g \n26.defibrillation \n27.dexamethasone (decadron) \n28.dextrose 10% \n29.dextrose 25% \n30.dextrose 5% in 0.45% ns \n31.dextrose 50% \n32.diazepam (valium) \n33.diltiazem (cardizem) \n34.diphenhydramine (benadryl) \n35.dobutamine \n36.dopamine \n37.duoneb \n38.endotracheal \n39.enoxaparin \n40.epi-pen (adult) \n41.fentanyl \n42.furosemide (lasix) \n43.glucagon \n44.glutose \n45.heparin \n46.hospital contact \n47.hydralazine (apresoline) \n48.in-line nebulizer \n49.insulin \n50.intraosseus \n51.intubation \n52.ipratropium (atrovent) \n53.iv \n54.king ltsd airway \n55.levalbuterol hcl (xopenex) \n56.lidocaine \n57.magnesium sulfate \n58.medical necessity \n59.midazolam (versed) \n60.naloxone (narcan) \n61.nasopharyngeal airway insertio \n62.neo-synephrine \n63.nicardipine (cardene) \n64.nitroglycerine \n65.nitroprusside \n66.norepinephrine \n67.normal saline \n68.occlusive dressing \n69.ondansetron (zofran) \n70.open airway \n71.oral glucose \n72.orogastric decompression \n78.oropharyngeal airway insertion \n79.oxygen \n80.phenergan \n81.potassium chloride \n82.propofol (diprivan) \n83.pulse oximetry \n84.racemic epinephrine \n85.restraints \n86.resusitation discontinued \n87.rosc \n88.sodium bicarbonate \n89.spinal motion restriction \n90.splinting \n91.suction \n92.synchronized cardioversion \n93.thoracostomy \n94.tourniquet \n95.transcutaneous pacing \n96.travel \n97.vagal maneuver \n98.ventilator \n99.warming blanket \n100.x-collar-only immobilization \n101.ziprasidone (geodon)"

choice=raw_input("Your selection:")

wb=xlrd.open_workbook(fileLoc)
sheet=wb.sheet_by_index(0)

interventionRows=sheet.nrows
interventionCol=sheet.ncols

interventionList=[['NA' for x in range(interventionCol)] for y in range(interventionRows)]

for i in range(interventionRows):
    for j in range(interventionCol):
        interventionList[i][j]=sheet.cell_value(i,j)

riskLevel=0 
riskLevelStr=''       
if (float(str(interventionList[int(choice)+2][2]))>2) or (float(str(interventionList[int(choice)+2][3]))-float(str(interventionList[int(choice)+2][2]))>1) or (float(str(interventionList[int(choice)+2][4]))-float(str(interventionList[int(choice)+2][2]))>1):
    riskLevelStr='High Risk Intervention'
    riskLevel=1
    
if (riskLevel==0) and ((float(str(interventionList[int(choice)+2][2]))==2) or (float(str(interventionList[int(choice)+2][3]))-float(str(interventionList[int(choice)+2][2]))==1) or (float(str(interventionList[int(choice)+2][4]))-float(str(interventionList[int(choice)+2][2]))==1)):
    riskLevelStr='Low Risk Intervention'
    riskLevel=2
    
if (riskLevel==0) and ((float(str(interventionList[int(choice)+2][2]))==1) or (float(str(interventionList[int(choice)+2][3]))-float(str(interventionList[int(choice)+2][2]))==0) or (float(str(interventionList[int(choice)+2][4]))-float(str(interventionList[int(choice)+2][2]))==0)):
    riskLevelStr='Risk-Free Intervention'
    riskLevel=3
    

#print EMT_is
        
# =============================================================================
# matchedCertification=0
# if str(EMT_is) == str(interventionList[int(choice)+2][1]):
#     matchedCertification=1
# =============================================================================

#print sheet.cell_value(100,0)
#print sheet.nrows
#print sheet.ncols

#for i in range(interventionRows):
    #print interventionList[i][1]
    
root = Tk()

if riskLevel==1:
    tkMessageBox.showinfo("Risk Level for this INTERVENTION!",str(riskLevelStr)+"           \n\nCertification Required: "+str(interventionList[int(choice)+2][1]))

elif riskLevel==2:
    tkMessageBox.showinfo("Risk Level for this INTERVENTION!",str(riskLevelStr)+"           \n\nCertification Required: "+str(interventionList[int(choice)+2][1]))

    
elif riskLevel==3:
    tkMessageBox.showinfo("Risk Level for this INTERVENTION!",str(riskLevelStr)+"           \n\nCertification Required: "+str(interventionList[int(choice)+2][1]))
    
#    tkMessageBox.showwarning("Required Info for this INTERVENTION!","YOU DO NOT HAVE THE PERMISSION TO PROCEED WITH THIS INTERVENTION!\n"+str(interventionList[int(choice)+2][1])+" certification required!\n\nRisk Level: "+str(interventionList[int(choice)+2][2])+"\n\nRisk Level if NOT done when indicated: "+str(interventionList[int(choice)+2][3])+"\n\nRisk Level if done when NOT indicated: "+str(interventionList[int(choice)+2][4])+"\n\nPrerequisites: "+str(interventionList[int(choice)+2][5]))

root.destroy()
    
print ("\nDone !")