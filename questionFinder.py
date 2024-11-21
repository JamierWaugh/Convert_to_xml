import pandas as pd
from pathlib import Path

path_load = Path(__file__).parent / "A level Questions.xlsx" #Generates relative path
path_write = Path(__file__).parent / "output.xml"

df = pd.read_excel(path_load) #turn excel spreadsheet into panda dataframe

xml_data = df.to_xml(root_name="data", row_name="record") #convert panda dataframe into xml

try:  #Error checking
    # Save the XML string to a file
    with path_write.open("w", encoding = "utf-8") as file: 
        file.write(xml_data) #Writes data to output.xml
        file.close()
    print("DataFrame successfully saved to output.xml")
except:
    print("DataFrame failed to save to output.xml")
