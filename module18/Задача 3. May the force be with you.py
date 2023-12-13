import json
import requests
from pprint import pprint
from typing import List, Dict, Union

session = requests.Session()

def get_pilots(starship: Dict[str, str]) -> List[Dict[str, str]]:
    pilots_link_list = starship["pilots"]
    pilots = []
    for link in pilots_link_list:
        pilots_req = session.get(link)
        pilot_data = pilots_req.json()

        homeworld_req = session.get(pilot_data["homeworld"])
        homeworld = homeworld_req.json()["name"]

        pilots.append({
            "height": pilot_data["height"],
            "homeworld": homeworld,
            "homeworld_url": pilot_data["homeworld"],
            "mass": pilot_data["mass"],
            "name": pilot_data["name"]
        })

    return pilots


def get_starships_list() -> List[Dict[str, str]]:
    req = session.get("https://swapi.dev/api/starships/")
    data = req.json()
    return data["results"]


def get_starship(starships_list: List[Dict[str, str]]) -> Dict[str, str]:
    return next((ship for ship in starships_list if ship["name"] == "Millennium Falcon"), None)


def prepare_data_to_be_entered_into_json(starship: Dict[str, str], pilots: List[Dict[str, str]]) -> Dict[str, Union[str, List[Dict[str, str]]]]:
    return {
        "max_atmosphering_speed": starship["max_atmosphering_speed"],
        "pilots": pilots,
        "ship_name": starship["name"],
        "starship_class": starship["starship_class"]
    }


starships_list = get_starships_list()
starship = get_starship(starships_list)
if starship:
    pilots = get_pilots(starship)
    result = prepare_data_to_be_entered_into_json(starship, pilots)

    with open("Millennium Falcon.json", "w") as file:
        json.dump(result, file, indent=4)

    with open("Millennium Falcon.json", "r") as file:
        data = json.load(file)

    pprint(data)