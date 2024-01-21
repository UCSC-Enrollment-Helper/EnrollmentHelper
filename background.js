chrome.tabs.onUpdated.addListener((tabId, tab) => {
    if (tab.url && tab.url.includes("catalog.ucsc.edu")) {
        //const queryParameters = tab.url.split("?")[1];
        //const urlParameters = new URLSearchParams(queryParameters);
        console.log("You are on the right website")
        } else {
            console.log("You are not on the right website")
        }
    });