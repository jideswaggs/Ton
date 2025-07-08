import requests
from colorama import init, Fore
query=input('input query : ')
init()

while True:
    for i in range(1, 13):
        try:
   
            login_url = "https://api.businesshublab.xyz/api/user/login"
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
                'Accept': "application/json, text/plain, */*",
                'content-length': "0",
                'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
                'content-type': "application/x-www-form-urlencoded",
                'sec-ch-ua-mobile': "?1",
                'authorization': query,
                'sec-ch-ua-platform': "\"Android\"",
                'origin': "https://web.businesshublab.xyz",
                'sec-fetch-site': "same-site",
                'sec-fetch-mode': "cors",
                'sec-fetch-dest': "empty",
                'referer': "https://web.businesshublab.xyz/",
                'accept-language': "en-US,en;q=0.9,ar;q=0.8"
            }
            
            response = requests.post(login_url, headers=headers)
            response.raise_for_status()
            token = response.json()['data']['token']
            
   
            claim_url = "https://api.businesshublab.xyz/api/project/claim"
            payload = {'id': str(i)}
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
                'Accept': "application/json, text/plain, */*",
                'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
                'sec-ch-ua-mobile': "?1",
                'authorization': token,
                'sec-ch-ua-platform': "\"Android\"",
                'origin': "https://web.businesshublab.xyz",
                'sec-fetch-site': "same-site",
                'sec-fetch-mode': "cors",
                'sec-fetch-dest': "empty",
                'referer': "https://web.businesshublab.xyz/",
                'accept-language': "en-US,en;q=0.9,ar;q=0.8"
            }
            
            response = requests.post(claim_url, data=payload, headers=headers)
            response.raise_for_status()
            balance = response.json()['data']['user']['balance']
            
            print(f"{Fore.GREEN}LV{i} »» {balance}{Fore.RESET}")
            
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}LV{i} »» {e}{Fore.RESET}")
        except KeyError as e:
            print(f"{Fore.RED}LV{i} »» {e}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}LV{i} »»  {e}{Fore.RESET}")