# Common Norwegian words

This repo was made to create a list of common Norwegian words to use for the [MonkeyType](https://monkeytype.com/) website.

The best Norwegian frequency list I could find online is this: <http://korpus.uib.no/humfak/nta/>. More specifically this file: <http://korpus.uib.no/humfak/nta/ordlistf.zip>. The problem is that this frequency list contains words like "finland" (country), "hvad" (old, outdated language) and "2" (number).

To remove such words, this repo uses the Norwegian Scrabble Associasions dictionary (<http://www2.scrabbleforbundet.no/?page_id=1488>) to check whether the words in the frequency list should be included in the final list or not.

An additional list of words which did not feel right to include in the MonkeyType word list is also added and used for additional filtering.

## Usage
Download the repo and run the follwing command to create the MonkeyType files in the correct format:

``` sh
python3 create_monkeytype_files.py
```

A list of .json-files should appear.
