import pyautogui

def on_double_click(x, y, button, pressed):
    if button == "left" and pressed:
        # Capture the selected text
        selected_text = pyautogui.screenshot(region=(x, y, 200, 30))

        # OCR (Optical Character Recognition) to extract the text from the captured image
        # You'll need to have pytesseract installed for this step
        # pip install pytesseract
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Path to Tesseract OCR executable
        extracted_text = pytesseract.image_to_string(selected_text)

        # Extract the word from the extracted text
        word = extracted_text.strip()

        print(f"Selected word: {word}")

pyautogui.doubleClick = on_double_click
pyautogui.mouse_events_hook = pyautogui.doubleClick

pyautogui.alert("Click OK to start capturing double-click events.")

while True:
    try:
        pyautogui.sleep(1)
    except KeyboardInterrupt:
        break
