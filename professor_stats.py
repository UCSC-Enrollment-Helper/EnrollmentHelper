import ratemyprofessor
import requests
from bs4 import BeautifulSoup


url = 'https://catalog.ucsc.edu/en/current/general-catalog/courses/biol-biology-molecular-cell-and-developmental/1-99/biol-20a/'


def findStats(name, ind):
    statStr = ""
    professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("UCSC"), name)

    if professor is not None:
        statStr += f"Instructor: {ind}\n"
        statStr += f"{professor.name} works in the {professor.department} Department of {professor.school.name}.\n"
        statStr += f"Rating: {professor.rating} / 5.0\n"
        statStr += f"Difficulty: {professor.difficulty} / 5.0\n"
        statStr += f"Total Ratings: {professor.num_ratings}\n"
        if professor.would_take_again is not None:
            statStr += f"Would Take Again: {round(professor.would_take_again, 1)}%\n"
        else:
            statStr += "Would Take Again: N/A\n"
    return statStr



def run(url):
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Specify the CSS selector of the specific div you want to scrape
        instructor_divs = soup.find_all("div", {"class": "instructor"})

        index = 1
        prof_stats = ""

        for instructor_div in instructor_divs:
            instructor_infos = instructor_div.text.strip()
            prof_names = instructor_infos.replace("Instructor", "").strip()
            nameList = prof_names.split(',')
            print(nameList)
            if(len(nameList) == 1):
                prof_stats = prof_stats + findStats(nameList[0], index) + "\n"
                index += 1
            else:
                for name in nameList:
                    prof_stats = prof_stats + findStats(name, index) + "\n"
                    index += 1   
            if(index == 10):
                break

        return prof_stats
    else:
        print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
        return None
