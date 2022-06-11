import os
import pandas as pd

def read_bed6plus_file(file: str):
    if os.path.exists(input_data_file):
        if os.path.isfile(input_data_file):
            file_obj = open(input_data_file)
            lines = file_obj.readlines()
            output_dict = {}
            data_df = pd.DataFrame()
            start_df_index = 0
            for line in lines:
                if line[0:2] == "##":
                    value_list = [val.strip() for val in line[2:len(line)].split(":")]
                    output_dict[value_list[0]] = " ".join(value_list[1:len(value_list)])
                    start_df_index = start_df_index + 1
                elif line[0] == "#":
                    df_columns_list = [val.strip() for val in " ".join(line[1:len(line)].split()).split(" ")]
                    start_df_index = start_df_index + 1
                    break
            df = pd.DataFrame([sub.split("\t") for sub in lines[start_df_index:len(lines)]])
            df.columns = df_columns_list
            output_dict["Data"] = df
            return output_dict
        else:
            return("Path is not of a file.")
    else:
        return("Path does not exist.")