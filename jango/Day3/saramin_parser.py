from bs4 import BeautifulSoup
import requests
'''
#select 추천 

company_names = html.select('.company_name')
recruit_names = html.select('.recruit_name')
recruit_conditions = html.select('.list_recruit_condition')
for company_name,recruit_name,recruit_condition in zip(company_names,recruit_names,recruit_conditions):
    print(f'{company_name.text}-{recruit_name.text}-{recruit_condition.text}')


'''
query = {
     '분야 전체보기':{
         'name': 'cat_cd',
         '웹개발 전체' : '404'
     },
     '세부분야 보기':{
         'name':'cat_key',
         'IOS':'40701'
     }
} 

#url = f'http://www.saramin.co.kr/zf_user/jobs/list/job-category?{query["분야 전체보기"]["name"]}={query["분야 전체보기"]["웹개발 전체"]}&panel_type=&search_optional_item=n&search_done=y&panel_count=y'

    #http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&search_done=y&panel_count=y
    #http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=407&panel_type=&search_optional_item=n&search_done=y&panel_count=y
    #http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_key=40701&panel_type=&search_optional_item=n&search_done=y&panel_count=y






url ="http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_cd=404&panel_type=&search_optional_item=n&search_done=y&panel_count=y"
response = requests.get(url)
html =  BeautifulSoup(response.text, 'html.parser')

'''
company = html.select('.part_top')
for com in company:
    print(f'{com.select_one(".company_name").text}-{com.select_one(".recruit_name").text}')
   # -{com.select_one(".list_recruit_condition").text}
    break
'''

#post 방식으로 불러오기 
company_list = html.select('ul.product_list li')
print("----------------------------------------------------------")
for com in company_list:
    idx = com.select_one('a')['href'].split('=')[-1]
    company_info_url = 'http://www.saramin.co.kr/zf_user/jobs/relay/view-ajax'
    copany_info_params = { 'rec_idx' : idx}

    company_response = requests.post(company_info_url,params=copany_info_params)
    print(company_response)
    company_html = BeautifulSoup(company_response.text,'html.parser')
    company_title = company_html.select_one('a.company').text
    print(company_title.strip())

    break
