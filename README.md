# Bar Tender
This is a project for the module "NoSQL Datenbanken (cds-115) FS25".

## Setup
BarTender is intendet to be run in a Docker Container. Therefore, you must have Docker running on your device. Ensure, that you run the following commands in the rootfolder of this application. Also, it is important, that the root folder is named "BarTender" as the application determins absolute paths with this name.

### Create the docker image
    docker build -t bar_tender .
### Run the container with a mongo-DB
    docker-compose up -d

## Test the Application
Go to http://localhost:6969/apidocs/ to access the Swagger docs and tryout the REST interface.

## Dump some example data
This repo has some example data prepared to try out the REST Interface.
### Dump the data
    docker cp ./data/dump mongodb-container:/data/db/dump

### Restore the dump
    docker exec -it mongodb-container mongorestore --username root --password example --authenticationDatabase admin --drop /data/db/dump

## About the App
Bar Tender is a smart cocktail-making application that stores drink recipes and controls pumps to automatically mix beverages. Users can create their own custom drinks by defining step-by-step instructions, including activating pumps for liquid ingredients or prompting manual actions for garnish and shaking.

## Entities

| Entity          | Explanation                                      |
|----------------|------------------------------------------------|
| Recipe       | Holds all steps needed to create a cocktail. The elements like ingridients are not linked to any of the other collections, as it is the responsibility of the controller to determine, how a step is executed. Therefore, any linking will be done during runtime. The recipes can be filtered, such that only recipes are shown, that dont take any action from the user. |
| Step          | An action in the recipe (pump activation or user prompt). |
| Pump          | Tracks, which Pin is connected to which Pump and what ingredients is connected to that pump.    |
| Glas   | Some default options for the user, when creating a new recipe.    |
| Ingredient      | Some default options for the user, when creating a new recipe.     |

## Notes for Module NoSQL Datenbanken (cds-115) FS25

### App Functionality & Scope
This application is designed to control pumps by activating specific pins on a microcontroller. However, in this version, no pump control is implemented, and no endpoint is available to execute a recipe. This functionality is out of scope for the current module request and will be added in a future release.

The Folders jupiternotebooks, log and test as well as the file dockerEnvironmentVariables.env have no functionallity in this version. They are left in, as they will have functionallity in later stages or are used for further development.

### PUT Endpoint Behavior
The `PUT` endpoint serves as both an **update** and **create** operation:  

- **Updating an Existing Entry**: If the provided ID exists in the database, the entry is updated.  
- **Creating a New Entry**: If the ID does not exist or is `null`, a new entry is created. However, any user-provided ID is ignored, as the database generates its own unique ID.  
- If a user submits a `PUT` request for a new entry **without providing all fields**, missing fields will be set to `null`.  
- This behavior may change in future versions, but it currently allows for a flexible API while the frontend and controller are still in development.  
