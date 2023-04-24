# hanzi-writer-data-youyin
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![trello](https://img.shields.io/badge/Trello-UDE-blue])](https://trello.com/b/HmfuRY2K/untitleddesktop)
[![Discord](https://img.shields.io/discord/717037253292982315.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/4wgH8ZE)

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
To use the data in your website simply create a custom data loader function like this below:
```js
async function charDataLoader(character, onLoad, onError)
{
    let response = await fetch(`https://cdn.jsdelivr.net/gh/MadLadSquad/hanzi-writer-data-youyin@latest/data/${character}.json`)
    if (await response.status !== 200)
    {
        console.log(`Bad response from both the character database, this is mainly caused by missing characters. Response code: ${response.status}`);
        return;
    }
    return await response.json();
}
```
this is a real world example used on the [youyin website](https://github.com/MadLadSquad/YouyinWeb)

Next, simply use the custom loader when creating your writer like this:
```js
let writer = HanziWriter.create(`character-target-div`, "ぷ", // deliberately use a Japanese Kana here
{
    width: 100,
    heigt: 100,
    padding: 5,
    showOutline: true,
    strokeAnimationSpeed: 1.25,
    delayBetweenStrokes: 50,
    charDataLoader: charDataLoader, // Use the custom data loader
})
target.addEventListener('mouseover', function() 
{
    writer.animateCharacter();
});
```
and you're done, now you can use the database.

Additionally, if you want to specify Korean or Japanese characters(for example to have an option to use Chinese, Japanese or 
Korean strokes), you can change the name from something like `高.json` to `高-ko.json`(Korean version) or `高-jp.json`
(Japanese version) in the loader function. This will load the alternative version when available, if no alternative is found,
the request will response with a non-200 response, at which point you might want to consider loading a different version of the
character

## Generating data
All data here is autogenerated using the `ci.sh` shell script. It's a couple of lines of code, it simply generates the Chinese,
Japanese, Korean, Kana and secondary Chinese data, merges the characters and copies them to the data directory

## Licensing
The code is licensed under MIT, the data is subject to the licenses used by the projects we depend on, mainly the following:
1. [hanzi-writer-data](https://github.com/chanind/hanzi-writer-data)
1. [makemeahanzi](https://github.com/skishore/makemeahanzi)
1. [hanzi-writer-data-jp](https://github.com/chanind/hanzi-writer-data-jp)
1. [animCJK](https://github.com/parsimonhi/animCJK)
