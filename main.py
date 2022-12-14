import collections
import sys

from Constants import osrs_items, osrs_locations, osrs_npcs, osrs_actions, count_words, misc_words, alphabet, alphabet_letters

import requests
from bs4 import BeautifulSoup


def scrape_items_osrs():
    items_list = []
    urls = [
        "https://oldschool.runescape.wiki/w/Special:Ask?eq=no&limit=500&offset=0&order=asc&p=format%3Dbroadtable/link%3Dall/headers%3Dshow/searchlabel%3D...-20further-20results/class%3Dsortable-20wikitable-20smwtable&q=[[Category:Free-to-play_items]]%0A[[All+Is+members+only::false]]&sort=#search",
        "https://oldschool.runescape.wiki/w/Special:Ask?eq=no&limit=500&offset=500&order=asc&p=format%3Dbroadtable%2Flink%3Dall%2Fheaders%3Dshow%2Fsearchlabel%3D...-20further-20results%2Fclass%3Dsortable-20wikitable-20smwtable&q=%5B%5BCategory%3AFree-to-play_items%5D%5D%0A%5B%5BAll+Is+members+only%3A%3Afalse%5D%5D&sort=#search",
        "https://oldschool.runescape.wiki/w/Special:Ask?eq=no&limit=500&offset=1000&order=asc&p=format%3Dbroadtable%2Flink%3Dall%2Fheaders%3Dshow%2Fsearchlabel%3D...-20further-20results%2Fclass%3Dsortable-20wikitable-20smwtable&q=%5B%5BCategory%3AFree-to-play_items%5D%5D%0A%5B%5BAll+Is+members+only%3A%3Afalse%5D%5D&sort=#search",
        "https://oldschool.runescape.wiki/w/Special:Ask?eq=no&limit=500&offset=1500&order=asc&p=format%3Dbroadtable%2Flink%3Dall%2Fheaders%3Dshow%2Fsearchlabel%3D...-20further-20results%2Fclass%3Dsortable-20wikitable-20smwtable&q=%5B%5BCategory%3AFree-to-play_items%5D%5D%0A%5B%5BAll+Is+members+only%3A%3Afalse%5D%5D&sort=#search"
    ]

    for item_wiki_url in urls:
        page = requests.get(item_wiki_url)
        soup = BeautifulSoup(page.content, "html.parser")
        all_sections = soup.find_all('table', {"class": "sortable"})
        for section in all_sections:
            items = section.find_all('a')
            for item in items:
                if item not in items_list:
                    print('"' + item.text + '",')
                    items_list.append(item.text)

    print(items_list)


def scrape_npcs_osrs():
    npcs_list = []
    urls = [
        "https://oldschool.runescape.wiki/w/Special:Ask?eq=no&limit=500&offset=0&order=asc&p=format%3Dbroadtable%2Flink%3Dall%2Fheaders%3Dshow%2Fsearchlabel%3D...-20further-20results%2Fclass%3Dsortable-20wikitable-20smwtable&q=%5B%5BCategory%3ANon-player+characters%5D%5D%0A%5B%5BAll+Is+members+only%3A%3Afalse%5D%5D&sort=#search",
        "https://oldschool.runescape.wiki/w/Special:Ask?eq=no&limit=500&offset=500&order=asc&p=format%3Dbroadtable%2Flink%3Dall%2Fheaders%3Dshow%2Fsearchlabel%3D...-20further-20results%2Fclass%3Dsortable-20wikitable-20smwtable&q=%5B%5BCategory%3ANon-player+characters%5D%5D%0A%5B%5BAll+Is+members+only%3A%3Afalse%5D%5D&sort=#search",
    ]

    for npc_wiki_url in urls:
        page = requests.get(npc_wiki_url)
        soup = BeautifulSoup(page.content, "html.parser")
        all_sections = soup.find_all('table', {"class": "sortable"})
        for section in all_sections:
            npcs = section.find_all('a')
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
                            formatted_list.append(item.upper())
                else:
                    if format_str and format_str not in formatted_list:
                        formatted_list.append(format_str[0])

        return formatted_list
    else:
        for str_obj in string_list:
            if str_obj not in formatted_list:
                format_str = str_obj.replace(" ", "").upper()
                formatted_list.append(format_str)

        return formatted_list


def run_search(cipher_list, search_list):
    # FIND MATCHES OF ITEMS AND LOCATIONS
    for x in range(0, len(word_sets)):
        print(word_sets[x])
        freq1 = collections.Counter(cipher_list[x][0])
        freq2 = collections.Counter(cipher_list[x][1])

        left_matches = []
        right_matches = []
        left_right_matches = []

        # check if item is in each side
        for search_word in search_list:
            does_both_match = True
            does_left_match = True
            does_right_match = True
            item_location_letter_freq = collections.Counter(search_word)
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
                left_right_matches.append(search_word)
            if does_left_match:
                left_matches.append(search_word)
            if does_right_match:
                right_matches.append(search_word)

        print("left matches:", set(left_matches))
        print("right matches:", set(right_matches))
        print("left/right matches:", set(left_right_matches))
        print()


if __name__ == "__main__":
    # scrape_npcs_osrs()
    # scrape_items_osrs()
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

    # format methods
    # 0 - original, remove space
    # 1 - split on space
    format_method = 0
    # format word list used for searching
    global_search_word_list = format_list(osrs_items, format_method) + format_list(osrs_npcs, format_method) + format_list(osrs_locations, format_method) + \
                         format_list(osrs_actions, format_method) + format_list(count_words, format_method) + format_list(misc_words, format_method)

    # run the search
    run_search(word_sets, global_search_word_list)
