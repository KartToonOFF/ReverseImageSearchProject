import requests

img_url = "https://upload.wikimedia.org/wikipedia/commons/a/a8/Genco_Gulan_with_4_eyes.jpg"
url = f"https://serpapi.com/search.json?engine=google_reverse_image&image_url={img_url}&api_key=4523b682434e6c04c57c1b7e8a3b72d5e2049f7fd9b1ab08466da5ae20245fdf"

r = requests.get(url)
# print(r.json())

imgs = r.json()["image_results"]

for img in imgs:
    print(img["title"], img["link"])