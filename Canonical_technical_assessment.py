# importing libraries
import argparse
import requests
from requests.exceptions import Timeout, HTTPError

def create_card(args):
    """ Creates a new card on a provided Trello board """
    
    url = "https://api.trello.com/1/cards"

    # Create card data for request
    request_info = {
            'key': args.api_key,
            'token': args.api_token,
            'idList': args.list_id,
            'name': args.card_name,
            'desc': args.card_desc
        }

    # Add card to specified column of Trello board
    try:
        response = requests.post(url, params=request_info, timeout=10)
        response.raise_for_status() # Raise exception for HTTP errors
        card_id = response.json()['id']
        print("Card Created")
        return card_id
    except Timeout:
        print("Error: The request timed out for Card Creation")
    except HTTPError as e:
        print(f"HTTP error occurred: {e} for Card")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e} for Card")

    return None


def create_card_label(args, card_id):
    """ Creates a new label for an existing card """

    valid_label_colors = {"green", "yellow", "orange", "red", "purple", "blue",
                          "sky", "lime", "pink", "black"}

    url = f"https://api.trello.com/1/cards/{card_id}/labels"

    if not args.label:
        return

    for label in args.label:
        try: 
            label_name, label_color = label.split(":")
        except ValueError:
            raise argparse.ArgumentTypeError("Label must be in format Name:Color")

        label_name = label_name.strip()
        label_color = label_color.strip().lower()

        if not label_name:
            raise argparse.ArgumentTypeError("Label Name cannot be empty")

        if label_color not in valid_label_colors:
            label_color = None

        # Create label data for request
        request_info = {
                'key': args.api_key,
                'token': args.api_token,
                'color': label_color,
                'name': label_name
            }

        # Add label to card
        try:
            response = requests.post(url, params=request_info, timeout=10)
            response.raise_for_status() # Raise exception for HTTP errors
            print(f"{label_name} - Label Created")
        except Timeout:
            print(f"Error: The request timed out for Label Creation - {label_name}")
        except HTTPError as e:
            print(f"HTTP error occurred: {e} for Label - {label_name}")
        except requests.exceptions.RequestException as e:
            print(f"An unexpected error occurred: {e} for Label - {label_name}")
 

def create_card_comment(args, card_id):
    """ Creates a new comment for an existing card """
    url = f"https://api.trello.com/1/cards/{card_id}/actions/comments"

    # Create comment data for request
    request_info = {
            'key': args.api_key,
            'token': args.api_token,
            'text': args.comment
        }

    # Add comment to card
    try:
        response = requests.post(url, params=request_info, timeout=10)
        response.raise_for_status() # Raise exception for HTTP errors
        print(f"Comment Created:{args.comment}")
    except Timeout:
        print("Error: The request timed out for Comment Creation")
    except HTTPError as e:
        print(f"HTTP error occurred: {e} for Comment")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e} for Comment")



def main():
    # create a parser object
    parser = argparse.ArgumentParser(description = "Add a new card to a Trello board.")

    # add arguments
    parser.add_argument("api_key", help="Trello API Key", type=str)
    parser.add_argument("api_token", help="Trello API Token", type=str)
    parser.add_argument("list_id", help="Trello Column List ID", type=str)
    parser.add_argument("card_name", help="Card Name", type=str)
    parser.add_argument("--card_desc", help="Card Description")

    parser.add_argument("--label", action="append", help="Add Card Label in Format Name:Color (can be repeated)")
    parser.add_argument("--comment", help="Card Comment")
    

    # parse the arguments from standard input
    args = parser.parse_args()

    # Create card with input information
    card_id = create_card(args)
    
    # Add any labels to card
    if args.label:
        create_card_label(args, card_id)

    # Add comment to card
    if args.comment:
        create_card_comment(args, card_id)


if __name__ == "__main__":
    main()



















    




