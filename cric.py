import pywhatkit
import requests
response = requests.get("https://www.cricapi.com/api/matches/?apikey=cHwZxSxnzBTfA8gVNkgIo60x5vB3")
match_List = ""
toss_winner = ""
winner_team = ""
status = ""
number = "+91"+"" //enter WA number
time = int(input("Enter the hour in 24 formate"))
mins = int(input("Enter the current Min")) + 1
for i in response.json()['matches']:
    if i["matchStarted"] == True:
        if i["squad"] == True:
            winner_team = i["winner_team"]
            ##toss_winner = i["toss_winner_team"]
        else:
            winner_team = "Match under process"
            toss_winner = "Toss under process"
        if toss_winner != "Toss under process" and winner_team == "Match under process":
            status = "Live"
            print(i["team-1"] + " VS " + i["team-2"])
            print(i["unique_id"])
        elif toss_winner != "Toss under process" and winner_team != "Match under process":
            status = "Match over"
            print(i["team-1"] + " VS " + i["team-2"])
            print(i["unique_id"])
        else:
            status = "Yet to start"
        match_List = match_List + i["team-1"] + " VS " + i["team-2"]+" - * "+status+" *"+"\n"+ "--- "+"Match Type - "+i["type"]+"\n"+"--- "+"toss winner - "+toss_winner+"\n"+"--- "+"won by - "+winner_team+"\n"+"\n"+"\n"
##print(match_List)
pywhatkit.sendwhatmsg(number, match_List, time, mins)
unique_id = input("enter theunique ID")
response2 = requests.get("https://www.cricapi.com/api/cricketScore?unique_id="+unique_id+"&apikey=cHwZxSxnzBTfA8gVNkgIo60x5vB3")
time = int(input("Enter the hour in 24 formate"))
mins = int(input("Enter the current Min")) + 1
result = "Score - " + response2.json()["score"] +"\n"+ "description - "+ response2.json()["description"]
pywhatkit.sendwhatmsg(number, result, time, mins)
