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

    # format and combine word lists, this could use some refactor tbh
    formatted_item_list = []
    for item in osrs_items:
        if item not in formatted_item_list:
            formatted_str = item.replace(" ", "")
            formatted_item_list.append(formatted_str)

    formatted_npcs_list = []
    for npc in osrs_npcs:
        if npc not in formatted_item_list:
            formatted_str = npc.replace(" ", "")
            formatted_npcs_list.append(formatted_str)

    formatted_location_list = []
    for location in osrs_locations:
        if location not in formatted_item_list:
            formatted_str = location.replace(" ", "")
            formatted_location_list.append(formatted_str)

    formatted_actions_list = []
    for action in osrs_actions:
        if action not in formatted_actions_list:
            formatted_str = action.replace(" ", "")
            formatted_location_list.append(formatted_str)

    formatted_misc_words_list = []
    for misc_word in misc_words:
        if misc_word not in formatted_misc_words_list:
            formatted_str = misc_word.replace(" ", "")
            formatted_misc_words_list.append(formatted_str)

    formatted_count_words_list = []
    for count_word in count_words:
        if count_word not in formatted_count_words_list:
            formatted_str = count_word.replace(" ", "")
            formatted_count_words_list.append(formatted_str)

    # combined items and location lists
    item_location_list = formatted_item_list + formatted_location_list + formatted_actions_list +\
                         formatted_misc_words_list + formatted_count_words_list + formatted_npcs_list

    # FIND MATCHES OF ITEMS AND LOCATIONS
    for x in range(0, 9):
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

        print("left matches:", left_matches)
        print("right matches:", right_matches)
        print("left/right matches:", left_right_matches)
        print()
