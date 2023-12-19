import requests, random, string, threading, json

def rstr(l):
    return ''.join(random.choice(string.ascii_letters) for _ in range(l))

def generate():
    with open('config.json') as f:
        config = json.load(f)
    headers = { #that is literally all headers u need lmao except for the user agent
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0 (Edition std-1)"
    }

    payload = {
        "partnerUserId": f"{rstr(8)}-{rstr(4)}-{rstr(4)}-{rstr(4)}-{rstr(12)}",
    }

    try:
        if config.get("use_proxies"):
            with open("proxies.txt", "r") as f:
                proxies = f.readlines()
            proxies = {
                "http": f"http://{random.choice(proxies)}",
                "https": f"http://{random.choice(proxies)}"
            }
            resp = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", headers=headers, json=payload, proxies=proxies)
        else:
            resp = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", headers=headers, json=payload)
        if resp.text:
            thingy = resp.json()
            link = (f"https://discord.com/billing/partner-promotions/1180231712274387115/{thingy['token']}")
            print(link)
            with open("promos.txt", "a") as f:
                f.write(f"{link}\n")
        else:
            print("opera being fucky again and doesnt return promos (happens quite often and it normal)")
    except Exception as e:
        print(e)

def start():
    while True:
        generate()

if __name__ == "__main__":
    for i in range(100):
        threading.Thread(target=start).start()
