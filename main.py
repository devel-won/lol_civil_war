import json
import requests

# 과거 티어에 대한 정보가 없음
# 현재 티어로만 분배해야함 - 랭겜 안하면 실력 확인 불가능 ㅜ,ㅜ

api_key = "RGAPI-72041298-77a5-43b8-a416-75aac041317d"

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