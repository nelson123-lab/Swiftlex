document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.executeScript({
      code: "window.getSelection().toString();"
    }, function(selection) {
      var word = selection[0].trim();
      fetchMeaning(word);
    });
  });
  
  function fetchMeaning(word) {
    // You'll need to implement the code here to fetch the meaning of the word
    // using a dictionary API or any other source of word meanings.
    // Update the 'word-meaning' element in popup.html with the fetched meaning.
  }
  