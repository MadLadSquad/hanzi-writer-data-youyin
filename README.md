# hanzi-writer-data-youyin
Merged hanziwriter data + data for all writing systems we support on [Youyin](https://youyin.madladsquad.com/). 

This repository was created mainly to make calls to different characters faster, since if we use the 
[hanzi-writer-data](https://github.com/chanind/hanzi-writer-data), 
[hanzi-writer-data-jp](https://github.com/chanind/hanzi-writer-data-jp) and our own hanzi-writer-others, we would need to make 3
requests in order to locate a non-jp and non-zh character. Because of this we decided to simply merge the 3 projects into a
single monolyth so that we can use only 1 call to fetch a character. 

Additionally, [hanzi-writer-data-jp](https://github.com/chanind/hanzi-writer-data-jp) depends on 
[AnimCJK](https://github.com/parsimonhi/animCJK) for Japanese data, and while that's good, 
[hanzi-writer-data-jp](https://github.com/chanind/hanzi-writer-data-jp) hasn't gotten an update to the data in quite a long time.
To fix this we also autogenerate newer characters from the Japanese data on schedule using github actions. 

Finally, we created this repository to provide more characters to the user. Since Japan, China and Korea,
have different stroke order standards, we decided that it would be better for our users if we merged the Chinese characters so that
they can choose which stroke order they want to use for the given character on the website. Outside of this,
[AnimCJK](https://github.com/parsimonhi/animCJK), also provides data for Japanese Kana, which we extract for our Hiragana and
Katakana support. Data for other writing systems is provided by our own hanzi-writer-others project

Script support:
- [X] Traditional Chinese Characters
- [X] Simplified Chinese Characters
- [X] Japanese Kanji
- [X] Korean Hanja
- [X] Katakana
- [X] Hiragana
- [ ] Latin
- [ ] Cyrillic
- [ ] Armenian
- [ ] Georgian
- [ ] Runic
- [ ] Greek
- [ ] Arabic
- [ ] Zhuyin/BoPoMoFo
- [ ] Hebrew
- [ ] Devanagari
- [ ] Bengali

## Using the data
Coming soon
