import utils as ut

base_url = "https://dumps.wikimedia.org/other/pageviews/"

years = ["2015", "2016", "2017", "2018"]

months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

for year in years:
    
    month_urls = []
    
    url = base_url+year
    month_urls.extend([url+"/"+year+"-"+month+"/" for month in months])


    all_urls = []
    
    for url in month_urls:
        all_urls.extend(ut.get_links(url))
    
    
    with open("file_names/files_"+year+".txt", "w") as f:
        for url in all_urls:
            f.write(url+"\n")
        f.close()
