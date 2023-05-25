# Live_dictionary_chrome_extension
Steps in creation of chrome extension:-

Chrome extensions are typically developed using JavaScript and HTML, but it is possible to use Python to develop a Chrome extension with the help of external tools and libraries. Here are the general steps to create a Chrome extension using Python:

1. Choose a Python web framework to build the back-end of your extension. Flask and Django are two popular options that can be used to create web services that interact with your extension.

2. Create a manifest.json file that describes your extension and its properties, such as the name, version number, and permissions. This file is required for all Chrome extensions and should be included in the root directory of your extension.

3. Write the front-end code for your extension using HTML, CSS, and JavaScript. You can use Python to generate the HTML dynamically or serve the static files through your Python web framework.

4. Write the Python code that interacts with your web framework and performs the desired functionality for your extension. This code should be executed on the server side and can interact with the Chrome APIs through AJAX requests or other methods.

5. Test your extension by loading it into Chrome as an unpacked extension. To do this, open the Extensions page in Chrome and click the "Load unpacked" button. Select the directory containing your extension files and click "OK".

6. Publish your extension to the Chrome Web Store if you want to make it available to other users.

7. Keep in mind that creating a Chrome extension using Python can be more complex and time-consuming than using JavaScript, as it requires additional tools and libraries to bridge the gap between Python and the Chrome APIs.

Publishing steps to web store:-

Publishing a Chrome extension to the Chrome Web Store involves a few steps. Here is a general overview of the process:

1. Create a developer account: To publish an extension on the Chrome Web Store, you will need to have a Google account and create a developer account. If you don't have a Google account, you will need to create one first. Then, go to the Chrome Web Store developer dashboard and sign up as a developer.

2. Package your extension: Before you can publish your extension, you need to package it. This involves creating a ZIP file of your extension's files, including the manifest file, HTML, CSS, JavaScript, and any other assets. You can do this from the Extensions page in Chrome by clicking the "Pack extension" button and following the prompts.

3. Upload your extension: Once you have packaged your extension, go to the Chrome Web Store developer dashboard and click the "Add new item" button. You will need to provide some basic information about your extension, including the name, description, category, and pricing (if any). You will also need to upload your extension's package file.

4. Set up your payment account (if applicable): If your extension is a paid app or extension, you will need to set up your payment account. This involves providing your banking and tax information and agreeing to the Chrome Web Store payment terms.

5. Publish your extension: After you have completed the above steps, you can submit your extension for review. The review process can take several days to complete, during which time your extension will not be visible on the Chrome Web Store. Once your extension has been approved, it will be available for users to install and use.

Note that there may be additional steps or requirements depending on the type of extension you are publishing and the region you are located in. Make sure to review the Chrome Web Store developer documentation and guidelines for detailed instructions.

References:
1. [Octopare scrape data from google search](https://youtu.be/_R8pNl41iUg)
2. [Complete Guide On PyDictionary: A “Real” Dictionary Module in Python](https://analyticsindiamag.com/complete-guide-on-pydictionary-a-real-dictionary-module-in-python/#:~:text=listed%20in%20it.-,PyDictionary%20is%20an%20open%2Dsource%20python%20library%20that%20is%20used,linguistic%20properties%20of%20different%20words.)
3. [How To Get Mouse Clicks With Python](https://analyticsindiamag.com/complete-guide-on-pydictionary-a-real-dictionary-module-in-python/#:~:text=listed%20in%20it.-,PyDictionary%20is%20an%20open%2Dsource%20python%20library%20that%20is%20used,linguistic%20properties%20of%20different%20words.)


Future upgrades:
- Live translation of the word or sentences to different languages
- Corresponding speech for the sentence or words.
- Dragging feature similar to dropbox for selecting the text in a specific area.
- 
