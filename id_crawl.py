import requests
import json

# 상품 id 정보가 담긴 json 파일을 생성하는 코드이다.


# 랭킹 - 많이 선물한


best_group = ['delivery', 'coupon']
delivery_group_id = [4, 2, 1, 5, 8, 11, 9, 7, 10, 6, 3, 20]
coupon_group_id = [14, 13, 16, 15, 17, 12, 19, 18]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

product_list = []

for group_id in delivery_group_id:
    URL_new = f"https://gift.kakao.com/a/v2/best/delivery/{group_id}?page=0&size=100"
    r = requests.get(URL_new, headers=headers)
    results = r.json()
    group = URL_new.split('/')[6] + '/' + URL_new.split('/')[7].split('?')[0]
    ranking = 1
    print(URL_new.split('/')[6] + '/' + URL_new.split('/')[7].split('?')[0])
    print(group_id)
    print(results[1]['product']['id'])

    for product in results[1:]:
        product_list.append({'group':group, 'ranking':ranking, 'id':product['product']['id']})
        ranking+=1

for group_id in coupon_group_id:
    URL_new = f"https://gift.kakao.com/a/v2/best/coupon/{group_id}?page=0&size=100"
    r = requests.get(URL_new, headers=headers)
    results = r.json()
    group = URL_new.split('/')[6] + '/' + URL_new.split('/')[7].split('?')[0]
    ranking = 1
    print(URL_new.split('/')[6] + '/' + URL_new.split('/')[7].split('?')[0])
    print(group_id)
    print(results[1]['product']['id'])

    for product in results[1:]:
        product_list.append({'group':group, 'ranking':ranking, 'id':product['product']['id']})
        ranking+=1


file_path = "./product_id1.json"

with open(file_path, 'w') as outfile:
    json.dump(product_list, outfile, indent="\t", ensure_ascii=False)




# 랭킹 - 받고 만족한

display_group = ['생일', '남친', '여친', '응원', '감사', '엄마', '아빠', '위로', \
    '재미', '이사/집들이', '임신/출산', '결혼', '백일/돌', '취업/이직', '친구', '직장동료', '형제/자매', '선/후배']
price_group = ['R_0_1', 'R_1_3', 'R_3_5', 'R_5']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

product_list = []

display_group = ['생일', '남친', '여친', '응원', '감사', '엄마', '아빠', '위로', \
    '재미', '이사/집들이', '임신/출산', '결혼', '백일/돌', '취업/이직', '친구', '직장동료', '형제/자매', '선/후배']
price_group = ['R_0_1', 'R_1_3', 'R_3_5', 'R_5']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

product_list = []

for display_name in display_group:
    for price_name in price_group:
        URL_new = f"https://gift.kakao.com/a/v2/review-rankings?displayTag={display_name}&priceRange={price_name}"
        r = requests.get(URL_new, headers=headers)
        results = r.json()
        group = display_name + '/' + price_name
        print(group)
        print(results['rankings'][0]['product']['id'])

        for rank in results['rankings']:
            ranking = rank['rank']
            product_list.append({'group':group, 'ranking':ranking, 'id':rank['product']['id']})


file_path = "./product_id2.json"

with open(file_path, 'w') as outfile:
    json.dump(product_list, outfile, indent="\t", ensure_ascii=False)