# Cantonese Romanization Converter

An interactive Python script to convert between different common romanization systems of the Cantonese language.


## Context

Cantonese is a language primarily spoken in Southern China, Hong Kong, and Macau, as well as in various overseas communities. As a part of the Yue Chinese branch of languages, it is mutually unintelligible with Chinese languages outside of this branch such as Mandarin and Hokkien. Furthermore, because Cantonese has not been elevated to the same political and social status as Standard Chinese (a form of Mandarin) in mainland China, there has not yet arisen a *de facto* standard romanization system for Cantonese in the same way that Hanyu Pinyin exists for Mandarin. There are a handful of systems commonly in use today along with many smaller and/or historical systems, and each system has a different approach to representing the wonderfully complex phonology of the Cantonese language!

Here is an example (using the poem 春曉 by 孟浩然) to help give a sense of the similarities and differences between these systems, and also why this can get pretty confusing:

| System | Text |
| ----------- | ----------- |
| Cantonese | 春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少？ |
| IPA (for linguists) | /tsʰɵn˥ miːn˨˩ bɐt̚˥ kɔːk̚˧ hiːu̯˧˥ tsʰyː˧ tsʰyː˧ mɐn˨˩ tʰɐi̯˨˩ niːu̯˩˧ jɛː˨ lɔːy̯˨˩ fʊŋ˥ jyː˩˧ sɪŋ˥ faː˥ lɔːk̚˨ tsiː˥ tɔː˥ siːu̯˧˥/ |
| ----------- | ----------- |
| ILE (Cantonese Pinyin) | Tsoen1 min4 bat7 gok8 hiu2, tsy3 tsy3 man4 tai4 niu5. Je6 loi4 fung1 jy5 sing1, faa1 lok9 dzi1 do1 siu2? |
| Jyutping | Ceon1 min4 bat1 gok3 hiu2, cyu3 cyu3 man4 tai4 niu5. Je6 loi4 fung1 jyu5 sing1, faa1 lok6 zi1 do1 siu2? |
| Sidney Lau | Chun1 min4 bat1 gok3 hiu2, chue3 chue3 man4 tai4 niu5. Ye6 loi4 fung1 yue5 sing1, fa1 lok6 ji1 do1 siu2? |
| Yale | Chēun mìhn bāt gok híu, chyu chyu màhn tàih níuh. Yeh lòih fūng yúh sīng, fā lohk jī dō síu? |

Note that, although this converter will recognize the high falling tone as well as checked tones in any applicable romanization systems, many romanization systems do not reflect these differences, and so some information may be lost in conversion.


## Usage

Simply run the `cantonese_romanization_converter.py` file using Python! The program will ask you which two romanization systems you want to convert between, as well as whether you want to interactively convert one line at a time or convert an entire file at once.

Note that each Cantonese syllable must be separated by a space, since otherwise the program will not recognize it as Cantonese. The program will automatically turn the input text entirely lowercase and remove all punctuation before attempting to convert. Any non-Cantonese or otherwise unrecognized text will not be altered further.

This program currently supports conversion between the Jyutping and Yale systems.


## Compatibility

This script requires Python 3.12 or above.


## Resources

Sources and further reading:
- [Cantonese language – Wikipedia](https://en.wikipedia.org/wiki/Cantonese)
- [ILE Romanization of Cantonese - Wikipedia](https://en.wikipedia.org/wiki/ILE_romanization_of_Cantonese)
- [Jyutping - Wikipedia](https://en.wikipedia.org/wiki/Jyutping)
- [Table of Jyutping symbols](https://www.cantoneselearning.com/jyutping)
- [Sidney Lau romanization](https://en.wikipedia.org/wiki/Sidney_Lau_romanisation)
- [Yale romanization of Cantonese - Wikipedia](https://en.wikipedia.org/wiki/Yale_romanization_of_Cantonese)
