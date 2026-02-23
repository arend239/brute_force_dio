#!/usr/bin/env python3
import itertools

def gen_leets(word):
    map_leet = {
        'a': ['a', '4', '@'],
        'e': ['e', '3'],
        'i': ['i', '1', '!'],
        'o': ['o', '0'],
        's': ['s', '5', '$'],
        't': ['t', '7']
    }

    res = [''.join(items) for items in itertools.product(*[map_leet.get(c.lower(), [c]) for c in word])]
    return res

def professional_wordlist(base_keywords):
    suffixes = ['', '123', '2024', '2025', '2026', '!', '@', '01']
    wordlist = set()

    for kw in base_keywords:
        variations = {kw.lower(), kw.upper(), kw.capitalize()}

        for v in variations:
            leets = gen_leets(v)
            for l in leets:
                for s in suffixes:
                    wordlist.add(f"{l}{s}")
                    wordlist.add(f"{s}{l}")

    return sorted(list(wordlist))

def main():
    print("--- Professional Wordlist Generator ---")

    targets = input("Insira palavras-chave separadas por vírgula (ex: admin,ti,empresa): ")
    keywords = [k.strip() for k in targets.split(',')]

    output_file = "wordlists/targeted_wordlist.txt"

    results = professional_wordlist(keywords)

    with open(output_file, "w") as f:
        for word in results:
            f.write(f"{word}\n")

    print(f"\n[+] Sucesso! {len(results)} senhas geradas em: {output_file}")

if __name__ == "__main__":
    main()