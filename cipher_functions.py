# Functions for implementing an encryption or decryption algorithm
# By Farzan Haq and Pratiman Shahi
# 06/11/2015

# Global variables
ENCRYPT = 'e'
DECRYPT = 'd'


def clean_message(message):
    """ (str) -> str

    Return a copy of the message that includes only its alphabetical characters,
    where each of those characters has been converted to uppercase.

    >>> clean_message('abcde')
    'ABCDE'

    >>> clean_message('abcd  *&& 7FG')
    'ABCDFG'
    """
    cleaned_message = ''

    for i in range(len(message)):
        if message[i].isalpha():
            cleaned_message += message[i].upper()

    return cleaned_message


def encrypt_letter(uppercase_letter, keystream_value):
    """ (str, int) -> str

    Precondition: len(uppercase_letter) == 1 and uppercase_letter.isupper()

    Apply the keystream_value to uppercase_letter to encrypt uppercase_letter,
    and return the result.

    >>> encrypt_letter('C', 6)
    'I'

    >>> encrypt_letter('X', 3)
    'A'
    """
    # Translate to number in the range 0-25. 'A' translates to 0, 'B' to 1, etc
    ord_diff = ord(uppercase_letter) - ord('A')

    # Apply the right shift; we use % to handle the end of the alphabet.
    # The result is still in the range 0-25
    new_char_ord = (ord_diff + keystream_value) % 26

    # Convert back to a letter
    return chr(new_char_ord + ord('A'))


def decrypt_letter(uppercase_letter, keystream_value):
    """ (str, int) -> str

    Precondition: len(uppercase_letter) == 1 and uppercase_letter.isupper()

    Apply the keystream_value to uppercase_letter to decrypt uppercase_letter,
    and return the result.

    >>> decrypt_letter('J', 2)
    'H'

    >>> decrypt_letter('B', 3)
    'Y'
    """
    # Translate to number in the range 0-25. 'A' translates to 0, 'B' to 1, etc
    ord_diff = ord(uppercase_letter) - ord('A')

    # Apply the left shift. we use % to handle the end of the alphabet.
    # The result is still in the range 0-25.
    new_char_ord = (ord_diff - keystream_value) % 26

    # Convert back to a letter
    return chr(new_char_ord + ord('A'))


def swap_cards(card_deck, deck_index):
    """ (list of int, int) -> NoneType

    Precondition: deck_index < len(card_deck)

    Swap card at deck_index with card that follows it. card_deck is circular.

    >>> card_deck = [1, 2, 5, 4, 3]
    >>> deck_index = 2
    >>> swap_cards(card_deck, deck_index)
    >>> card_deck
    [1, 2, 4, 5, 3]

    >>> card_deck = [2, 4, 1, 3]
    >>> deck_index = 3
    >>> swap_cards(card_deck, deck_index)
    >>> card_deck
    [3, 4, 1, 2]
    """
    # Special case when deck_index refers to last index in card_deck.
    # Holds value of card at first index in order to perform swap
    if deck_index == len(card_deck) - 1:
        held_value = card_deck[0]
        card_deck[0] = card_deck[deck_index]
        card_deck[len(card_deck) - 1] = held_value
    # Regular case when deck_index does not refer to last index in card_deck;
    # Holds value of card at given index in order to perform swap
    else:
        held_value = card_deck[deck_index]
        card_deck[deck_index] = card_deck[deck_index + 1]
        card_deck[deck_index + 1] = held_value


def get_small_joker_value(card_deck):
    """ (list of int) -> int

    Return the value of the small joker (second highest card)
    for the given card_deck

    >>> get_small_joker_value([1, 2, 5, 4, 3])
    4

    >>> get_small_joker_value([8, 1, 9, 7, 3, 4, 5, 2, 6])
    8
    """
    # Removes the highest value from card_deck (big joker), calls max function
    # on the modified card_deck, then re-inserts big joker
    big_joker_value = get_big_joker_value(card_deck)
    big_joker_index = card_deck.index(big_joker_value)

    card_deck.remove(big_joker_value)
    small_joker_value = max(card_deck)
    card_deck.insert(big_joker_index, big_joker_value)

    return small_joker_value


def get_big_joker_value(card_deck):
    """ (list of int) -> int

    Return the value of the big joker (highest card) for the given card_deck.

    >>> get_big_joker_value([1, 7, 4, 2, 3, 6, 5])
    7

    >>> get_big_joker_value([5, 4, 3, 2, 1])
    5
    """
    return max(card_deck)


def move_small_joker(card_deck):
    """ (list of int) -> NoneType

    Swap small joker with following card in card_deck. card_deck is circular.

    >>> card_deck = [2, 1, 9, 7, 3, 8, 6, 5, 4]
    >>> move_small_joker(card_deck)
    >>> card_deck
    [2, 1, 9, 7, 3, 6, 8, 5, 4]

    >>> card_deck = [3, 1, 2]
    >>> move_small_joker(card_deck)
    >>> card_deck
    [2, 1, 3]
    """
    small_joker_index = card_deck.index(get_small_joker_value(card_deck))

    swap_cards(card_deck, small_joker_index)


def move_big_joker(card_deck):
    """ (list of int) -> NoneType

    Move the big joker two cards down the card_deck. card_deck is circular.

    >>> card_deck = [2, 1, 9, 7, 3, 6, 5, 8, 4]
    >>> move_big_joker(card_deck)
    >>> card_deck
    [2, 1, 7, 3, 9, 6, 5, 8, 4]

    >>> card_deck = [1, 2, 3, 4, 5]
    >>> move_big_joker(card_deck)
    >>> card_deck
    [2, 5, 3, 4, 1]
    """
    # Variable is assigned the value of the big_joker_index
    big_joker_index = card_deck.index(get_big_joker_value(card_deck))

    # Special case when index refers to last_index in card_deck;
    # Two consecutive swaps performed, second swap occurs at card on top of deck
    if big_joker_index == len(card_deck) - 1:
            swap_cards(card_deck, big_joker_index)
            swap_cards(card_deck, 0)
    # Regular case when index does not refers to last_index in card_deck;
    # Two consecutive swaps performed starting at given index then at next index
    else:
        swap_cards(card_deck, big_joker_index)
        swap_cards(card_deck, big_joker_index + 1)


def triple_cut(card_deck):
    """ (list of int) -> NoneType

    Do a triple cut on the card_deck.

    >>> card_deck = [2, 1, 7, 3, 9, 6, 5, 8, 4]
    >>> triple_cut(card_deck)
    >>> card_deck
    [4, 9, 6, 5, 8, 2, 1, 7, 3]

    >>> card_deck = [5, 3, 2, 1, 4]
    >>> triple_cut(card_deck)
    >>> card_deck
    [5, 3, 2, 1, 4]
    """
    # Variable(s) assigned the values after calling previous functions
    big_joker_index = card_deck.index(get_big_joker_value(card_deck))
    small_joker_index = card_deck.index(get_small_joker_value(card_deck))
    first_joker = min(small_joker_index, big_joker_index)
    second_joker = max(small_joker_index, big_joker_index)

    # Slicing and storing values in lists and adding them to a card_deck list
    top_deck = []
    for card in range(first_joker):
        top_deck.append(card_deck[card])

    mid_deck = []
    for card in range(first_joker, second_joker + 1):
        mid_deck.append(card_deck[card])

    bottom_deck = []
    for card in range(second_joker + 1, len(card_deck)):
        bottom_deck.append(card_deck[card])

    new_card_deck = bottom_deck + mid_deck + top_deck
    card_deck.clear()

    for card in new_card_deck:
        card_deck.append(card)


def insert_top_to_bottom(card_deck):
    """ (list of int) -> NoneType

    Examine the value of the bottom card of card_deck; move that many cards from
    top of card_deck to the bottom, inserting them just above the bottom card.
    If bottom card is big joker, use value of small joker as number of cards.

    >>> card_deck = [1, 2, 5, 4, 3]
    >>> insert_top_to_bottom(card_deck)
    >>> card_deck
    [4, 1, 2, 5, 3]

    >>> card_deck = [1, 2, 6, 5, 3, 7, 4, 8]
    >>> insert_top_to_bottom(card_deck)
    >>> card_deck
    [1, 2, 6, 5, 3, 7, 4, 8]
    """
    # Variable refers to value of card at bottom of card_deck
    bottom_card_value = card_deck[-1]
    # Iterate through card_deck from top to bottom_card_val, and insert cards
    # at the bottom of card_deck prior to removing them from original positions
    for card in card_deck[:bottom_card_value]:
        card_deck.insert(-1, card)
        card_deck.remove(card)


def get_card_at_top_index(card_deck):
    """ (list of int) -> int

    Using the value of the top card as an index, return the card in card_deck at
    that index. If top card is the big joker, use value of small joker as index.

    >>> get_card_at_top_index([2, 4, 3, 1])
    3

    >>> get_card_at_top_index([10, 1, 2, 3, 9, 5, 6, 7, 8, 4])
    4
    """
    # Variable refers to value of card at top of deck
    if card_deck[0] != get_big_joker_value(card_deck):
        top_card_value = card_deck[0]
        return card_deck[top_card_value]
    else:
        return card_deck[-1]


def get_next_keystream_value(card_deck):
    """ (list of int) -> int

    Return valid keystream value after all five steps of the algorithm execute
    using the given card_deck.

    >>> get_next_keystream_value([1, 4, 5, 7, 3, 2, 9, 10, 13, 12, 6, 8, 11])
    10

    >>> get_next_keystream_value([7, 4, 2, 5, 1, 3, 6])
    2
    """
    joker_value = get_big_joker_value(card_deck)

    while joker_value == get_big_joker_value(card_deck) or \
          joker_value == get_small_joker_value(card_deck):
        # Execute the five steps of the algorithm
        move_small_joker(card_deck)
        move_big_joker(card_deck)
        triple_cut(card_deck)
        insert_top_to_bottom(card_deck)
        joker_value = get_card_at_top_index(card_deck)

    return joker_value


def process_messages(card_deck, message_list, encrypt_or_decrypt):
    """ (list of int, list of str, str) -> list of str

    Return a list of encrypt_or_decrypt messages using the given card_deck,
    in the same order as they appear in the message_list.

    >>> process_messages([1, 2, 3, 4, 5], ['lake hylia', 'lake', 'hylia'], 'e')
    ['NDMFJBNLC', 'MDLG', 'JANLC']

    >>> process_messages([3, 5, 7, 9], [''NDMFJBNLC', 'MDLG', 'JANLC'], 'd')
    Error
    """
    # Variables refer to empty lists
    e_or_d_list = []
    modified_list = []

    # Iterate through message_list and append messages to e_or_d_list after
    # performing clean_message on each message
    for message in message_list:
        e_or_d_list.append(clean_message(message))

    # Iterate through e_or_d_list and perform encrypt_letter or decrypt_letter
    # on each each letter before adding it hold, appending hold to modified list
    if encrypt_or_decrypt == ENCRYPT:
        for message in e_or_d_list:
            processed_message = ''
            for letter in message:
                processed_message += encrypt_letter \
                    (letter, get_next_keystream_value(card_deck))
            modified_list.append(processed_message)
        return modified_list
    elif encrypt_or_decrypt == DECRYPT:
        for message in e_or_d_list:
            processed_message = ''
            for letter in message:
                processed_message += decrypt_letter \
                    (letter, get_next_keystream_value(card_deck))
            modified_list.append(processed_message)
        return modified_list


def read_messages(message_file):
    """ (file open for reading) -> list of str

    Read and return the contents of the file as a list of messages,
    in the order in which they appear in the message_file.
    Strip the newline from each line.
    """
    list_messages = []

    for line in message_file:
        line = line.strip()
        list_messages.append(line)

    return list_messages


def is_valid_deck(candidate_card_deck):
    """ (list of int) -> bool

    Return True if and only if the candidate_card_deck is a valid deck of cards.

    >>> is_valid_deck([1, 8, 7, 4, 5, 2, 3, 6])
    True

    >>> is_valid_deck([1, 4, 2])
    False
    """
    # Variable refers to value of big joker
    big_joker_value = get_big_joker_value(candidate_card_deck)
    # String accumulator
    new_deck = ''

    # Determine length of card_deck, and iterate through each card to identify
    # if it does not repeat and is of appropriate length
    if len(candidate_card_deck) == big_joker_value and \
       len(candidate_card_deck) >= 3:
        for num in candidate_card_deck:
            if str(num) not in new_deck and num <= big_joker_value:
                return True

    return False


def read_deck(deck_file):
    """ (file open for reading) -> list of int

    Read and return the numbers that are in the deck_file,
    in the order in which they appear in the deck_file.
    """
    card_deck = []

    for line in deck_file:
        new_line = line.split()
        for i in range(len(new_line)):
            card_deck.append(int(new_line[i]))

    return card_deck
