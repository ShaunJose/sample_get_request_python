import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts/5"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)

if __name__ == "__main__":
    main()
