import pandas as pd
import json
import os
import subprocess
import docker

def get_image(container_name):
    
    output = subprocess.check_output(args=["docker","inspect","--format","{{.Config.Image}}",f"{container_name}"])
    img_name = output.decode("utf-8").split("\n") 
    return img_name[0]

def make_scan_json(img):
    with open("scan.json", "w") as f:
        subprocess.run(["docker", "scan", img, "--json"], stdout=f)
    
def get_vul_array():
        f = open ('scan.json', "r")
        data = json.loads(f.read())
        f.close()
        try:
            vul_array = data[0]['vulnerabilities']
        except KeyError:
             vul_array=data['vulnerabilities']
        return vul_array
        
def feature_extraction(vul_array):
    result=[]
    for i in range (0,len(vul_array)):
        vul_dict=vul_array[i]
        new_dict = {
        "title": vul_dict['title'],
        "CVSSv3": vul_dict['CVSSv3'],
        "severity": vul_dict['severity'],
        "cvssScore": vul_dict['cvssScore'],
        "CVE": vul_dict['identifiers']['CVE']
        }
        result.append(new_dict)
    return result  

def separate_severity(result):
    low_sev = [d for d in result if d['severity'] == 'low']
    med_sev = [d for d in result if d['severity'] == 'medium']
    high_sev = [d for d in result if d['severity'] == 'high']
    low_sev_count=len(low_sev)
    med_sev_count=len(med_sev)
    high_sev_count=len(high_sev)  
    return high_sev,low_sev_count,med_sev_count



def get_high_json(high_sev):
    df_high = pd.DataFrame(high_sev)
    df_high.drop('severity', axis=1, inplace=True)
    df_high['Remote Attack Possibility'] = df_high['CVSSv3'].apply(lambda x: 'possible' if 'AV:N' in x else 'not possible')
    df_high = df_high.rename(columns={'title': 'Vulnerability Type'})
    # convert each row to a dictionary and append to a list
    records = []
    for index, row in df_high.iterrows():
        record = row.to_dict()
        records.append(record)

    # convert the list of dictionaries to a list of JSON strings
    json_records = [json.dumps(record) for record in records]
    return json_records


def scanning(container_name):
    img=get_image(container_name)
    make_scan_json(img)
    array=get_vul_array()
    result=feature_extraction(array)
    high_sev,low_sev_count,med_sev_count=separate_severity(result)
    high_json=get_high_json(high_sev)
    return high_json,low_sev_count,med_sev_count,len(high_sev)
    

    
container_name="gracious_jackson"
high_json,low_sev_count,med_sev_count,high_sev_count=scanning(container_name)
print("Total number of Low Severnity ",low_sev_count)
print("Total number of Medium Severnity ",med_sev_count) 
print("Total number of High Severnity ",high_sev_count)  
print(high_json)