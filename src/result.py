
from src.util import create_dataframe
from src.cleaner import get_extracted_job
from src.parser import fetch_data
from src.summary import create_useful_data

jobs_list  = fetch_data()
extracted_jobs = get_extracted_job(jobs_list)

df =create_dataframe(extracted_jobs , "jobvision_data.csv")
report = create_useful_data(df)




