console.log("Content script running");

if(window.location.href.indexOf("catalog.ucsc.edu") != -1){
  console.log("You are on the right page")
  //chrome.runtime.sendMessage({ message: "check_url" });
}else{
  console.log("You are not on the right page")
}