import requests

def fetch_random_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product = data["data"]
        brand = product["brand"]
        description = product["description"]
        return brand,description
    else:
        raise Exception("Failed to fetch Product Data")
    
def main():
    try:
        brand,category = fetch_random_product()
        print(f"Brand : {brand}\nCategory : {category}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()
