from pyscript import display


club_members = ["Carmel Villamora", "Gian Beauxtanaut", "Miles Sarmiento", "Archie Martinez", "Luthien Agustine"]
from js import document

def check_membership(event):

    first_name = document.querySelector("#first-name").value
    last_name = document.querySelector("#last-name").value
    
    full_name = first_name + " " + last_name

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    display(messages[is_member], target="result", append=False)
    
