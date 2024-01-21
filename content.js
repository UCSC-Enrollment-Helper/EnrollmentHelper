

console.log("Content script running");
// Check if the current URL contains "catalog.ucsc.edu"
if (window.location.href.indexOf("catalog.ucsc.edu") !== -1) {
  console.log("You are on the right page. Sending message to background script...");
  const params = new URLSearchParams(
    {param_name: window.location.href}
    )

  fetch('http://127.0.0.1:5000/run_python_script?' + params)
  .then(response => {
    console.log(response)
    return response.json()
  })
  .then(result => {
    console.log(result);
    // You can handle the result as needed
    console.log(result.result)
    //chrome.runtime.sendMessage({type: "result", data: result.result})
    chrome.storage.local.set({ "key": result.result }, function() {
      console.log("Data saved to storage");
  });
  })
    // Wait and ensure popup has loaded 
    /*
    console.log("finished waiting")
    const resultContainer = doc.getElementById('reviews');
    console.log(resultContainer)
    resultContainer.innerHTML = `
      <h2>Ratings:</h2>
      <p>${result.result}</p>
    `;
    */
  
  //.catch(error => console.error('Error executing Python script:', error));

} else {
  console.log("You are not on the right page");
}
