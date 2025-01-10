import wikipedia
wikipedia.set_lang('fr')

page = wikipedia.summary("Genco Gulan", sentences=3)
print(page)
