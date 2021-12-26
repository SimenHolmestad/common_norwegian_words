def write_output_monkeytype_file(words, num_words_for_file):
    # Add quotes and spaces around the input words and limit list to required amount
    output_word_lines = list(map(lambda x: f"    \"{x}\",", words))[:num_words_for_file]

    # Remove comma at last line for valid json
    output_word_lines[-1] = output_word_lines[-1][:-1]

    filename = f"norwegian_{num_words_for_file // 1000}k.json"
    print(f"Writing {filename}")

    with open(filename, 'w') as f:
        print("{", file=f)
        print(f"  \"name\": \"norwegian_{num_words_for_file // 1000}k\",", file=f)
        print("  \"leftToRight\": true,", file=f)
        print("  \"bcp47\": \"no-NO\",", file=f)
        print("  \"words\": [", file=f)
        print("\n".join(output_word_lines), file=f)
        print("  ]", file=f)
        print("}", file=f)


def write_output_txt_file(words, num_words_for_file):
    filename = f"common_norwegian_words_{num_words_for_file}.txt"
    print(f"Writing {filename}")
    with open(filename, 'w') as f:
        print("\n".join(words[:num_words_for_file]), file=f)


def main():
    with open("frequency_list.txt", "r", encoding='latin-1') as f:
        frequency_lines = f.readlines()

    # Remove frequency information from file
    frequency_words = [x[7:].strip() for x in frequency_lines]

    with open("scrabble_word_list.txt", "r") as f:
        scrabble_words = set([line.strip() for line in f.readlines()])

    with open("unapproved_words.txt", "r") as f:
        unapproved_words = set([line.strip() for line in f.readlines()])

    passed_words = []

    for word in frequency_words:
        if (word in scrabble_words) and (word not in unapproved_words):
            passed_words.append(word)

    print(f"{len(passed_words)} words passed the test.")

    write_output_monkeytype_file(passed_words, 1000)
    write_output_monkeytype_file(passed_words, 5000)
    write_output_monkeytype_file(passed_words, 10000)


if __name__ == '__main__':
    main()
