from src.util import get_company_score,get_salary
def get_extracted_job(raw_data_list) :
    processed_jobs = []
    for job in raw_data_list : 
    
        title = job.get("title" , "unknown")
        categories = job.get("jobCategories", [])
        jobCategorie = categories[0].get("titleFa", "unknown") if categories else "unknown" 
        
        company = job.get("company") or {}
        company_name = company.get("nameFa", "unknown")
        company_score_info = company.get("companyScore" , "نظری ثبت نشده است")
        
        location = job.get('location', {}).get('city', {})
        city_name = location.get('titleFa', "unknown")
        
        salary_info = job.get('salary')
        labels = job.get("labelDetails", [])
        labels_text = "، ".join([label.get("title", "") for label in labels]) if labels else "ندارد"
            
        processed_jobs.append({
            "حوزه شغلی" : jobCategorie,
            'عنوان شغلی': title,
            'شرکت': company_name,
            'شهر': city_name,
            'حقوق': get_salary(salary_info=salary_info),
            'برچسب‌های آگهی': labels_text,
            "نمره شرکت" : get_company_score(company_score_info=company_score_info)
        })  
    return processed_jobs 
