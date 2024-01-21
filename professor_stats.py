import ratemyprofessor
import requests
from bs4 import BeautifulSoup


url = 'https://catalog.ucsc.edu/en/current/general-catalog/courses/bioe-biology-ecology-and-evolutionary/'

response = requests.get(url)

#Check if the request was successful (status code 200)
if response.status_code == 200:
    #Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    #Specify the CSS selector of the specific div you want to scrape
    instructor_divs = soup.find_all("div", {"class": "instructor"})

    #print(instructor_divs)
    index = 1
    for instructor_div in instructor_divs:

        instructor_info = instructor_div.text.strip()
        profName = instructor_info.replace("Instructor", "").strip()
        #print(profName)

    #Find the div using BeautifulSoup
        professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("UCSC"), profName)

        
        if professor is not None:
            print("Instructor: ", index)
            print("%s works in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
            print("Rating: %s / 5.0" % professor.rating)
            print("Difficulty: %s / 5.0" % professor.difficulty)
            print("Total Ratings: %s" % professor.num_ratings)
            if professor.would_take_again is not None:
                print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
            else:
                print("Would Take Again: N/A")
            index+=1
            print("")