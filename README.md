# Canonical Technical Assessment - Trello Card Creation

This is a Python CLI tool that creates a Trello card in a specified board column and optionally allows the user to add labels and a comment. This project was created as part of Canonical's technical assessment process.

Time Spent: 3 hours

## Table of Contents
* [Features](#features)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Development Notes](#development_notes)
* [Future Improvements](#future_improvements)
* [Sources Used](#sources_used)

## Features
The features of this Trello CLI tool include:
* Creating a new card on a Trello board
* Adding color-coded labels to the card
* Adding a comment to the card
* Specifying the target column (via list_id) for where the card should be created

## Getting Started
Instructions on how to get a local copy of the project configured and running.

### Project Requirements
* Python 3.8+
* A Trello Account
* Create a Trello Power-Up
* A Trello API Key
* A Trello API Token

### Python Libraries & Dependencies
* requests (Installation Bash Command> pip instal requests)
* argparse  (Part of Python Standard Library)

### Setting Up & Getting Trello API Credentials
1. Create a Trello Power-Up if you have not created on before (https://developer.atlassian.com/cloud/trello/guides/power-ups/managing-apps/#adding-a-new-custom-power-up)
2. Once created, access your Power-Up, navigate to the API Key tabl and select Generate a new API Key (https://trello.com/power-ups/admin)
3. You will need to allow permissions to be redirected to the page with your API key

## Usage
### General Bash Command Line Format
python Canonical_technical_assessment.py \  
API_KEY \
API_TOKEN \
LIST_ID \ 
CARD_NAME \
[--card_desc DESCRIPTION] \
[--label NAME:COLOR] \
[--comment COMMENT]

### Example Bash Command For Card Creation
python Canonical_technical_assessment.py \
your_api_key \
your_api_token \ 
list_list \
"Bug Fix" \
--card_desc "Fix program bug and update error handling." \
--label "Bug:blue" \
--label "Priority:red" \
--comment "Initial issue created"

### Command Line Arguments
* api_key: Trello API Key
* api_token: Trello API Token
* list_id: ID of the list (column) where the card will be created
* card_name: Name of the new card
* --card_desc: Optional card description
* --label: Optional label(s) in format Name:Color (can be repeated)
* --comment: Optional comment added to the new card

### Valid Label Colors
This is the list of label colors supported by Trello. Any input colors not in this list will default to no color.
* green, yellow, orange, red, purple, blue, sky, lime, pink, black

## Development Notes
This tool interacts directly with the Trello REST API using Python and the requests library for HTTP communication.
The Python library argparse is used for CLI argument parsing

### Project Structure
|-- Canonical_technical_assessment.py
|-- README.md

### Script Structure
Each Trello operation is separated into its own function:
* create_card()
* create_card_label()
* create_card_comment()

### Error Handling
This project includes error handling for:
* Trello API request failures and HTTP errors
* Invalid label formats
* Network errors
* Request timeouts

## Future Improvements
Some potential future improvements for this project include:
* Improving CLI UX with subcommands
* Adding structured logging
* Implementating retry logic for API requests
* Adding unit tests
* Extending feature capabilities to interact with:
    * Card Attachments
    * Card Checklists
    * Card Stickers
    * Card Custom Fields
    * Card Members
    * Card Notifications
    * Board Membership
    * Board Actions

## Sources Used
* Generate a new API Key: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
* Create Trello Power-up: https://developer.atlassian.com/cloud/trello/guides/power-ups/managing-apps/#adding-a-new-custom-power-up
* Python Argparse Documentation: https://docs.python.org/3/library/argparse.html#module-argparse
* Trello Developer Notes: https://developer.atlassian.com/cloud/trello/rest/api-group-boards/
* Python Requests Documentation: https://realpython.com/python-requests/

