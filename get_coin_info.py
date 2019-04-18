import json

raw_coin_info = '{"code":200,"message":"success","data":[{"id":1,"name":"AE","address":"0x5CA9a71B1d01849C0a95490Cc00559717fCF0D1d"},{"id":2,"name":"BNB","address":"0xB8c77482e45F1F44dE1745F52C74426C631bDD52"},{"id":3,"name":"BTM","address":"0xcB97e65F07DA24D46BcDD078EBebd7C6E6E3d750"},{"id":4,"name":"EOS","address":null},{"id":6,"name":"ICX","address":"0xb5A5F22694352C15B00323844aD545ABb2B11028"},{"id":7,"name":"OMG","address":"0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"},{"id":8,"name":"TRX","address":null},{"id":9,"name":"GKC","address":"0x35b0ec11c0b45486f5bcbf10b50d111ea9ec5f90"}]}'

coin_info = json.loads(raw_coin_info)['data']

result = []
for per_coin in coin_info:
    per_coin_info = {}
    per_coin_info['name'] = per_coin['name']
    per_coin_info['address'] = per_coin['address']
    result.append(per_coin_info)

print(result)