import json
import clipboard
from woocommerce import API

# wcapi = API(
#     url="https://iqorfe.com",
#     consumer_key="ck_ca8e9ff29f574fb98253fe5f31b6ac107e22a1b1",
#     consumer_secret="cs_0e98713b9c97f4b8d92b8df758bd02a5c62b3953",
#     version="wc/v3"
# )

wcapi = API(
    url="https://majdsazeh.com",
    consumer_key="ck_0076ccda79c74b85558657d322e5dcdd8055a3ac",
    consumer_secret="cs_98b1f95d4590cce374990aebc0e7e7860c9b05ed",
    version="wc/v3"
)

class products:
    def __init__(self, pages=1):
        self.pages = pages

    def show_all(self, keyword=None):
        if keyword is None:
            keyword = {}
        all = []
        for i in range(1, self.pages + 1):
            while True:
                try:
                    params = {"per_page": 100, "page": i}
                    params.update(keyword)
                    rt_page = wcapi.get("products", params=params)
                    print(i)


                    break
                except Exception as e:
                    print(e)
            all = all + json.loads(rt_page.text)
        json_formatted_str = json.dumps(all[0], indent=2)
        clipboard.copy(json_formatted_str)

        return all

    def update_product(self, product_id: int, data):
        while True:
            try:
                rt_page = wcapi.put(f"products/{product_id}", data=data)
                print(rt_page.text)
                break
            except Exception as e:
                print(e)
        return rt_page

    def update_products(self, data):
        while True:
            try:
                create_data = {
                    'update': data
                }
                rt_page = wcapi.post("products/batch/", data=create_data)
                break
            except Exception as e:
                print(e)
        return json.loads(rt_page.text)


class categories:
    pass


if __name__ == '__main__':
    all = products().show_all()
    # clipboard.copy(json.dumps(all[0], indent=2))
    txt = 'خرید سرسره بادی و قصر بادی تجهیزات شهربازی بادی سازان مجد خرید تجهیزات مهد کودک و لوازم جانبی شهربازی - '
    for i in all:
        update = [{
            'id': i['id'],
            'meta_data': [
                {
                    "key": "_yoast_wpseo_metadesc",
                    "value": txt + i['name'].replace(i['sku'], '')
                }
            ]
        }]
        pr = products().update_products(data=update)['update'][0]['name']
        print(pr)
    # prd = products().show_all()
    # for p in prd:
    #     pr = p['meta_data']
    #     print(next(item for item in pr if item["key"] == "_yoast_wpseo_focuskw"))
