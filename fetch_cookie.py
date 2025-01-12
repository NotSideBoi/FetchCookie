class info:
    def get_user_id(cookie):
        url="https://users.roblox.com/v1/users/authenticated"
        req=requests.get(url,headers=info.get_headers(cookie),cookies=info.get_cookies(cookie))
        return req.json()['id']
    def get_info_request_url(type:str,id:int):
        if type=="gamepass":
            return f"https://apis.roblox.com/game-passes/v1/game-passes/{id}/product-info"
        elif type=="asset":
            return f"https://economy.roblox.com/v2/assets/{id}/details"
    def get_info(id:int,type:str):
        url=info.get_info_request_url(type,id)
        req=requests.get(url)
        list=[]
        list.append(req.json()['ProductId'])
        list.append(req.json()['Creator']['Id'])
        list.append(req.json()['PriceInRobux'])
        return list
    def getXsrf(cookie):
        xsrfRequest = requests.post(authurl, headers={'User-Agent': useragent}, cookies=info.get_cookies(cookie))
        if xsrfRequest.headers['x-csrf-token']:
            return xsrfRequest.headers['x-csrf-token']
        else:
            return ''
    def get_headers(cookie):
        return {"X-CSRF-TOKEN":info.getXsrf(cookie)}
    def get_cookies(cookie):
        return {".ROBLOSECURITY":cookie}
    def getUserId(username):
        API_ENDPOINT = "https://users.roblox.com/v1/usernames/users"
        payload={'usernames':[username],}
        req=requests.post(API_ENDPOINT,json=payload)
        return req.json()['data'][0]['id']
    def get_gamepasses(username):
        url=f"https://games.roblox.com/v2/users/{info.getUserId(username)}/games?accessFilter=Public&limit=50"
        req=requests.get(url)
        ids=[]
        for game in req.json()['data']:
            ids.append(game['id'])
        gamepasses=[]
        for universe in ids:
            url=f'https://games.roblox.com/v1/games/{universe}/game-passes?limit=100&sortOrder=Asc'
            otherequest=requests.get(url)
            for gamepass in otherequest.json()['data']:
                a=[]
                if not gamepass['price']==None:
                    a.append(gamepass['id'])
                    a.append(gamepass['price'])
                    gamepasses.append(a)
        return gamepasses
    def getUniverseId(cookie):
        ID = info.get_user_id(cookie)
        Id=requests.get(f"https://games.roblox.com/v2/users/{ID}/games?accessFilter=2&limit=10&sortOrder=Asc")
        game_id = Id.json()['data'][0]['id']
        return game_id
