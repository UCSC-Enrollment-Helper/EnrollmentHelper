chrome.runtime.onInstalled.addListener(function () {
    console.log("Extension installed");
  });
  
  chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.message === "check_url") {
      console.log("Received message from content script. Initiating Python script execution...");
  
      // Send a request to the server to run the Python script
      
    }
  });
  