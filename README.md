# Cantonese Romanization Converter

An interactive Python script to convert between different common romanization systems of the Cantonese language.


## Context

Cantonese is a language primarily spoken in Southern China, Hong Kong, and Macau, as well as in various overseas communities. As a part of the Yue Chinese branch of languages, it is mutually unintelligible with Chinese languages outside of this branch such as Mandarin and Hokkien. Furthermore, because Cantonese has not been elevated to the same political and social status as Standard Chinese (a form of Mandarin) in mainland China, there has not yet arisen a *de facto* standard romanization system for Cantonese in the same way that Hanyu Pinyin exists for Mandarin. There are a handful of systems commonly in use today along with many smaller and/or historical systems, and each system has a different approach to representing the wonderfully complex phonology of the Cantonese language!

Here is an example (using the poem 春曉 by 孟浩然) to help give a sense of the similarities and differences between these systems and also show why this can get pretty confusing:

| System | Text |
| ----------- | ----------- |
| Cantonese | 春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少？ |
| IPA (for linguists) | /tsʰɵn˥ miːn˨˩ bɐt̚˥ kɔːk̚˧ hiːu̯˧˥ tsʰyː˧ tsʰyː˧ mɐn˨˩ tʰɐi̯˨˩ niːu̯˩˧ jɛː˨ lɔːy̯˨˩ fʊŋ˥ jyː˩˧ sɪŋ˥ faː˥ lɔːk̚˨ tsiː˥ tɔː˥ siːu̯˧˥/ |
| Guangdong Romanization | Cên<sup>1</sup> min<sup>4</sup> bed<sup>1</sup> gog<sup>3</sup> hiu<sup>2</sup>, qu<sup>3</sup> qu<sup>3</sup> men<sup>4</sup> tei<sup>4</sup> niu<sup>5</sup>. Yé<sup>6</sup> loi<sup>4</sup> fung<sup>1</sup> yu<sup>5</sup> xing<sup>1</sup>, fa<sup>1</sup> log<sup>6</sup> ji<sup>1</sup> do<sup>1</sup> xiu<sup>2</sup>? |
| ILE (Cantonese Pinyin) | Tsoen1 min4 bat7 gok8 hiu2, tsy3 tsy3 man4 tai4 niu5. Je6 loi4 fung1 jy5 sing1, faa1 lok9 dzi1 do1 siu2? |
| Jyutping | Ceon1 min4 bat1 gok3 hiu2, cyu3 cyu3 man4 tai4 niu5. Je6 loi4 fung1 jyu5 sing1, faa1 lok6 zi1 do1 siu2? |
| Sidney Lau | Chun<sup>1</sup> min<sup>4</sup> bat<sup>1°</sup> gok<sup>3</sup> hiu<sup>2</sup>, chue<sup>3</sup> chue<sup>3</sup> man<sup>4</sup> tai<sup>4</sup> niu<sup>5</sup>. Ye<sup>6</sup> loi<sup>4</sup> fung<sup>1</sup> yue<sup>5</sup> sing<sup>1</sup>, fa<sup>1°</sup> lok<sup>6</sup> ji<sup>1</sup> doh<sup>1</sup> siu<sup>2</sup>? |
| Standard Romanization | Ch‘un mīn pat kòk hiú, ch‘uè ch‘uè mān t‘aī niŭ. Yê loī fung yuĕ shing, fa lôk chi toh shiú? |
| Yale | Chēun mìhn bāt gok híu, chyu chyu màhn tàih níuh. Yeh lòih fūng yúh sīng, fā lohk jī dō síu? |

Note that, although this converter will recognize the high falling tone (distinguished by some speakers from the high level tone) as well as checked tones in any romanization systems that specifically denote these concepts, many romanization systems do not distinguish these sounds from level tones in general, and so some information may be lost in conversion.


## Usage

Simply run the `cantonese_romanization_converter.py` file using Python! The program will ask you which two romanization systems you want to convert between, as well as whether you want to interactively convert one line at a time or convert an entire file at once.

Note that each Cantonese syllable must be separated by a space, since otherwise the program will not recognize it as Cantonese. The program will automatically turn the input text entirely lowercase and remove all punctuation before attempting to convert. Any non-Cantonese or otherwise unrecognized text will not be altered further.

This program currently supports conversion between the ILE (Cantonese Pinyin), Jyutping, and Yale systems.


## Compatibility

This script requires Python 3.12 or above.


## Resources

Sources and further reading:
- [Cantonese language – Wikipedia](https://en.wikipedia.org/wiki/Cantonese)
- [廣州話拼音方案 GuangZhou Dialect (Cantonese) Romanisation Scheme](https://web.archive.org/web/20091208043921/http://www.sungwh.freeserve.co.uk/chinese/gzhhpy.htm)
- [ILE Romanization of Cantonese - Wikipedia](https://en.wikipedia.org/wiki/ILE_romanization_of_Cantonese)
- [Jyutping - Wikipedia](https://en.wikipedia.org/wiki/Jyutping)
- [Table of Jyutping symbols](https://www.cantoneselearning.com/jyutping)
- [Sidney Lau romanization - Wikipedia](https://en.wikipedia.org/wiki/Sidney_Lau_romanisation)
- [Standard Romanization (Cantonese) - Wikipedia](https://en.wikipedia.org/wiki/Standard_Romanization_(Cantonese))
- [Yale romanization of Cantonese - Wikipedia](https://en.wikipedia.org/wiki/Yale_romanization_of_Cantonese)