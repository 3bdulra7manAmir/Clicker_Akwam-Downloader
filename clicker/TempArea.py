import os
import zipfile


def search_iwi_in_iwd(directory, iwi_name_part):
    found = False
    # Iterate through all files in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.iwd'):
                iwd_path = os.path.join(root, file)
                print(f"Scanning {iwd_path}...")

                # Open the .iwd file as a ZIP file
                with zipfile.ZipFile(iwd_path, 'r') as iwd_file:
                    iwi_files = [name for name in iwd_file.namelist() if name.endswith('.iwi')]
                    if iwi_files:
                        print(f"Found the following .iwi files in {iwd_path}:")
                        for name in iwi_files:
                            print(f" - {name}")
                            if iwi_name_part in name:
                                found = True
                                print(f"Match found: {iwi_name_part} in {iwd_path}")
                                # Extract the found .iwi file if needed
                                extraction_path = os.path.join(root, 'extracted')
                                iwd_file.extract(name, extraction_path)
                                print(f"Extracted {name} to {extraction_path}")

    if not found:
        print(f"{iwi_name_part} not found in any .iwd files in {directory}")


# Specify the directory to search and the part/full name of the .iwi image
directory_to_search = 'E:\\Games\\Original_Games\\Steam\\steamapps\\common\\Call of Duty Modern Warfare 3\\main'
iwi_image_name_part = '~shad_co_head_c_spc-rgb&shad_~2aad3015'

search_iwi_in_iwd(directory_to_search, iwi_image_name_part)
