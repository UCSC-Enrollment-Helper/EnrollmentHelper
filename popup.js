document.addEventListener('DOMContentLoaded', function() {
    chrome.storage.local.get("key", function(result) {
        if (result.key) {
            console.log("Data retrieved from storage:", result.key);
            // Do something with result.key
            const resultContainer = document.getElementById('reviews');
            resultContainer.innerHTML = result.key
        }
    });

    // Optional: Clear the storage after retrieving the data
    chrome.storage.local.remove("key", function() {
        console.log("Data removed from storage");
    });
});

