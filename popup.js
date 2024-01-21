document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the stored data from chrome.storage.local
    chrome.storage.local.get("key", function(result) {
      if (result.key) {
        // Split the data by the '!' delimiter to separate each instructor's info
        mainDiv = document.getElementById("maindiv")
        const instructors = result.key.split('!');
        list = []
        for(let i = 0; i < instructors.length - 1;i++)
        {
            list.push(instructors[i].split("\n"))
        }
        for(let ls of list)
        {
            const profTab = document.createElement("div")
            profTab.classList.add('section')
            //profTab.classList.add()
            for (let attr of ls)   //looking at specific attribute to each professor
            {
                profAttr = document.createElement("div")
                profAttr.innerHTML = attr
                profTab.appendChild(profAttr)
            }
            mainDiv.appendChild(profTab)
        }

        
        /*
        // Iterate over each instructor's info
        instructors.forEach((instructor, index) => {
          // Ensure there's a corresponding container for this instructor
          //const professorInfo = document.querySelector(`.professor-info[data-index="${index + 1}"]`);
  
          // If the container exists, populate it with data
          if (professorInfo) {
            // Split the instructor's info by the '/' delimiter
            const details = instructor.split('/');
  
            // Populate the professor's name
            const professorNameElement = professorInfo.querySelector('.professor-name');
            //professorNameElement.textContent += details[1].trim(); // Append the name to "Professor:"
  
            // Populate the rating
            const ratingElement = professorInfo.querySelector('.rating-stars');
            const ratingValue = details[2].trim(); // Assuming the rating is always the third element
            ratingElement.textContent = ratingValue; // Replace "stars" with the actual rating
  
            // For a visual representation of stars, you would create and append star images according to the rating
            // This is a placeholder for that logic
  
            // Populate the reviews
            const reviewElement = professorInfo.querySelector('.professor-reviews');
            reviewElement.textContent = details.slice(3).join(' / '); // Join the remaining details for reviews
          }
        
        });
        */
        // Optional: Clear the storage after retrieving the data
        chrome.storage.local.remove("key", function() {
          console.log("Data removed from storage");
        });
      }
    });
  });