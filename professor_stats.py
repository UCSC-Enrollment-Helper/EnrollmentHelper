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

        index = 1
        prof_stats = ""

        for instructor_div in instructor_divs:
            instructor_info = instructor_div.text.strip()
            prof_name = instructor_info.replace("Instructor", "").strip()

            # Find the div using BeautifulSoup
            professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("UCSC"), prof_name)

            if professor is not None:
                prof_stats += f"Instructor: {index}\n"
                prof_stats += f"{professor.name} works in the {professor.department} Department of {professor.school.name}.\n"
                prof_stats += f"Rating: {professor.rating} / 5.0\n"
                prof_stats += f"Difficulty: {professor.difficulty} / 5.0\n"
                prof_stats += f"Total Ratings: {professor.num_ratings}\n"
                if professor.would_take_again is not None:
                    prof_stats += f"Would Take Again: {round(professor.would_take_again, 1)}%\n"
                else:
                    prof_stats += "Would Take Again: N/A\n"
                prof_stats += "\n"
                index += 1
            if(index == 10):
                break

        return prof_stats
    else:
        print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
        return None

prof_stats_string = run(url)

# Print the string
print(prof_stats_string)