from TemplateLoader import TemplateLoader as T
from ReplacementLoader import ReplacementLoader as R
from EmailGenerator import EmailGenerator as EG
from EmailWriter import EmailWriter as EW

try:
    Template = T("Mail Merge/Input/Letters/starting_letter.txt")
    Replace = R("Mail Merge/Input/Names/invited_names.txt")
    Generate = EG(Template, Replace)
    Writer = EW("./100DaysOfCode/Intermediate/Day 24/Mail Merge/Output/ReadyToSend", Generate)
    print("✅ All emails were generated successfully.")
except Exception as e:
    print(f"❌ Erreur : {e}")