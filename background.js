// Listen for messages from the content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "result") {
    // Assuming message.data contains the HTML or text you want to display
    const res = message.data
    console.log("dsadsadsadsa",res)
    let resultContainer = document.getElementById('reviews');
    resultContainer.innerHTML = res
    // Display the result in the reviews section
    reviewsSection.innerHTML = message.data;
  }
  return true;
});
//chrome.runtime.sendMessage({type: "result", data: resu})
