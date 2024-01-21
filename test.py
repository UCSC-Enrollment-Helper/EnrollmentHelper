import ratemyprofessor
import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'https://catalog.ucsc.edu/en/current/general-catalog/courses/bioe-biology-ecology-and-evolutionary/'

# Make a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Specify the CSS selector of the specific div you want to scrape
    div_selector = '.instructor'  # Replace with the actual class or id of your div

    # Find the div using BeautifulSoup
    target_div = soup.select_one(div_selector)

    # Check if the div is found
    if target_div:
        # Extract the information you need from the div
        extracted_info = target_div.text.strip()

        # Print or store the extracted information
        print("Extracted Information:", extracted_info)
    else:
        print("Div not found on the page.")
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")

profName = extracted_info.replace("Instructor", "").strip()

professor = ratemyprofessor.get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("UCSC"), profName)
#print(extracted_info)
#print(professor.name)

if professor is not None:
    print("%s works in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
    print("Rating: %s / 5.0" % professor.rating)
    print("Difficulty: %s / 5.0" % professor.difficulty)
    print("Total Ratings: %s" % professor.num_ratings)
    if professor.would_take_again is not None:
        print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
    else:
        print("Would Take Again: N/A")




