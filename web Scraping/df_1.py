import requests
import json
import pandas as pd

urls = ["https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=0",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=10",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=20",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=30",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=40",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=50",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=60",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=70",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=80",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=90"
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=100",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=110",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=120",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=130",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=140",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=150",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=160",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=170",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=180",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=190",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=200",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=210",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=220",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=230",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=240",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=250",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=260",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=270",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=280",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=290",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=300",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=310",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=320",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=330",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=340",
        "https://www.instahyre.com/api/v1/job_search?company_size=0&isLandingPage=true&job_type=0&offset=350"]

total_data = []
for url in urls:
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        response_data = json.loads(response.text)
        data = response_data['objects']
        for uidata in data:
            companyname = uidata['employer']['company_name']
            
            founded = uidata['employer']['company_founded']
            location = uidata['locations']
            employees_count=uidata['employer']['employee_count']
            
            
            
            finaldata = {"Company":companyname,"Founded":founded,"Location":location,"employees_count":employees_count}
            
            total_data.append(finaldata)
            
    else:
        print("Request failed with status code:", response.status_code)
df = pd.DataFrame(total_data)
excel_filename = "D:/Project/Project/Table2.xlsx"
df.to_excel(excel_filename, index=False)