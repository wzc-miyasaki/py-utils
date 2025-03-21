import requests
from bs4 import BeautifulSoup
from loguru import logger
from common.enumeration.shom_enum import ShomConst

from common.csv_utils.common_writer import listMap_to_csv

class ShomConst:
    def __init__(self, **kwargs):
        self.job_type_map = {}
        self.job_division_map = {}
        self.job_district_map = {}
        self.job_work_exp_map = {}
        self.education_map = {}

    def get_job_type_by_id(self, id, map_type: ShomConst):
        if map_type == ShomConst.JOB_TYPE:
            return self.job_type_map.get(id)
        elif map_type == ShomConst.DIVISION:
            return self.job_division_map.get(id)
        elif map_type == ShomConst.DISTRICT:
            return self.job_district_map.get(id)
        elif map_type == ShomConst.WORK_EXPERIENCE:
            return self.job_work_exp_map.get(id)
        else:
            return ""

def post_data(url, headers, params={}):
    try:
        response = requests.post(url, headers=headers, json=params)
        response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
        return response.json()  # Return the parsed JSON response
    except requests.exceptions.RequestException as e:
        logger.error("error", e)
        return None

def fetch_data_list():
    """
    shomvob 所有filter的ID和英文描述映射
    """
    url = "https://iuazegsorvopdfkveycu.supabase.co/rest/v1/rpc/public_data_list_with_topic_name"
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJvbGUiOiJhbm9uIiwiaWF0IjoxNjQyNDkxMTc4LCJleHAiOjE5NTgwNjcxNzh9.Oz-apWdllp2W8JlB4oGG0mF5QJnrN4vDOzk6BkJlSH4"
    headers = {
        "accept": "application/json, text/plain, */*",
        "apikey": api_key
    }

    data = post_data(url, headers)
    if data:
        filter_list = data[0]

        job_type_list = filter_list.get("job_type")
        job_type_map = {}
        for info in job_type_list:
            job_type_map[info.get("id")] = info.get("job_type_en")

        district_list = filter_list.get("district")
        district_map = {}
        for info in district_list:
            district_map[info.get("district_id")] = info.get("district_en")


        division_list = filter_list.get("division")
        division_map = {}
        for info in division_list:
            division_map[info.get("division_id")] = info.get("division_en")

        education_list = filter_list.get("education")
        education_map = {}
        for info in education_list:
            education_map[info.get("id")] = info.get("education_en")

        work_experience_list = filter_list.get("work_experience")
        work_experience_map = {}
        for info in work_experience_list:
            work_experience_map[info.get("id")] = info.get("work_experience_en")

        filterData = ShomConst()
        filterData.job_type_map = job_type_map
        filterData.job_division_map = division_map
        filterData.job_district_map = district_map
        filterData.job_work_exp_map = work_experience_map
        filterData.education_map = education_map
        return filterData
    return None

def fetch_single_job_detail(job_id):
    url = "https://iuazegsorvopdfkveycu.supabase.co/rest/v1/rpc/get_single_job_description_guest_new_v2"
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJvbGUiOiJhbm9uIiwiaWF0IjoxNjQyNDkxMTc4LCJleHAiOjE5NTgwNjcxNzh9.Oz-apWdllp2W8JlB4oGG0mF5QJnrN4vDOzk6BkJlSH4"
    headers = {
        "accept": "application/json, text/plain, */*",
        "apikey": api_key,
        "content-type": "application/json"
    }
    param = {"job_id_data": job_id}
    data = post_data(url, headers, param)
    if data:
        print(data)
        return data
    else:
        return None

def fetch_job_list():
    url = "https://iuazegsorvopdfkveycu.supabase.co/rest/v1/rpc/custom_job_listing_guest"
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJvbGUiOiJhbm9uIiwiaWF0IjoxNjQyNDkxMTc4LCJleHAiOjE5NTgwNjcxNzh9.Oz-apWdllp2W8JlB4oGG0mF5QJnrN4vDOzk6BkJlSH4"
    headers = {
        "accept": "application/json, text/plain, */*",
        "apikey": api_key,
        "content-type": "application/json"
    }
    data = post_data(url, headers)
    return data

def parse_html(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        raw_text = soup.get_text(separator=",", strip=True)
        print(len(raw_text))
        return raw_text
    except Exception as e:
        logger.error(e)
        return None



if __name__ == "__main__":
    # Call the function and print the response
    data = fetch_data_list()
    holder = []
    for id, typeName in data.job_type_map.items():
        tmp = {}
        tmp["id"] = id
        tmp["job_type"] = typeName
        holder.append(tmp)

    # 获取岗位列表
    data = fetch_job_list()
    if data:
        print(len(data))
        for info in data:
            print(f"{info.get('id')} : {info.get('job_title')}")


