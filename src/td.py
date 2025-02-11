# %%
import requests
import json
import pandas as pd

def getTDCareer(df_length_limit = 100):
    # Target URL for the request
    url = "https://td.wd3.myworkdayjobs.com/wday/cxs/td/TD_Bank_Careers/jobs"

    # Request headers
    headers = {
        "accept": "application/json",
        "accept-language": "en-US",
        "content-type": "application/json",
        "origin": "https://td.wd3.myworkdayjobs.com",
        "priority": "u=1, i",
        "referer": "https://td.wd3.myworkdayjobs.com/en-US/TD_Bank_Careers?redirect=/en-US/TD_Bank_Careers/userHome",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-calypso-csrf-token": "c8e70fbb-96e9-4b1b-b215-69138ac98da9"
    }

    # Cookie information, note that the original cookie string is split into dictionary format
    cookies = {
        "__cflb": "02DiuJFb1a2FCfph91kR4Zp9F5cQ8FdpESYHmyiYqof9E",
        "PLAY_SESSION": "8bcb8c9bde5bb5bedf7c528003000485031f0b10-td_pSessionId=i7nr25vbbk8ssr6kvu0uk6c437&instance=vps-prod-wohip0zt.prod-vps.pr502.cust.dub.wd",
        "wday_vps_cookie": "2052692234.53810.0000",
        "_cfuvid": "elNFbPCv90Pz.AIcdsKNH4yXDirLsY560OhwozffaEE-1739311909744-0.0.1.1-604800000",
        "PLAY_LANG": "en-US",
        "timezoneOffset": "480",
        "__cf_bm": "PpyHRdF4hFaOEHRSB0qOAUodQo9nuGiXG8o7XpkNunA-1739313802-1.0.1.1-8.oxxqm5Wh1IdGk91kWswRse4hyzAvuEq5.eIXqnXWbI.lXvrIIt38Zm42gc0rwaZUUHVIFN.AsUKZ5Nx9dcoQ",
        "enablePrivacyTracking": "true",
        "wd-browser-id": "9fb36c9b-54c8-4e81-ab6e-64cc750c05e2",
        "CALYPSO_CSRF_TOKEN": "c8e70fbb-96e9-4b1b-b215-69138ac98da9"
    }

    # Data submitted by POST request (in JSON format)
    payload = {
        "appliedFacets": {},
        "limit": 20,
        "offset": 0,
        "searchText": ""
    }

    # Initialize offset
    offset = 0
    all_data = []

    while offset < df_length_limit:
        # Update offset in payload
        payload['offset'] = offset

        # Send POST request
        response = requests.post(url, headers=headers, cookies=cookies, json=payload)
        
        # Parse response content
        data = response.json()
        
        # Extract required fields
        job_postings = data.get('jobPostings', [])
        if not job_postings:
            break
        
        for job in job_postings:
            all_data.append({
                'title': job.get('title'),
                'externalPath': job.get('externalPath'),
                'locationsText': job.get('locationsText'),
                'postedOn': job.get('postedOn'),
                'remoteType': job.get('remoteType'),
                'bulletFields': job.get('bulletFields')
            })
        
        # Increase offset
        offset += 20

    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    return df

# %%
if __name__=="__main__":
    df = getTDCareer(df_length_limit = 100)
# %%

