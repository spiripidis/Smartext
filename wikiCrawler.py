import wikipedia


def wiki_run(userwiki):
    try:
        return wikipedia.summary(userwiki)
    except wikipedia.DisambiguationError as e:
        return e
