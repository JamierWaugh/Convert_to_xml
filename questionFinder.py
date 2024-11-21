import pandas as pd
from pathlib import Path

spreadsheet = "A level Questions.xlsx" #Added variables and function for more scalability
output_file = "output.xml"

def saveToXml(spreadsheet, output_file):
    path_load = Path(__file__).parent / spreadsheet #Generates relative path
    path_write = Path(__file__).parent / output_file
    type = path_load.suffix.lower()
    if type in [".xls", ".xlsx"]: #Enabled functionality for excel, json, csv and parquet
        df = pd.read_excel(path_load) #turn excel spreadsheet into panda dataframe
    elif type == ".json":
        df = pd.read_json(path_load)
    elif type == ".csv":
        df = pd.read_csv(path_load)
    elif type == ".parquet":
        df = pd.read_parquet(path_load)

    xml_data = df.to_xml(root_name="data", row_name="record") #convert panda dataframe into xml

    try:  #Error checking
        # Save the XML string to a file
        with path_write.open("w", encoding = "utf-8") as file: 
            file.write(xml_data) #Writes data to output.xml
            file.close()
        print("DataFrame successfully saved to output.xml")
    except:
        print("DataFrame failed to save to output.xml")

saveToXml(spreadsheet, output_file)