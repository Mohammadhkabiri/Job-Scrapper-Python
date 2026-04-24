import re
import pandas as pd

def get_company_score (company_score_info) :
    company_score = None
    if (not company_score_info) :
        company_score = "نظری ثبت نشده است"      
    else :
        company_score = company_score_info    
    return company_score


def get_salary(salary_info) :
    salary = "توافقی"
    if salary_info:
        salary = salary_info.get('titleFa', 'توافقی')
    else:
        salary = 'توافقی / نامشخص'
    return salary         

def get_average_salary(text):
    nums = re.findall(r"\d+" ,str(text))
    if(nums) :
        nums = [int(x) for x in nums]
        return sum(nums) / len(nums)
    return None

def create_dataframe(data , file_name) :
    df = pd.DataFrame(data=data)
    df.to_csv(file_name , index=False , encoding="utf-8-sig")
    return df
