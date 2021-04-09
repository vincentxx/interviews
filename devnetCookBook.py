#@vincent
#@MIT License

#Get authorization token: https://developer.webex.com/docs/api/getting-started#accounts-and-authentication
bearerToken='OWUzYTcwMTctZjgyMy00ODg3LTllNjUtZDM2Yjg1N2RjNWU0MDk5MDg2NDAtNjc3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
def getToken():
    return "Bearer " + bearerToken

#https://developer.cisco.com/learning/modules/spark-extensibility-sd/collab-spark-extensibility-itp/step/3
import requests,json
def sendWebexMessage():
    msg = 'Hello World!!'
    roomID = 'Y2lzY29zcGFyazovL3VzL1JPT00vZmMxNTdmMTAtNWI4NC0xMWViLTliNDEtYjdlMmIxM2EzNDhh'
    body = {"roomId" : roomID, "text" : msg}
    headers = {
        "Authorization": getToken(),
        "Content-Type": "application/json"
        }
    response = requests.request("POST", url="https://webexapis.com/v1/messages", data=json.dumps(body), headers=headers)
    print(response.content)

def getRoomList():
    headers = {
        "Authorization": getToken(),
        "Content-Type": "application/json"
    }
    response = requests.request("GET", url="https://webexapis.com/v1/rooms", headers=headers)
    print(response.json())






##Test bed
#getRoomList()
#print(getToken())
sendWebexMessage()



