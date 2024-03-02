import os
from colorama import Fore, Back, Style
from time import sleep
from num2words import num2words
from pathlib import Path

file_name = "ireland_bray_showroom_stock.txt"
LOG_FILE_NAME = os.getenv("TASKS_LOG_PATH", file_name)

if os.path.isabs(LOG_FILE_NAME):
    full_path = LOG_FILE_NAME
else:
    desktop_path = Path.home() / "Desktop"
    full_path = desktop_path / LOG_FILE_NAME


# ============================================================================
space_menu_count = 2
menu_str = (
    f"{Fore.CYAN}1:{' ' * space_menu_count}Add_car\n"
    f"{Fore.CYAN}2:{' ' * space_menu_count}Modify_car\n"
    f"{Fore.YELLOW}3:{' ' * space_menu_count}Delete_car\n"
    f"{Fore.YELLOW}4:{' ' * space_menu_count}Show_Cars\n"
    f"{Fore.RED}5:{' ' * space_menu_count}Total_cars\n"
    f"{Fore.RED}6:{' ' * space_menu_count}Exit\n"
)

showroom_data = []
header_line = f"{'='*23}  Showroom data  {'='*23}"
separator_line = "=" * 63
car_count = str(len(showroom_data))


header = {
    "ID": "",
    "Brand": "alfabetic",
    "Model": "alfanumeric",
    "Fuel_Type": "alfabetic",
    "Engine_Size": "float",
    "Transmission": "alfabetic",
    "Year": "numeric",
    "Mileage": "numeric",
    "Color": "alfabetic",
    "Price": "numeric",
}
# ============================================================================


def msg_count_car():
    """
    Prints a message indicating the total number of cars in the showroom.
    This total is converted to words for a friendly user interface.
    """

    message = (
        f"Hey there! We've got {num2words(car_count).upper()} "
        "awesome cars waiting for you in the showroom!\n"
    )
    print(Fore.RED + message)
    sleep(5)


# ============================================================================


def clear_screen():
    """
    Clears the console screen based on the operating system.
    """
    # Check if the operating system is Windows
    if os.name == "nt":
        os.system("cls")
    else:
        # Assume the operating system is Unix/Linux/Mac
        os.system("clear")


# ============================================================================


def exist(path):
    """
    Checks if a given path exists in the file system.

    Returns:
    - bool: True if the path exists, False otherwise.
    """
    return os.path.exists(path)


# ============================================================================


def validate_input(msg, data_type):
    while True:
        user_input = input(msg)
        if data_type == "alfabetic" and user_input.isalpha():
            return user_input
        elif data_type == "numeric" and user_input.isdigit():
            return user_input
        elif data_type == "alfanumeric" and user_input.isalnum():
            return user_input
        elif data_type == "float":
            try:
                float(user_input)
                return user_input
            except ValueError:
                pass
        print(Fore.RED + f"\rInput should be {data_type}. Try again.", end="")
        input(Fore.RED + " Press Enter to continue...")
        print("\r" + " " * 100, end="\r")


# ============================================================================


def user_input(data_dict):
    """
    Collects user input for each key in a dictionary, excluding the 'ID' field.

    Parameters:
    -data_dict (dict): Dictionary template with keys representing data fields.

    Returns:
    -dict: A new dictionary populated with user input for each key.
    """
    new_data = {}
    count = 0
    for key, value in data_dict.items():
        if key == "ID":
            new_data[key] = ""
        else:
            count += 1
            msg = f"{Fore.CYAN}{count}: Enter {key:<13}:\t".replace(" ", "-")

            new_data[key] = validate_input(msg, value)
    print()
    return new_data


# ============================================================================


def add_car(new_data):
    """
    Adds a new car's details to the showroom data and writes it to a file.

    Parameters:
    - new_data (dict): A dictionary containing the car's details to add.
    - after (optional): Parameter not used in the function but could be
      for specifying position.
    """

    global car_count
    # car_count = str(car_count)
    car_count = str(len(showroom_data) + 1)
    new_data["ID"] = car_count
    mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, mode, encoding="utf-8") as file:

        if mode == "w" or os.path.getsize(file_name) == 0:
            file.write(f"{header_line}\n")

        for key, value in new_data.items():
            format_key = f"{key:<12}".replace(" ", "-")
            file.write(f"{format_key}:\t{car_count if key=='ID' else value}\n")

        file.write(f"{separator_line}\n")
    showroom_data.append(new_data)


# ============================================================================


def load_data(what_file=file_name, what_array=showroom_data):
    """
    Loads car data from a file into a list.

    Parameters:
    - what_file (str): The name of the file from which to load the data.
    - what_array (list): The list to populate with the loaded car data.
    """
    loaded_data = {}
    count = 0

    readable = False

    if os.path.exists(file_name):
        readable = bool(os.path.getsize(file_name) > 0)
    else:
        with open(file_name, "w"):
            pass

    if readable:
        with open(what_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if not line.startswith("="):
                    key, value = line.split(":")
                    loaded_data[key.strip("-")] = value.strip("\n")
                elif not any(char.isalpha() for char in line):
                    count += 1
                    what_array.append(loaded_data)
                    loaded_data = {}


# ============================================================================


def save_data(file_path=file_name, cars=showroom_data):
    """
    Saves the car data to a specified file.

    Parameters:
    - file_path: The file to write the car data to.
    - cars: The list of car dictionaries to save.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        local_car_count = 0
        file.write(f"{header_line}\n")
        for car in cars:
            local_car_count += 1
            for key, value in car.items():
                format_key = f"{key:<12}".replace(" ", "-")
                if key == "ID":
                    car_value = str(local_car_count)
                else:
                    car_value = value.strip()
                file.write(f"{format_key}:\t{car_value}\n")
            file.write(f"{separator_line}\n")


# ============================================================================
def main():
    pass


if __name__ == "__main__":
    main()
