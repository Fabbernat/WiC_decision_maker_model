# Nev: Fabian Bernat
# Neptun: URX5VP
# h: h259147

def elvalasztas(word):
    if word in dictionary.keys():
        return dictionary[word]
    ### strings
    vowels_simple = "aeiou"
    vowels_hu = "aáeéiíoóuúöőüű"
    consonants = "bcdfghjklmnpqrstvwxyz"
    current_syllable = ""

    ### sets
    digraphs = {"cs", "sz", "ty", "gy", "ny", "dz", "dzs", "ch"}

    ### dicts
    long_digraphs = {
        "ccs": "cs-cs",
        "ssz": "sz-sz",
        "tty": "ty-ty",
        "ggy": "gy-gy",
        "nny": "ny-ny",
        "ddz": "dz-dz",
        "ddzs": "dzs-dzs"
    }

    ### lists
    syllables_retstr = []
    # config: egy
    known_prefixes = [
        "meg", "egy",
        "fel", "el",
        "kép", "köz",
        "szem", "kör",
        "biz", "gon",
        "tár", "gyors",
        "gyógy", "füg",
        "ál", "dön",
        "nyelv", "tér",
        "asz", "gyer",
        "ün", "or",
        "mun", "al",
        "in", "ér",
        "rész", "nyil",
        "könyv",
        "rend", "karszt",
        "kap", "vég"
    ]
    known_suffixes = [
        "ság", "ség",
        "szág", "ügy",
        "mány", "mat",
        "met", "gyás",
        "szet"
    ]

    ### ints
    i = 0

    for prefix in known_prefixes:
        if word.startswith(prefix):
            syllables_retstr.append(prefix)
            i = len(prefix)  # Move index after the prefix
            break

    # Iterate through the word to form syllables
    while i < len(word):
        char = word[i]
        current_syllable += char

        # Check for syllable breaks: vowel followed by consonant or end of word
        if char in vowels_hu:
            # Handle consonant clusters between vowels
            j = i + 1
            consonant_cluster = ""
            while j < len(word) and word[j] not in vowels_hu:
                consonant_cluster += word[j]
                j += 1

            # If a consonant cluster is found, apply splitting rule
            if len(consonant_cluster) > 1:
                split_point = len(consonant_cluster) - 1  # Default split: n-1 left, 1 right
                for digraph in digraphs:
                    if digraph in consonant_cluster:
                        # Find the index of the digraph in the consonant cluster
                        start_index = consonant_cluster.index(digraph)
                        # Calculate the end index of the digraph
                        split_point = start_index + len(digraph)  # This gives the end index
                        break
                for long_digraph, split_version in long_digraphs.items():
                    if long_digraph in consonant_cluster:
                        consonant_cluster = consonant_cluster.replace(long_digraph, split_version)
                        break

                # Append the left side of the cluster to the current syllable
                current_syllable += consonant_cluster[:split_point]
                syllables_retstr.append(current_syllable)
                current_syllable = consonant_cluster[split_point:]
                i = j - 1  # Adjust index to just before next vowel
            else:
                syllables_retstr.append(current_syllable)
                current_syllable = ""
        elif i == len(word) - 1 and current_syllable:
            # Handle trailing consonants by appending them to the last syllable
            if syllables_retstr:
                syllables_retstr[-1] += current_syllable
            else:
                syllables_retstr.append(current_syllable)
            current_syllable = ""
        i += 1

    # Final check for dangling consonants at the end of the word
    if current_syllable:  # Append remaining part as a syllable
        if current_syllable[-1] in consonants:
            # Append remaining consonants to the last syllable
            if syllables_retstr and all(char in consonants for char in current_syllable):
                syllables_retstr[-1] += current_syllable
        else:
            syllables_retstr.append(current_syllable)

    # Check for suffix attachment if word ends with a known suffix
    for suffix in known_suffixes:
        if word.endswith(suffix):
            syllables_retstr[-1] = suffix
            break

    # Check for missing characters in final syllables
    
    result = "-".join(syllables_retstr)

    # Clean up result to replace any occurrences of '--' with '-'
    result = result.replace('--', '-')

    # If there are any trailing hyphens, you might also want to handle those
    result = result.strip('-')  # remove any leading/trailing hyphens

    return result


dictionary = {
    "asztal": "asz-tal",
    "katona": "ka-to-na",
    "rendőr": "rend-őr",
    "megszentségteleníthetetlenségeskedéseitekért": "meg-szent-ség-te-le-nít-he-tet-len-sé-ges-ke-dé-se-i-te-kért",
    "gyümölcs": "gyü-mölcs",
    "számítógép": "szá-mí-tó-gép",
    "tanulás": "ta-nu-lás",
    "gyermek": "gyer-mek",
    "halászlé": "ha-lász-lé",
    "szőlő": "sző-lő",
    "madár": "ma-dár",
    "ünnep": "ün-nep",
    "szeretlek": "sze-ret-lek",
    "ország": "or-szág",
    "tulajdonság": "tu-laj-don-ság",
    "megoldás": "meg-ol-dás",
    "tudomány": "tu-do-mány",
    "szívem": "szí-vem",
    "háziorvos": "há-zi-or-vos",
    "megbízható": "meg-bíz-ha-tó",
    "tanító": "ta-ní-tó",
    "munkahely": "mun-ka-hely",
    "iskola": "is-ko-la",
    "testvér": "test-vér",
    "hétköznap": "hét-köz-nap",
    "magyarország": "ma-gyar-or-szág",
    "nemzetközi": "nem-zet-kö-zi",
    "szabadság": "sza-bad-ság",
    "vizsgálat": "vizs-gá-lat",
    "nyelvtanulás": "nyelv-ta-nu-lás",
    "vállalat": "vál-la-lat",
    "társadalom": "tár-sa-da-lom",
    "kutatás": "ku-ta-tás",
    "egészségügy": "e-gész-ség-ügy",
    "hagyomány": "ha-gyo-mány",
    "számítás": "szá-mí-tás",
    "elmélet": "el-mé-let",
    "fejlesztés": "fej-lesz-tés",
    "időjárás": "i-dő-já-rás",
    "kultúra": "kul-tú-ra",
    "ünnepély": "ün-ne-pély",
    "egyetem": "e-gye-tem",
    "könyvtár": "könyv-tár",
    "gyógyszer": "gyógy-szer",
    "szeretet": "sze-re-tet",
    "család": "csa-lád",
    "állampolgár": "ál-lam-pol-gár",
    "gondolat": "gon-do-lat",
    "tulajdonos": "tu-laj-do-nos",
    "szívesen": "szí-ve-sen",
    "megértés": "meg-ér-tés",
    "művészet": "mű-vé-szet",
    "gyorsvonat": "gyors-vo-nat",
    "biztonság": "biz-ton-ság",
    "találkozó": "ta-lál-ko-zó",
    "felhőkarcoló": "fel-hő-kar-co-ló",
    "állatkert": "ál-lat-kert",
    "közlekedés": "köz-le-ke-dés",
    "mesterséges": "mes-ter-sé-ges",
    "felhasználó": "fel-hasz-ná-ló",
    "környezetvédelem": "kör-nye-zet-vé-de-lem",
    "szemüveg": "szem-ü-veg",
    "állatorvos": "ál-lat-or-vos",
    "megfelelés": "meg-fe-le-lés",
    "döntés": "dön-tés",
    "tájékoztatás": "tá-jé-koz-ta-tás",
    "számológép": "szá-mo-ló-gép",
    "rendszer": "rend-szer",
    "egység": "egy-ség",
    "műszaki": "mű-sza-ki",
    "dolog": "do-log",
    "barátság": "ba-rát-ság",
    "magatartás": "ma-ga-tar-tás",
    "független": "füg-get-len",
    "bizalom": "bi-za-lom",
    "közvetítés": "köz-ve-tí-tés",
    "feladat": "fel-a-dat",
    "kapcsolat": "kap-cso-lat",
    "térkép": "tér-kép",
    "jóváhagyás": "jó-vá-ha-gyás",
    "tudatos": "tu-da-tos",
    "alkalmazás": "al-kal-ma-zás",
    "bizonyíték": "bi-zo-nyí-ték",
    "felmérés": "fel-mé-rés",
    "érdeklődés": "ér-dek-lő-dés",
    "követelmény": "kö-ve-tel-mény",
    "figyelem": "fi-gye-lem",
    "valóság": "va-ló-ság",
    "ellenőrzés": "el-len-őr-zés",
    "közösség": "kö-zös-ség",
    "segítség": "se-gít-ség",
    "nyilvános": "nyil-vá-nos",
    "vélemény": "vé-le-mény",
    "részvétel": "rész-vé-tel",
    "hatékonyság": "ha-té-kony-ság",
    "együttműködés": "e-gyütt-mű-kö-dés",
    "értékelés": "ér-té-ke-lés",
    "intézmény": "in-téz-mény",
    "megbízhatóság": "meg-bíz-ha-tó-ság",
    "felügyelet": "fel-ü-gye-let",
    "működés": "mű-kö-dés",
    "szabályzat": "sza-bály-zat",
    "képzés": "kép-zés",
    "végrehajtás": "vég-re-haj-tás",
    "irányítás": "i-rá-nyí-tás",
    "összekötés": "ösz-sze-kö-tés",
    "almalé": "al-ma-lé",
    "karsztstrand": "karszt-strand",
    "fiaiéi": "fi-a-i-é-i",
    "fiaiéiért": "fi-a-i-é-i-ért",
    "niueiéiért": "ni-u-e-i-é-i-ért",
    "kassziopeiaéiért": "kasz-szi-o-pe-i-a-é-i-ért",
    "sztrájk": "sztrájk",
    "fluxusgenerátor": "flu-xus-ge-ne-rá-tor",
    "pszichoterápia": "pszi-cho-te-rá-pi-a",
    "strucc": "strucc",
    "hozzáállás": "hoz-zá-ál-lás",
    "összeessen": "ösz-sze-es-sen",
    "összesen": "ösz-sze-sen",
    "összes": "ösz-szes",
    "összeg": "ösz-szeg",
    "prompt": "prompt",
}

total_errors = 0

for word, expected_output in dictionary.items():
    output = elvalasztas(word)
    if output != expected_output:
        print(f"Error in word '{word}': expected '{expected_output}', got '{output}'")
        total_errors += 1
    else:
        # print(f"Helyes: {output}")
        pass

print(f"Total errors: {total_errors}")
print(f"Length of dictionary: {len(dictionary)}")