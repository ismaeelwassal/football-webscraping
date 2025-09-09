
import csv
import requests
from bs4 import BeautifulSoup
import lxml
import os
os.makedirs("documents/yallakora", exist_ok=True)

date=input("enter date of matches")
page =requests.get(f"https://www.yallakora.com/match-center?date={date}")


def main(page):
    source=page.content
    #print(source)
    soup=BeautifulSoup(source,"lxml")
    matches_details=[]
    #print(soup)
    # find all divs with class= matchCard 
    championships=soup.find_all("div",{'class':'matchCard'})
   # print(championships)


    def get_match_info(championships):
        championship_title=championships.find("h2").text.strip()
        #print(championship_title)
        all_matches = championships.find_all("div", {'class':'item'})


        num_of_matches=len(all_matches)
        print(num_of_matches)



        for i in range(num_of_matches):
            # names of teams
            team_A=all_matches[i].find("div",{'class':'teamA'}).text.strip()
            team_B=all_matches[i].find("div",{'class':'teamB'}).text.strip()
            
            # score 
            match_result=all_matches[i].find("div",{"class": "MResult"}).find_all("span",{"class":"score"})
            score = str(match_result[0].text.strip()) + " - " + str(match_result[1].text.strip())
            score = "'" + score  





            # time of match
            time=all_matches[i].find("div",{"class": "MResult"}).find("span",{"class":"time"}).text.strip()

            matches_details.append({"نوع البطوله":championship_title,"الفريق الاول":team_A,"الفريق الثاني":team_B,"ميعاد المباراه":time,"النتيجه":score})
    if len(championships)==0:
        print("no matches today")
    for i in range(len(championships)):

        get_match_info(championships[i])


    keys=matches_details[0].keys()
   
   
    with open("documents/yallakora/matches-details.csv", 'w', encoding='utf-8-sig', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)

print(os.path.abspath("documents/yallakora/matches-details.csv"))

main(page)