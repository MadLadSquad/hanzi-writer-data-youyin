# hanzi-writer-data-others
Data for other writing systems for hanziwriter

Script support:
- [ ] Katakana
- [ ] Hiragana
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

## Using data
To use the data simply implement a custom loader function in Hanziwriter like this:
```js
async function charDataLoader(character, onLoad, onError)
{
    let response = await fetch(`https://cdn.jsdelivr.net/gh/MadLadSquad/hanzi-writer-data-others@latest/data/${character}.json`);
    if (await response.status !== 200)
    {
        console.log("ERROR");
        return;
    }
    return await response.json();
}

function createHanziWriter()
{
    let target = document.getElementById("character-target-div");

    let writer = HanziWriter.create("character-target-div", "Ж",
    {
        width: 100,
        height: 100,
        padding: 5,
        showOutline: true,
        strokeAnimationSpeed: 1.25,
        delayBetweenStrokes: 50,
        charDataLoader: charDataLoader,
    });

    target.addEventListener('mouseover', function() 
    {
        writer.animateCharacter();
    });
}
```
if you want to have support for the Hanzi database or the Hanzi and JP databases simply change the character loader function to 
this
```js

async function charDataLoader(character, onLoad, onError)
{
    let f = await fetch(`https://cdn.jsdelivr.net/gh/MadLadSquad/hanzi-writer-data-others@latest/data/${character}.json`);
    if (await f.status !== 200)
    {
        let response = await fetch(`https://cdn.jsdelivr.net/gh/chanind/hanzi-writer-data@latest/data/${character}.json`);
        if (await response.status !== 200)
        {
            let res = await fetch(`https://cdn.jsdelivr.net/gh/chanind/hanzi-writer-data-jp@latest/data/${character}.json`);
            if (await res.status !== 200)
            {
                console.log(`Bad response from both the Chinese and Japanese hanzi databases, ZH: ${response.status}, JP: ${res.status}`);
                return;
            }
            return await res.json();
        }
        return await response.json();
    }
    return await f.json();
}
```
This loads both the other scripts, the Chinese data and the JP data. Though this code is somewhat slow(especially when trying to 
load Chinese or JP data) you can use various optimization methods such as Unicode parsing

This project mainly uses [Noto fonts](https://fonts.google.com/noto)
