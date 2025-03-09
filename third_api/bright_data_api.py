import requests

class BrightDataAPIClient:
    def __init__(self, api_token: str):
        """
        初始化 API 客户端
        :param api_token: API 认证 Bearer 令牌
        """
        self.api_token = api_token
        self.base_url = "https://api.brightdata.com/datasets/v3/trigger"
        self.progress_url = "https://api.brightdata.com/datasets/v3/progress"
        self.collect_url = "https://api.brightdata.com/datasets/v3/snapshot"
    def set_api_token(self, new_token: str):
        """更新 API 令牌"""
        self.api_token = new_token

    def check_dataset_status(self, snapshot_id):
        url = f"{self.progress_url}/{snapshot_id}"
        headers = {
            "Authorization": f"Bearer {self.api_token}"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 如果请求失败，抛出异常
            return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def collect_dataset(self, snapshot_id):
        url = f"{self.collect_url}/{snapshot_id}?format=json"
        headers = {
            "Authorization": f"Bearer {self.api_token}"
        }
        test = "https://api.brightdata.com/datasets/v3/snapshot/132?format=json"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # 如果请求失败，抛出异常
            return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def trigger_dataset(self, dataset_id: str, input_data: list, bucket: str = "", directory: str = ""):
        url = f"{self.base_url}?dataset_id={dataset_id}&include_errors=true"

        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=input_data, headers=headers)
            response.raise_for_status()  # 如果请求失败，抛出异常
            return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
            return None

    def create_facebook_group_req(self, *gLinks, num_of_posts=20, start_date="", end_date=""):
        input_data = []
        for link in gLinks:
            req_json = {"url": link, "num_of_posts":num_of_posts, "start_date":start_date, "end_date":end_date}
            input_data.append(req_json)
        return input_data


if __name__ == "__main__":
    # 初始化 API 客户端
    api_client = BrightDataAPIClient(api_token="148ed6d792d3c511e5e088f48a494137d5522fa2dd8dccf314a66d54e4c6e732")

    # 定义数据集 ID 和输入数据
    dataset_id = "gd_lz11l67o2cb3r0lkj3"
    test = ["https://www.facebook.com/groups/960497488053417/", "https://www.facebook.com/groups/1379024045506726"]
    input_data = api_client.create_facebook_group_req(*test, num_of_posts=10)


    response = api_client.collect_dataset("s_m7ztqjv3lqytk0r0o")
    print(response)

