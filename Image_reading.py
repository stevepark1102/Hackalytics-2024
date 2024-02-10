import cv2
import pytesseract
import pandas as pd



def image_to_csv(image_path, csv_output_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)


    # Use pytesseract to do OCR on the image
    ocr_result = pytesseract.image_to_string(img)

    # Assuming the data is tabular and each row is separated by a newline and columns by a tab
    # This might need adjustment depending on the actual data format
    rows = ocr_result.split('\n')
    data = [row.split('\t') for row in rows if row.strip()]

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_output_path, index=False)

# Example usage
image_path = 'path/to/your/image.png'
csv_output_path = 'output.csv'
image_to_csv(image_path, csv_output_path)

print("CSV file has been created.")
