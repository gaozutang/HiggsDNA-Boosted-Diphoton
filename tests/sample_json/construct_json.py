import os
import json

import numpy as np
import matplotlib.pyplot as plt
import uproot
import awkward as ak
import argparse

parser = argparse.ArgumentParser(
    description="Simple script to construct sample json from the path."
)
parser.add_argument("--source", type=str, help="Path to input file. Example:/GG-Box-3Jets_MGG-80_13p6TeV_sherpa/Run3Summer22EEMiniAODv4-130X_mcRun3_2022_realistic_postEE_v6-v2/MINIAODSIM. The string after 'file dataset='")

parser.add_argument("--name", type=str, help="name")

args = parser.parse_args()
nano_dir = args.source
name = args.name
# das_file_cmd = f'/cvmfs/cms.cern.ch/common/dasgoclient -query=\"file dataset={nano_dir} instance=prod/phys03"'
das_file_cmd = f'/cvmfs/cms.cern.ch/common/dasgoclient -query=\"file dataset={nano_dir}"'
print(das_file_cmd)
das_output_files = os.popen(das_file_cmd).readlines()
print(das_output_files)
root_dir = []
for i,das_file in enumerate(das_output_files):
    root_dir.append("root://xrootd-cms.infn.it/"+das_file.split()[0])

print(root_dir)

def create_json(output_name, root_files, json_filename="output.json"):
    """
    Creates a JSON file with the given structure containing root files from the specified path.

    Args:
        output_name (str): Custom name for the JSON key.
        input_path (str): Path to the directory containing root files.
        json_filename (str): Name of the output JSON file (default: "output.json").
    """
    try:
        # Verify the input path exists
        # if not os.path.exists(input_path):
        #    raise FileNotFoundError(f"The specified path does not exist: {input_path}")

        # Get the list of .root files in the directory
        # root_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(".root")]
        # Check if there are root files
        if not root_files:
            raise FileNotFoundError("No .root files found in the specified directory.")

        # Create the JSON structure
        data = {
            output_name: root_files
        }

        # Write to a JSON file
        with open(json_filename, "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"JSON file '{json_filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # custom_name = "GluGluHtoGG_M-125_postEE"  # Replace with your desired name
    # output_file_name = "ggh_125_post.json"  # Replace with desired output JSON file name
    # custom_name = "pp-gg_80_postEE"
    # output_file_name = "pp-gg_80_post.json"
    custom_name = name
    output_file_name = name + ".json"
    create_json(custom_name, root_dir, output_file_name)

