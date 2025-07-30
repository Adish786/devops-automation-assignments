import configparser  # Module to handle configuration files (.ini format)
import json          # Module to work with JSON data
import os            # Module to interact with the operating system (used to check file existence)

def parse_config(file_path, output_file="config_data.json"):
    """
    Parse the given .ini configuration file and extract key-value pairs.

    Parameters:
        file_path (str): Path to the input configuration file.
        output_file (str): Path where the parsed data will be saved in JSON format.

    Returns:
        dict: Parsed configuration data as a dictionary.
    """

    # Check if the configuration file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file {file_path} not found.")

    # Create a ConfigParser instance
    config = configparser.ConfigParser()
    
    # Read the configuration file
    config.read(file_path)

    result = {}

    # Iterate through each section and convert its key-value pairs to a dictionary
    for section in config.sections():
        result[section] = dict(config.items(section))

    # Save the resulting dictionary to a JSON file
    with open(output_file, "w") as json_file:
        json.dump(result, json_file, indent=4)

    return result

if __name__ == "__main__":
    try:
        # Attempt to parse the configuration file
        data = parse_config("config.ini")

        # Display the parsed data in a readable format
        print("✅ Parsed Config Data:")
        print(json.dumps(data, indent=4))

    except Exception as e:
        # Catch and display any errors during parsing or file handling
        print(f"❌ Error: {e}")
