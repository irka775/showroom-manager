# Showroom Manager

Sowroom Manager represents a robust console-based application designed to manage the inventory
of a car showroom efficiently. This project aims to streamline the process of adding, modifying, deleting,
and viewing car details, offering a user-friendly interface for showroom management tasks. The application
leverages various functionalities such as input validation,
file handling, and data manipulation to ensure accurate and seamless management of car inventory.
This Python console offers a comprehensive solution for organizing and maintaining a car showroom's inventory,
catering to the needs of showroom managers and facilitating efficient management of car listings through a simple
yet powerful console interface. This helps new users get acquainted with the application quickly.

## Features

- **Welcome Message and Instructions**:
  Display a welcome message and instructions when the application starts
  to guide users on how to use the different features of the show from the showroom inventory. Users should be able
  to specify the ID of the car they want to delete, and the corresponding car entry should be removed from the inventory.

![Welcome msg](assets\screenshots\welcome_screenshot.JPG "Welcome message")

- **User-Friendly Interface**:
  Design a user-friendly interface using color-coding and clear prompts to guide users
  through different actions such as adding, modifying, deleting, or viewing cars in the showroom.

![Menu](assets\screenshots\app_screenshot.JPG "Menu screenshot")

- **Add Car Functionality**:
  Allow users to add new cars to the showroom inventory by providing details such as brand, model,
  fuel type, engine size, transmission, year, mileage, color, and price.

![Add car](assets\screenshots\addCar_screenshot.JPG "Add car screenshot")

- **Modify Car Functionality**:
  Enable users to modify the details of existing cars in the showroom inventory.
  This feature should allow users to select a car by its ID and update its attributes.
- **Delete Car Functionality**:
  Provide the capability to remove cars from the showroom inventory. Users should be able to specify
  the ID of the car they want to delete, and the corresponding car entry should be removed from the inventory.
- **Show Cars Functionality**:
  Implement a feature to display all cars currently present in the showroom inventory.
  This functionality should show detailed information about each car, including its ID, brand, model, fuel type, etc.

![Show cars](assets\screenshots\addCar_screenshot.JPG "Show cars screenshot")

- **Total Cars Functionality**:
  Show the total number of cars present in the showroom inventory. This feature provides
  users with a quick overview of the current size of the inventory.

![Total cars](assets\screenshots\totalCars_screenshot.JPG "Total cars screenshot")

- **Exit**:
  Exit the application.
- **Data Persistence**:
  Implement data persistence mechanisms to ensure that the showroom inventory data is saved between
  sessions. This ensures that the data is not lost when the application is closed or restarted.
- **Input Validation**:
  Validate user input to ensure that only valid data is accepted. Implement checks to verify that
  input values adhere to specified formats and ranges (e.g., numeric fields should only accept numbers).
- **Error Handling**:
  Handle errors gracefully by providing informative error messages to users when unexpected issues occur.
  This helps users understand the nature of the problem and how to address it.

## Future Features

- **Search and Filter Functionality** :  
  Allow users to search for specific cars or filter cars based on criteria such as brand,
  model, price range, or year.
- **Image Upload and Display**:  
  Enable users to upload images of cars to accompany their details in the inventory.
- **Sorting Options**:  
  Provide options to sort the showroom inventory based on various attributes such as price, year, mileage, or brand.
- **User Authentication and Authorizations**:  
  Implement user authentication and authorization mechanisms to restrict access to certain features or data
  based on user roles.
- **Integration with External Systems**:  
  Integrate the showroom management system with other systems or platforms, such as accounting software, customer
  relationship management (CRM) systems, or online marketplaces.

## Testing

I have manually tested this code by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems
- Test each menu option (adding a car, modifying a car, deleting a car, showing cars,
  displaying the total number of cars, and exiting) to ensure they perform the intended actions.
- Enter different types of input (valid, invalid) when prompted and verify that the
  program handles them correctly.
- Test each data type validation (alphanumeric, numeric, float) with valid and invalid inputs.
- Check for any error messages or unexpected behavior during execution.
- Verify that the program provides appropriate error messages and prompts
  the user to re-enter input when validation fails.
- Verify that the file is created if it doesn't exist and that existing data is
  overwritten or appended as expected.
- Test each function in the code to ensure it performs its intended functionality accurately.
  For example, when adding a car, verify that the car details are correctly added to the showroom
  data and written to the file or similarly, when modifying or deleting a car, verify that
  the specified car is updated or removed from the showroom data.
- Tested in my local terminal and the Code Institute Heroku terminal.

## Validator Testing

- PEP8:  
  No errors were returned from PEP8 online.com

## Deployment

- Steps for deployment:  
  Fork or clone this repository  
  Create a new Heroku app  
  Set the buildbacks to Python and NodeJS in that order  
  Link the Heroku app to the repository  
  Click on Deploy

## Installation

1. Clone or download the repository.
2. Ensure you have Python installed on your system (Python 3.6 or later).
3. Install the required dependencies using pip:

   ```bash
   pip install colorama num2words
   ```

## License

## Usage

Run the main Python script to start the Showroom Manager:

```bash
python showroom_manager.py

Copyright (c) 2024 Irina Barbascumpa

Permission is hereby granted, free of charge,

THE SOFTWARE IS PROVIDED "AS IS",WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR  OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

