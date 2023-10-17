import os
import pandas as pd

# set main directory path
main_directory = "D:\\test_workspace\\CC_work\\all_directory"
# set target file path
target_file = "D:\\test_workspace\\CC_work\\output_directory\\output.xlsx"

# declare combined_data as DataFrame to store excel data
combined_data = pd.DataFrame()
count = 0
# traversal all dirs
for root, dirs, files in os.walk(main_directory):
    for file in files:
        if file.endswith(".xlsx"):
            file_path = os.path.join(root, file)
            print( "merging : ", file )
            # read excel
            data = pd.read_excel(file_path)
            # merge into combined_data
            combined_data = pd.concat([combined_data, data], ignore_index=True)
            count += 1

# write combined data to output excel
combined_data.to_excel( target_file, index=False)

print( "Successfully merge ", count, " files to output.xlsx" )