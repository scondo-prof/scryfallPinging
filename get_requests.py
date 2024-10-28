import httpx
from dotenv import load_dotenv

header = {"User-Agent": "scootsEnigm/1.0"}


def get_scryfall_card_search(query_string: str) -> list[dict]:

    scryfall_cards = []
    request = httpx.get(
        url=f"https://api.scryfall.com/cards/search?{query_string}", headers=header
    )

    response = request.json()
    total_cards = response["total_cards"]
    scryfall_cards += response["data"]

    while len(response["data"]) == 175:
        print("next page")
        request = httpx.get(
            url=response["next_page"],
            headers=header,
        )

        response = request.json()
        scryfall_cards += response["data"]

    return scryfall_cards


def get_scryfall_set(set_name: str) -> dict:
    request = httpx.get(headers=header, url=f"https://api.scryfall.com/sets/{set_name}")
    set_obj = request.json()

    return set_obj


def get_all_scryfall_sets() -> list[dict]:
    request = httpx.get(headers=header, url="https://api.scryfall.com/sets")
    sets_obj = request.json()["data"]

    return sets_obj


def get_all_sets_by_set_type(set_type: str) -> list[dict]:
    set_type_sets = []
    scryfall_sets = get_all_scryfall_sets()
    for scryfall_set in scryfall_sets:
        if scryfall_set["set_type"] == set_type:
            set_type_sets.append(scryfall_set)

    return set_type_sets


# get_scryfall_card_search(query_string="order=cmc&q=c%3Ared+pow%3D3")
# print(get_scryfall_set(set_name="commander"))

# print(get_all_scryfall_sets())
# print(get_all_sets_by_set_type(set_type="commander"))
