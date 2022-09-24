import collections
import sys

from Constants import osrs_items, osrs_locations, osrs_npcs, osrs_actions, count_words, misc_words, alphabet, alphabet_letters

import requests
from bs4 import BeautifulSoup


def scrape_items_osrs():
    for filter_letter in alphabet_letters:
        url = f"https://oldschool.runescape.wiki/w/Category:Free-to-play_items?from={filter_letter.upper()}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        all_sections = soup.find_all('div', {"class": "mw-category"})
        for section in all_sections:
            items = section.find_all('li')
            for item in items:
                print('"' + item.text + '",')


def scrape_npcs_osrs():
    npcs_list = []
    urls = [
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pageuntil=Awusah+the+Mayor#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Awusah+the+Mayor#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Brother+Omad#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Commander+Veldaban#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Duel+Guide#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Feanor#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Ghost+%28The+General%27s+Shadow%29#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Hari#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Jonas#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Lizard+man+%282014+April+Fools%29#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Miner+%28Jatizso%29#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Oobapohk#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=R0ck+5masher#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Saro#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Snowman#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Tolna#mw-pages",
        "https://oldschool.runescape.wiki/w/Category:Non-player_characters?pagefrom=Wemund#mw-pages"
    ]

    for npc_wiki_url in urls:
        page = requests.get(npc_wiki_url)
        soup = BeautifulSoup(page.content, "html.parser")
        all_sections = soup.find_all('div', {"class": "mw-category mw-category-columns"})
        for section in all_sections:
            npcs = section.find_all('li')
            for npc in npcs:
                if npc not in npcs_list:
                    print('"' + npc.text + '",')
                    npcs_list.append(npc.text)

    print(npcs_list)

def search_word_list_line_matches(word_sets):
    common_letter_list = []
    for set in word_sets:
        common_letters = []
        s1 = set[0]
        s1_letter_list = [x for x in s1]
        s2 = set[1]
        s2_letter_list = [x for x in s2]

        for letter in s1_letter_list:
            if letter in s2_letter_list:
                common_letters.append(letter)
        common_letter_list.append(common_letters)

    for index, matches in enumerate(common_letter_list):
        print("row:", word_sets[index], "| common letters:", matches)

    return common_letter_list


def search_word_list_column_matches(first_set, second_set):
    for letter_set in first_set:
        second_set_copy = second_set
        letters = [x for x in letter_set]
        for letter in letters:
            second_set_copy = list(filter(lambda x: letter in x, second_set_copy))
        print("letter set:", letter_set, "matching sets:", list(second_set_copy))


def filter_osrs_locations(matched_letters):
    all_matched_letters = []
    for matched_list in matched_letters:
        for letter in matched_list:
            all_matched_letters.append(letter)

    print(all_matched_letters)

    # try to get the location with letters shown
    location_list = []
    for location in osrs_locations:
        location_list.append(location.lower())

    for letter in all_matched_letters:
        location_list = list(filter(lambda x: letter.lower() in x, location_list))
        print("Filtered Down with letter " + letter, location_list)

    print("search results:", location_list)


def remove_letter_from_str(letter, str):
    return str.replace(letter, '', 1)


def format_list(string_list, method=None):
    formatted_list = []
    if method == 1:
        for str_obj in string_list:
            if str_obj not in formatted_list:
                format_str = str_obj.split(" ")
                if len(format_str) > 1:
                    for item in format_str:
                        if item and item not in formatted_list:
                            formatted_list.append(item)
                else:
                    if format_str and format_str not in formatted_list:
                        formatted_list.append(format_str[0])

        return formatted_list
    else:
        for str_obj in string_list:
            if str_obj not in formatted_list:
                format_str = str_obj.replace(" ", "")
                formatted_list.append(format_str)

        return formatted_list


if __name__ == "__main__":
    # scrape_items_osrs()
    # get_osrs_locations()
    # scrape_npcs_osrs()

    """
        "Between the two, you'll find a match.
        Easy you think, but there's a catch."
    """

    first_set = [
        "YPWAIETOAENRMHMGEN",
        "NQLLWQMIRLVFSDROTN",
        "LINVADMCURYBOFEUAI",
        "VRBOOHHSDEWEAANANN",
        "ANHIITBICPATELTTMH",
        "SFTOAINWLXARKLANFE",
        "OENIRSRONOFKGVEKAR",
        "EHERESSOVEMDGJTCWS",
        "TASEWNHEVGRANOKNOT",
        "HRFRONLRATTATTIQAT"
    ]

    second_set = [
        "MIVWDMKDTCBANGBFKW",
        "VKIIAAKIRLHADHESVG",
        "DRULRHTDEESEBREPYE",
        "EERATOLITEJEPEPZFN",
        "FEKETCHPMSNAFEWNQM",
        "NEWEDSANENTEGQLHUA",
        "TLBGONGUWHILPAFNAS",
        "RDMCORRODAPJNLSAWY",
        "SHTOELHTICUTMLHOIO",
        "ANEUOASGNHSFALEHND"
    ]

    word_sets = [
        ("YPWAIETOAENRMHMGEN", "MIVWDMKDTCBANGBFKW"),
        ("NQLLWQMIRLVFSDROTN", "VKIIAAKIRLHADHESVG"),
        ("LINVADMCURYBOFEUAI", "DRULRHTDEESEBREPYE"),
        ("VRBOOHHSDEWEAANANN", "EERATOLITEJEPEPZFN"),
        ("ANHIITBICPATELTTMH", "FEKETCHPMSNAFEWNQM"),
        ("SFTOAINWLXARKLANFE", "NEWEDSANENTEGQLHUA"),
        ("OENIRSRONOFKGVEKAR", "TLBGONGUWHILPAFNAS"),
        ("EHERESSOVEMDGJTCWS", "RDMCORRODAPJNLSAWY"),
        ("TASEWNHEVGRANOKNOT", "SHTOELHTICUTMLHOIO"),
        ("HRFRONLRATTATTIQAT", "ANEUOASGNHSFALEHND"),
    ]
    # methods
    # 0 - original, remove space
    # 1 - split on space
    search_method = 0
    # format and combine word lists, this could use some refactor tbh
    item_location_list = format_list(osrs_items, search_method) + format_list(osrs_npcs, search_method) + format_list(osrs_locations, search_method) + \
                         format_list(osrs_actions, search_method) + format_list(count_words, search_method) + format_list(misc_words, search_method)

    # FIND MATCHES OF ITEMS AND LOCATIONS
    for x in range(0, 10):
        print(word_sets[x])
        freq1 = collections.Counter(word_sets[x][0])
        freq2 = collections.Counter(word_sets[x][1])

        left_matches = []
        right_matches = []
        left_right_matches = []

        # check if item is in each side
        for item_location in item_location_list:
            does_both_match = True
            does_left_match = True
            does_right_match = True
            item_location_letter_freq = collections.Counter(item_location)
            for letter in item_location_letter_freq.keys():
                if freq1[letter] >= item_location_letter_freq[letter] and freq2[letter] >= item_location_letter_freq[letter]:
                    continue
                elif freq1[letter] >= item_location_letter_freq[letter] and not freq2[letter] >= item_location_letter_freq[letter]:
                    does_right_match = False
                    does_both_match = False
                    continue
                elif not freq1[letter] >= item_location_letter_freq[letter] and freq2[letter] >= item_location_letter_freq[letter]:
                    does_left_match = False
                    does_both_match = False
                    continue
                else:
                    does_both_match = False
                    does_left_match = False
                    does_right_match = False

            if does_both_match:
                left_right_matches.append(item_location)
            if does_left_match:
                left_matches.append(item_location)
            if does_right_match:
                right_matches.append(item_location)

        print("left matches:", set(left_matches))
        print("right matches:", set(right_matches))
        print("left/right matches:", set(left_right_matches))
        print()
