import json
import requests

api_key = "RGAPI-c4c9112c-c604-4545-9164-c9a28a1f9d94"

print("1: 플레이어 검색")
selectnum = input("번호를 입력해주세요: ")

if selectnum == "1":
    name = input("소환사의 닉네임을 입력해주세요: ")
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        #코드가 200일때
        resobj = json.loads(res.text)
        URL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resobj["id"]
        res = requests.get(URL, headers={"X-Riot-Token": api_key})
        rankinfo = json.loads(res.text)
        print("소환사 이름: "+name)
        for i in rankinfo:
            if i["queueType"] == "RANKED_SOLO_5x5":
                #솔랭과 자랭중 솔랭
                print("솔로랭크:")
                print(f'티어: {i["tier"]} {i["rank"]}')
                print(f'승: {i["wins"]}판, 패: {i["losses"]}판')
            else:
                # 솔랭과 자랭중 자랭
                print("자유랭크:")
                print(f'티어: {i["tier"]} {i["rank"]}')
                print(f'승: {i["wins"]}판, 패: {i["losses"]}판')
    else:
        # 코드가 200이 아닐때(즉 찾는 닉네임이 없을때)
        print("소환사가 존재하지 않습니다")