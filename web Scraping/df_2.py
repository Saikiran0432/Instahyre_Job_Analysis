import json 
import pandas as pd
import requests
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

final_data=[]
for url in urls:
    request=requests.get(url)
    if request.status_code==200:
        request_data=json.loads(request.text)
        data=request_data['objects']
        for new_column in data:
            designation=new_column['title']
            location=new_column['locations']
            required_data={'job_title':designation,'job_location':location}
            final_data.append(required_data)

    else:
        print('request status error',request.status_code)
df=pd.DataFrame(final_data)
excel_file='D:/Project/Project/Table1.xlsx'
df.to_excel(excel_file,index=False)


    

