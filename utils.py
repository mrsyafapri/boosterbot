import requests
import translators as ts


def random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    if response.status_code == 200:
        word_en = response.text.replace('["', "").replace('"]', "")
        word_id = ts.google(word_en, to_language="id").lower()
    else:
        word_en = "Word not found"
        word_id = "Kata tidak ditemukan"
    return word_en, word_id


def random_image():
    url = "https://source.unsplash.com/random"
    response = requests.get(url)
    if response.status_code == 200:
        image = response.url
        return image
    else:
        return None


def random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        fact_en = data["text"]
        fact_id = ts.google(fact_en, to_language="id")
        return fact_en, fact_id
    else:
        return "Fact not found", "Fakta tidak ditemukan"


def random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote_en = data["content"]
        quote_id = ts.google(quote_en, to_language="id")
        author = data["author"].upper()
        tags = data["tags"]
        return quote_en, quote_id, author, tags
    else:
        return "Quote not found", "Quote tidak ditemukan", None, None


def random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["type"] == "twopart":
            joke_en = f"- {data['setup']}\n- {data['delivery']}"
            joke_id = (
                "- "
                + ts.google(data["setup"], to_language="id")
                + "\n"
                + "- "
                + ts.google(data["delivery"], to_language="id")
            )
        else:
            joke_en = data["joke"]
            joke_id = ts.google(joke_en, to_language="id")
        return joke_en, joke_id
    else:
        return "Joke not found", "Joke tidak ditemukan"


def dict_en(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        first_en = f"{data['meanings'][0]['partOfSpeech']}: {data['meanings'][0]['definitions'][0]['definition']}"
        second_en = (
            f"{data['meanings'][1]['partOfSpeech']}: {data['meanings'][1]['definitions'][0]['definition']}"
            if len(data["meanings"]) > 1
            else None
        )
        first_id = ts.google(first_en, to_language="id")
        second_id = ts.google(second_en, to_language="id") if second_en else None
        try:
            pronunciation = data["phonetics"][0]["text"] if data["phonetics"] else None
        except KeyError:
            try:
                pronunciation = (
                    data["phonetics"][1]["text"] if data["phonetics"] else None
                )
            except KeyError:
                pronunciation = None
        if second_en and second_id:
            return first_en, second_en, first_id, second_id, pronunciation
        else:
            return first_en, None, first_id, None, pronunciation
    else:
        return None, None, None, None, None


def dict_id(word):
    url = f"https://new-kbbi-api.herokuapp.com/cari/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["data"][0]
        first_id = f"{data['arti'][0]['kelas_kata']}: {data['arti'][0]['deskripsi']}"
        second_id = (
            f"{data['arti'][1]['kelas_kata']}: {data['arti'][1]['deskripsi']}"
            if len(data["arti"]) > 1
            else None
        )
        first_en = ts.google(first_id, to_language="en")
        second_en = ts.google(second_id, to_language="en") if second_id else None
        pronunciation = data["lema"]
        if second_en and second_id:
            return first_id, second_id, first_en, second_en, pronunciation
        else:
            return first_id, None, first_en, None, pronunciation
    else:
        return None, None, None, None, None
