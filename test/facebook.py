from macholib.mach_o import source_version_command

from third_api.bright_data_api import BrightDataAPIClient
import time

API_WAITING_TIME_SECONDS = 1200

def test():
    dataset_id = "gd_lz11l67o2cb3r0lkj3"
    token = "148ed6d792d3c511e5e088f48a494137d5522fa2dd8dccf314a66d54e4c6e732"
    api = BrightDataAPIClient(api_token=token)
    urlList = api.create_facebook_group_req("https://www.facebook.com/groups/960497488053417/", num_of_posts=10)
    snapshot_id = api.trigger_dataset(dataset_id, urlList)


def test2():
    id = "s_m8130at01fhw8y0alt"
    dataset_id = "gd_lz11l67o2cb3r0lkj3"
    token = "148ed6d792d3c511e5e088f48a494137d5522fa2dd8dccf314a66d54e4c6e732"
    api = BrightDataAPIClient(api_token=token)
    progress = api.check_dataset_status(id)

    start = time.time()
    while True:
        if "status" in progress:
            if progress["status"] == "ready":
                break
        if time.time() - start > API_WAITING_TIME_SECONDS:
            break
        time.sleep(60)
        progress = api.check_dataset_status(id)

    dataset = api.collect_dataset(id)
    if dataset:
        print(dataset)



if __name__ == '__main__':
    test()