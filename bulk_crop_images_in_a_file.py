import cv2
import os

def crop_and_save_images(input_folder, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)

        if os.path.isfile(filepath) and filename.lower().endswith(('.tif')):
            try:
                
                img = cv2.imread(filepath)

                img_cropped = img[760:1360,710:1310]

                output_filepath = os.path.join(output_folder, filename)
                cv2.imwrite(output_filepath, img_cropped)

            except Exception as e:
                print(f"Error processing {filename}: {e}")

input_folder = r"C:\Users\srina\Desktop\CS-testing"
output_folder = r"C:\Users\srina\Desktop\CS-TESTING-CROPPED-IMGS"

crop_and_save_images(input_folder, output_folder)

