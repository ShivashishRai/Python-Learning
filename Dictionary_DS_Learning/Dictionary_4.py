
#Merging of Collections



#Nested Collction :Collection inside the one collection

json_example = [{'title':'Stories for Ages',
                 'Books': ['50 Shades','RamCharitra', 'Ramayan','Tales of Laxma'],
                 'Account':('Savings','Current','Deposit', 'Cheque','Loan')
                 }]

print(json_example[0]['Books'][2])


json_example = {
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": {
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": [
              "GML",
              "XML"
            ]
          },
          "GlossSee": "markup"
        }
      }
    }
  }
}

print(json_example['glossary']['GlossDiv']['GlossList']['GlossEntry']['Acronym'])        #SGML

print(json_example['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][1])   #XML