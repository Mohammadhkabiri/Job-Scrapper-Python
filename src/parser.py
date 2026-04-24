import time
from src.config import jobvision_payload
import requests

url  = "https://candidateapi.jobvision.ir/api/v1/JobPost/List"
headers =  {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }

def fetch_data () :
    raw_jobs = []
    current_page = 1
    while(True) :
        jobvision_payload["requestedPage"]= current_page
        payload = jobvision_payload

        response = requests.post(url=url , json= payload , headers=headers)
        data = response.json()
        current_page_jobs_list  = data.get("data" ,[]).get("jobPosts", [])
        if(len(current_page_jobs_list) == 0) :
            break
        print(f"✅ تعداد آگهی‌های پیدا شده در صفحه {current_page}: {len(current_page_jobs_list)}")
        raw_jobs.extend(current_page_jobs_list)
        current_page += 1
        time.sleep(2)
    return raw_jobs
