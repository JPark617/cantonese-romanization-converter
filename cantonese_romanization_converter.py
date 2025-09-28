### INPUT CLEANING

import string

punctuation_remover = str.maketrans('', '', string.punctuation)

def remove_punctuation(text):
    assert isinstance(text, str)
    return text.translate(punctuation_remover)


### ROMANIZATION SYSTEMS

from enum import Enum

class System(Enum):
    ILE = 1
    JYUTPING = 2
    YALE = 3


### SYSTEM: ILE

ile_initials = (
    '',
    'b', 'p', 'm', 'f',
    'd', 't', 'n', 'l',
    'g', 'k', 'ng', 'h',
    'gw', 'kw', 'w',
    'dz', 'ts', 's', 'j',
)

ile_finals = (
    '',
    'aa', 'aai', 'aau', 'aam', 'aan', 'aang', 'aap', 'aat', 'aak',
    'a', 'ai', 'au', 'am', 'an', 'ang', 'ap', 'at', 'ak',
    'o', 'oi', 'ou', 'on', 'ong', 'ot', 'ok',
    'oe', 'oeng', 'oet', 'oek',
    'oey', 'oen', 'oet',
    'e', 'ei', 'eu', 'em', 'eng', 'ep', 'ek',
    'u', 'ui', 'un', 'ung', 'ut', 'uk',
    'y', 'yn', 'yt',
    'i', 'iu', 'im', 'in', 'ing', 'ip', 'it', 'ik',
)

ile_stop_consonants = ('p', 't', 'k')

ile_tones = (1, 1, 2, 3, 4, 5, 6, 7, 8, 9)


### SYSTEM: JYUTPING

jyutping_initials = (
    '',
    'b', 'p', 'm', 'f',
    'd', 't', 'n', 'l',
    'g', 'k', 'ng', 'h',
    'gw', 'kw', 'w',
    'z', 'c', 's', 'j',
)

jyutping_finals = (
    '',
    'aa', 'aai', 'aau', 'aam', 'aan', 'aang', 'aap', 'aat', 'aak',
    'a', 'ai', 'au', 'am', 'an', 'ang', 'ap', 'at', 'ak',
    'o', 'oi', 'ou', 'on', 'ong', 'ot', 'ok',
    'oe', 'oeng', 'oet', 'oek',
    'eoi', 'eon', 'eot',
    'e', 'ei', 'eu', 'em', 'eng', 'ep', 'ek',
    'u', 'ui', 'un', 'ung', 'ut', 'uk',
    'yu', 'yun', 'yut',
    'i', 'iu', 'im', 'in', 'ing', 'ip', 'it', 'ik',
)

jyutping_stop_consonants = ('p', 't', 'k')

jyutping_tones = (1, 1, 2, 3, 4, 5, 6, 1, 3, 6)


### SYSTEM: YALE

yale_initials = (
    '',
    'b', 'p', 'm', 'f',
    'd', 't', 'n', 'l',
    'g', 'k', 'ng', 'h',
    'gw', 'kw', 'w',
    'j', 'ch', 's', 'y',
)

yale_finals = (
    '',
    'a', 'aai', 'aau', 'aam', 'aan', 'aang', 'aap', 'aat', 'aak',
    'a', 'ai', 'au', 'am', 'an', 'ang', 'ap', 'at', 'ak',
    'o', 'oi', 'ou', 'on', 'ong', 'ot', 'ok',
    'eu', 'eung', 'eut', 'euk',
    'eui', 'eun', 'eut',
    'e', 'ei', 'eu', 'em', 'eng', 'ep', 'ek',
    'u', 'ui', 'un', 'ung', 'ut', 'uk',
    'yu', 'yun', 'yut',
    'i', 'iu', 'im', 'in', 'ing', 'ip', 'it', 'ik',
)

yale_ending_consonants = ('m', 'n', 'ng', 'p', 't', 'k')

yale_stop_consonants = ('p', 't', 'k')

yale_tones = ('¯ ', '` ', '´ ', '  ', '`h', '´h', ' h', '¯ ', '  ', ' h')

yale_tones_on_letters = {
    'a': ('ā', 'à', 'á', 'a'),
    'o': ('ō', 'ò', 'ó', 'o'),
    'e': ('ē', 'è', 'é', 'e'),
    'u': ('ū', 'ù', 'ú', 'u'),
    'i': ('ī', 'ì', 'í', 'i'),
    'm': ('m̄', 'm', 'ḿ', 'm'),
    'n': ('n̄', 'ǹ', 'ń', 'n'),
}

def deconstruct_yale_vowel(vowel_with_tone, is_low_tone):
    for vowel in yale_tones_on_letters:
        try:
            match yale_tones_on_letters[vowel].index(vowel_with_tone):
                case 0: tone = '¯'
                case 1: tone = '`'
                case 2: tone = '´'
                case _: tone = ' '
            return vowel, tone + ('h' if is_low_tone else ' ')
        except ValueError:
            pass
    raise ValueError


### ENCODING

def encode_ile(syllables):
    encoded = []
    initials_sorted = sorted(ile_initials, key=len, reverse=True)
    for syllable in syllables:
        initial = next((x for x in initials_sorted if syllable.startswith(x)), None)
        try:
            final = syllable[len(initial):-1]
            tone = int(syllable[-1])
            if final[-1] in ile_stop_consonants:
                match tone:
                    case 1: tone_index = 7
                    case 3: tone_index = 8
                    case 6: tone_index = 9
                    case _: tone_index = ile_tones.index(tone)
            else:
                tone_index = ile_tones.index(tone)
            indices = (
                ile_initials.index(initial),
                ile_finals.index(final),
                tone_index
            )
            if indices[0] == 0 and indices[1] == 0:
                encoded.append(syllable)
            else:
                encoded.append(indices)
        except (IndexError, ValueError) as e:
            encoded.append(syllable)
    return encoded

def encode_jyutping(syllables):
    encoded = []
    initials_sorted = sorted(jyutping_initials, key=len, reverse=True)
    for syllable in syllables:
        initial = next((x for x in initials_sorted if syllable.startswith(x)), None)
        try:
            final = syllable[len(initial):-1]
            tone = int(syllable[-1])
            if final[-1] in jyutping_stop_consonants:
                match tone:
                    case 1: tone_index = 7
                    case 3: tone_index = 8
                    case 6: tone_index = 9
                    case _: tone_index = jyutping_tones.index(tone)
            else:
                tone_index = jyutping_tones.index(tone)
            indices = (
                jyutping_initials.index(initial),
                jyutping_finals.index(final),
                tone_index
            )
            if indices[0] == 0 and indices[1] == 0:
                encoded.append(syllable)
            else:
                encoded.append(indices)
        except (IndexError, ValueError) as e:
            encoded.append(syllable)
    return encoded

def encode_yale(syllables):
    encoded = []
    initials_sorted = sorted(yale_initials, key=len, reverse=True)
    for syllable in syllables:
        try:
            if syllable == "m" or syllable == "mh": # "m" all tones
                initial = 'm'
                final = ''
                tone_index = yale_tones.index('`h')
            else:
                match list(syllable):
                    case [('n̄' | 'ǹ' | 'ń' | 'n') as n_with_tone, 'g']: # "ng" high tones
                        initial = 'ng'
                        final = ''
                        tone_index = yale_tones.index(deconstruct_yale_vowel(n_with_tone, False)[1])
                    case [('n' | 'ǹ' | 'ń') as n_with_tone, 'g', 'h']: # "ng" low tones
                        initial = 'ng'
                        final = ''
                        tone_index = yale_tones.index(deconstruct_yale_vowel(n_with_tone, True)[1])
                    case _:
                        initial = next((x for x in initials_sorted if syllable.startswith(x)), None)
                        final_end = next((x for x in yale_ending_consonants if syllable.endswith(x)), '')
                        final_vowels_with_tone = syllable[len(initial):-len(final_end)] if len(final_end) > 0 else syllable[len(initial):]
                        if final_vowels_with_tone[-1] == 'h': # low tones
                            is_low_tone = True
                            final_vowels = final_vowels_with_tone[:-1]
                        else: # high tones
                            is_low_tone = False
                            final_vowels = final_vowels_with_tone
                        if final_vowels[0] == 'y': # 'yu' vowel with an initial consonant
                            final_start = 'y'
                            final_vowels = final_vowels[1:]
                        elif initial == 'y' and final_vowels in yale_tones_on_letters['u']: # 'yu' vowel without an initial consonant
                            final_start = 'y'
                        else:
                            final_start = ''
                        vowel, tone = deconstruct_yale_vowel(final_vowels[0], is_low_tone)
                        final = final_start + vowel + final_vowels[1:] + final_end
                        if final_end in yale_stop_consonants:
                            match tone:
                                case '¯ ': tone_index = 7
                                case '  ': tone_index = 8
                                case ' h': tone_index = 9
                                case _: tone_index = yale_tones.index(tone)
                        else:
                            tone_index = yale_tones.index(tone)
            indices = (
                yale_initials.index(initial),
                yale_finals.index(final),
                tone_index,
            )
            if indices[0] == 0 and indices[1] == 0:
                encoded.append(syllable)
            else:
                encoded.append(indices)
        except (IndexError, ValueError) as e:
            encoded.append(str(syllable))
            continue
    return encoded

def encode(text, origin_system):
    assert origin_system in System
    syllables = text.lower().split(' ')
    match origin_system:
        case System.ILE: encoded = encode_ile(syllables)
        case System.JYUTPING: encoded = encode_jyutping(syllables)
        case System.YALE: encoded = encode_yale(syllables)
        case _: encoded = text
    return encoded


### DECODING

def decode_ile(syllables):
    decoded = []
    for syllable in syllables:
        if type(syllable) == tuple:
            decoded.append('{}{}{}'.format(
                ile_initials[syllable[0]],
                ile_finals[syllable[1]],
                ile_tones[syllable[2]]
            ))
        else:
            decoded.append(str(syllable))
    return decoded

def decode_jyutping(syllables):
    decoded = []
    for syllable in syllables:
        if type(syllable) == tuple:
            decoded.append('{}{}{}'.format(
                jyutping_initials[syllable[0]],
                jyutping_finals[syllable[1]],
                jyutping_tones[syllable[2]]
            ))
        else:
            decoded.append(str(syllable))
    return decoded

def decode_yale(syllables):
    decoded = []
    for syllable in syllables:
        if type(syllable) == tuple:
            initial = yale_initials[syllable[0]]
            final = yale_finals[syllable[1]]
            tone = yale_tones[syllable[2]]
            final_end = next((x for x in yale_ending_consonants if final.endswith(x)), '')
            final_vowels = final[0:-len(final_end)] if len(final_end) > 0 else final
            if len(final_vowels) == 0: # check for syllabic 'm' and 'ng'
                final_vowels = initial[-1]
                initial = initial[:-1]
            if final_vowels[0] == 'y': # check for finals that start with 'y'
                final_start = '' if initial == 'y' else 'y'
                final_vowels = final_vowels[1:]
            else:
                final_start = ''
            match tone[0]:
                case '¯': final_vowels = yale_tones_on_letters[final_vowels[0]][0] + final_vowels[1:]
                case '`': final_vowels = yale_tones_on_letters[final_vowels[0]][1] + final_vowels[1:]
                case '´': final_vowels = yale_tones_on_letters[final_vowels[0]][2] + final_vowels[1:]
            final_highlow = tone[1].strip()
            decoded.append('{}{}{}{}{}'.format(initial, final_start, final_vowels, final_highlow, final_end))
        else:
            decoded.append(str(syllable))
    return decoded

def decode(syllables, target_system):
    assert target_system in System
    match target_system:
        case System.ILE: decoded = decode_ile(syllables)
        case System.JYUTPING: decoded = decode_jyutping(syllables)
        case System.YALE: decoded = decode_yale(syllables)
        case _: decoded = syllables
    return ' '.join(decoded)


### MAIN

def run_converter():
    print("CANTONESE ROMANIZATION CONVERTER")
    print("--------------------------------")
    print()
    print("Supported romanization systems:")
    for system in System:
        print("{}: {}".format(system.value, system.name))
    print()
        
    input_is_valid = False
    while not input_is_valid:
        origin = input("Input system (enter name or number): ")
        try:
            origin_system = System[origin.upper()]
            input_is_valid = True
        except KeyError:
            try:
                origin_system = System(int(origin))
                input_is_valid = True
            except ValueError as e:
                print("Invalid input system. Please try again.")
        print()
        
    input_is_valid = False
    while not input_is_valid:
        target = input("Output system (enter name or number): ")
        try:
            target_system = System[origin.upper()]
            input_is_valid = True
        except KeyError:
            try:
                target_system = System(int(target))
                input_is_valid = True
            except ValueError as e:
                print("Invalid output system. Please try again.")
        print()

    print("--------------------------------")
    print()

    input_is_valid = False
    while not input_is_valid:
        converter_type = input("Conversion method (line/file): ").lower()
        if converter_type == "line" or converter_type == "file":
            input_is_valid = True
        else:
            print("Invalid conversion method. Please try again.")
        print()

    # line-by-line converter
    if converter_type == "line":
        print("NOTE: Please separate each syllable with a space.")
        print()
        run_again = True
        while run_again:
            input_text = input("Text to be converted: ")
            encoded = encode(remove_punctuation(input_text), origin_system)
            decoded = decode(encoded, target_system)
            print(decoded)
            print()

    # file-to-file converter
    elif converter_type == "file":
        print("NOTE: Ensure that each syllable in the input file is separated with a space.")
        print()
        run_again = True
        while run_again:
            input_file = input("Input file path: ")
            output_file = input("Output file path: ")
            with open(input_file, 'r', encoding='utf8') as reader, open(output_file, 'w', encoding='utf8') as writer:
                for line in reader:
                    encoded = encode(remove_punctuation(line.strip()), origin_system)
                    decoded = decode(encoded, target_system)
                    writer.write(decoded + '\n')
            print("Conversion complete!")
            print()

if __name__ == "__main__":
    run_converter()
