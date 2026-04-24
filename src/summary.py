import pandas as pd
from src.util import get_average_salary

def add_salary_features(df) :
    df_copy= df.copy()
    df_copy['میانگین حقوق (میلیون)'] = df_copy['حقوق'].apply(get_average_salary)
    return df_copy


def calculate_statistics(df) :
    
    total_jobs = len(df)
      
    top_companies = df["شرکت"].value_counts().head(5).reset_index()
    top_companies.columns = ['شرکت', 'تعداد آگهی']
    
    top_category = df["حوزه شغلی"].value_counts().head(5).reset_index()
    top_category.columns = ["حوزه شغلی" , "تعداد آگهی"]
    
    top_cities = df["شهر"].value_counts().head(5).reset_index()
    top_city_name = top_cities.iloc[0]['شهر'] if not top_cities.empty else "نامشخص"
    top_cities.columns = ['شهر', 'تعداد آگهی']
    
    transparent_salary = df[~df['حقوق'].str.contains('توافقی', na=False)]
    percentage = (len(transparent_salary) / total_jobs) * 100
    overall_avg_salary = df['میانگین حقوق (میلیون)'].mean()
    
    summary_data = pd.DataFrame({
        "شاخص": ["تعداد کل آگهی‌ها", "درصد حقوق شفاف", "میانگین حقوق بازار (میلیون تومان)", "پرتقاضاترین شهر"],
        "مقدار": [total_jobs, f"% {percentage:.2f}", f"{overall_avg_salary:.2f}", top_city_name]
    })
    
    return  { "total_jobs": total_jobs,"top_companies": top_companies,"top_cities": top_cities,"top_category": top_category ,"percentage": percentage ,"summary_data" : summary_data}


def save_data_csv(stats) :
    stats["top_companies"].to_csv("top_companies.csv", index=False, encoding="utf-8-sig")
    stats["top_cities"].to_csv("top_cities.csv", index=False, encoding="utf-8-sig")
    stats["top_category"].to_csv("top_category.csv", index = False , encoding = "utf-8-sig")
    stats["summary_data"].to_csv("summary_stats.csv", index=False, encoding="utf-8-sig")



def create_useful_data(df) :
     df_processed = add_salary_features(df)
     stats = calculate_statistics(df_processed)
     save_data_csv(stats)
