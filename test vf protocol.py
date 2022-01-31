import nltk
#nltk.download()
from nltk import sent_tokenize
from nltk import word_tokenize

import string
from Tkinter import *
import tkMessageBox


cp_bag_valve_mask=1
cp_lungs_clear_to_auscultation_bilaterally_or_bilateral_chest_rise=2
cp_autopulse_in_place_or_cpr_initiated=3
cp_intraosseous_access_after_attempting_intravenous_access_for_ninety_seconds=4
cp_first_defibrillation=5
cp_second_defibrillation=6
cp_third_defibrillation=7
cp_continued_cpr=8
cp_switch_every_five_minutes_from_start_of_CPR_initiation=9
cp_administration_of_IVP=10
cp_administration_of_post_medication_flush=11
cp_Amiodarone_IVP=12
cp_epinephrine_or_antiarrhythmic_sequence_every_three_minutes=13
cp_amiodarone_drip_hundred_fifty_mg_over_ten_mins_via_IV_pump=14

cpList=["","Check bag valve mask","Check bilateral chest rise","Check CPR initiation","Check intraosseous access","Check defibrilations","Check defibrilations","Check defibrilations","Check CPR Continuation","Check provider switch","Check IVP administration","Check post medication flush","Check Amiodarone IVP","Check epinephrine sequence","Check Amiodarone drip"]


op_intubation_or_oropharyngeal_airway=1
op_oro_gastric_tube_in_place_with_suctioning=2
op_dilution_of_hundred_fifty_mg_amiodarone_in_hundred_ml_D5W_to_yield_one_point_five_mg_mL_concentration=3

opList=[" ","Check intubation or oropharyngeal airway","Check oro gastric tube in place with suctioning", "Check dilution of hundred fifty mg amiodarone in hundred ml D5W to yield one point five mg mL concentration"]


f=open("vf test1.txt", "r")
contents=f.read()
contents=string.lower(contents)
#print contents

sents=nltk.sent_tokenize(contents)
for oneSent in sents:
    if ("bag-mask valve is initialed" in oneSent):
        cp_bag_valve_mask=0

    if ("intubation is in place" in oneSent):
        op_intubation_or_oropharyngeal_airway=0

    if ("lungs clear to auscultation bilaterally" in oneSent):
        cp_lungs_clear_to_auscultation_bilaterally_or_bilateral_chest_rise=0 
        
    if ("cpr is initiated" in oneSent):
        cp_autopulse_in_place_or_cpr_initiated=0    

    if ("intraosseous access after attempting intravenous access for 90 seconds" in oneSent):
        cp_intraosseous_access_after_attempting_intravenous_access_for_ninety_seconds=0
        
    if ("oro-gastric tube in place" in oneSent):
        op_oro_gastric_tube_in_place_with_suctioning=0

    if ("first defibrillation at 120 joules" in oneSent):
        cp_first_defibrillation=0

    if ("second defibrillation at 150 joules" in oneSent):
        cp_second_defibrillation=0
        
    if ("third defibrillation at 200 joules" in oneSent):
        cp_third_defibrillation=0
        
    if ("cpr continued" in oneSent):
        cp_continued_cpr=0
        
    if ("providers switch every 5 minutes" in oneSent):
        cp_switch_every_five_minutes_from_start_of_CPR_initiation=0
        
    if ("administration of 1:10,000 1mg ivp" in oneSent):
        cp_administration_of_IVP=0
        
    if ("administration of post-medication flush" in oneSent):
        cp_administration_of_post_medication_flush=0
        
    if ("amiodarone 300 mg ivp" in oneSent):
        cp_Amiodarone_IVP=0
        
    if ("epinephrine/antiarrhythmic sequence every 3 minutes" in oneSent):
        cp_epinephrine_or_antiarrhythmic_sequence_every_three_minutes=0

    if ("amiodarone drip 150mg over 10 mins" in oneSent):
        cp_amiodarone_drip_hundred_fifty_mg_over_ten_mins_via_IV_pump=0
        
    if ("dilution of 150mg amiodarone in 100ml d5w to yield 1.5mg/ml concentration" in oneSent):
        op_dilution_of_hundred_fifty_mg_amiodarone_in_hundred_ml_D5W_to_yield_one_point_five_mg_mL_concentration=0
        

  
#words=nltk.word_tokenize(contents)
#print words


root = Tk()
tkMessageBox.showinfo("!!! MISSING CRITICAL INFO !!!",
                      cpList[cp_bag_valve_mask]+"\n"+cpList[cp_lungs_clear_to_auscultation_bilaterally_or_bilateral_chest_rise]+"\n"+cpList[cp_autopulse_in_place_or_cpr_initiated]+"\n"+cpList[cp_intraosseous_access_after_attempting_intravenous_access_for_ninety_seconds]+"\n"+cpList[cp_first_defibrillation]+"\n"+cpList[cp_second_defibrillation]+"\n"+cpList[cp_third_defibrillation]+"\n"+cpList[cp_continued_cpr]+"\n"+cpList[cp_switch_every_five_minutes_from_start_of_CPR_initiation]+"\n"+cpList[cp_administration_of_IVP]+"\n"+cpList[cp_administration_of_post_medication_flush]+"\n"+cpList[cp_epinephrine_or_antiarrhythmic_sequence_every_three_minutes]+"\n"+cpList[cp_Amiodarone_IVP]+"\n"+cpList[cp_amiodarone_drip_hundred_fifty_mg_over_ten_mins_via_IV_pump])

tkMessageBox.showinfo("--- MISSING OPTIONAL INFO ---", opList[op_intubation_or_oropharyngeal_airway]+"\n"+opList[op_oro_gastric_tube_in_place_with_suctioning]+"\n"+opList[op_dilution_of_hundred_fifty_mg_amiodarone_in_hundred_ml_D5W_to_yield_one_point_five_mg_mL_concentration])

root.destroy()

print "\nDone !"