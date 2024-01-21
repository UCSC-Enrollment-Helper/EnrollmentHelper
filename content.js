console.log("Content script running");

// Check if the current URL contains "catalog.ucsc.edu"
if (window.location.href.indexOf("catalog.ucsc.edu") !== -1) {
  console.log("You are on the right page. Sending message to background script...");
  // Send a message to the background script to initiate further actions
  chrome.runtime.sendMessage({ message: "check_url" });
} else {
  console.log("You are not on the right page");
}