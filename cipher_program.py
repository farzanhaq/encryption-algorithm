"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import a2.cipher_functions
import os.path

def get_valid_filename(msg):
   """ (str) -> str

   Prompt the user, using msg, to type the name of a file. This file should
   exist in the same directory as the starter code. If the file does not
   exist, keep re-prompting until they give a valid filename.
   Return the name of that file.
   """

   filename = input(msg)
   while not os.path.exists(filename):
       print("That file does not exist.")
       filename = input(msg)
   return filename

def get_encryption_mode():
   """ () -> str

   Prompt the user to enter the encryption mode. If the user enters an invalid
   mode, keep re-prompting until they give a valid mode.
   """

   msg = 'Do you want to encrypt ({0}) or decrypt ({1})? '.format(
             a2.cipher_functions.ENCRYPT, a2.cipher_functions.DECRYPT)
   mode = input(msg)
   while not (mode == a2.cipher_functions.ENCRYPT or
                  mode == a2.cipher_functions.DECRYPT):
       print('Invalid mode.')
       mode = input(msg)
   return mode

def main():
    """ () -> NoneType

    Perform the encryption using the deck from file named DECK_FILENAME and
    the message from file named MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """

    prompt = 'Enter the name of the file that contains the card deck: '
    deck_file = open(get_valid_filename(prompt), 'r')
    deck = a2.cipher_functions.read_deck(deck_file)
    deck_file.close()
    if not (a2.cipher_functions.is_valid_deck(deck)):
        print('The supplied card deck is not a valid deck.')
        print('Encryption process stopping.')
        return

    prompt = 'Enter the name of the file that contains the message: '
    msg_file = open(get_valid_filename(prompt), 'r')
    messages = a2.cipher_functions.read_messages(msg_file)
    msg_file.close()

    mode = get_encryption_mode()

    for msg in a2.cipher_functions.process_messages(deck, messages, mode):
        print(msg)

if __name__ == "__main__":
    main()
