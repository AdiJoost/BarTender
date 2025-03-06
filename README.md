# Bar Tender
This is a project for the module "NoSQL Datenbanken (cds-115) FS25".

## Setup
BarTender is intendet to be run in a Docker Container. Therefore, you must have Docker running on your device. Ensure, that you run the commands of the 

### Create the docker image
    docker build -t bar_tender .
### Run the container with a mongo-DB
    docker-compose up d

## Test the Application
Go to http://localhost:6969/apidocs/ to access the Swagger docs and tryout the REST interface.

## Dump some example data
This repo has some example data prepared to try out the REST Interface.
### Dump the data
    docker cp ./dump mongodb-container:/data/db/dump+

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
The App is intended to controll pumps via activation of pins on a microcontroller. However, in this version of the app, no controll is implemented and no Endpoint is available to execute a recipe. This is out of scope for the module request and will be implemented in a later version.

The PUT endpoint acts as an Update as well. If the user calls the PUT with an ID that already exists in the DB, the entry is updated. If the ID does not exist or is null, a new entry is created. In that case, the ID given by the user is thrown away, as the db is responsible for choosing an adequate ID. Keep in mind, in this version, if the user PUTs a new entry and does not give all fields, the fields will be instantiated as null. This behaviour may change in the future, but is currently left like this to allow a flexible API while developing the frontend and controller.
