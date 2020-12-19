import re
alphabets= "([A-Za-z])"
prefixes = "(Rev|Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt|Sr|Sra)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Rev|Mr|Mrs|Ms|Dr|Sr|Sra|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|me|edu)"

def split_into_sentences(text):
    
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = text.replace("...?”","...?”<stop>")
    text = text.replace("....","<stop>")
    text = text.replace(" ....","<stop>")
    text = text.replace(" ...","<stop>")
    text = text.replace("...? ...","<stop>")
    text = text.replace("?...?...","<stop>")
    text = text.replace("...? ","<stop>")
    text = text.replace("...?\n","<stop>")
    text = text.replace(".\"","\"<stop>")
    text = text.replace(".“","\"<stop>")
    text = text.replace(".'","'<stop>")
    text = text.replace(".»","»<stop>")
    text = text.replace("?“","“?")
    text = text.replace("?»","»?")
    text = text.replace("?'","'?")
    text = text.replace("…?","<stop>")
    text = re.sub("…","<stop>",text)
    text = text.replace("...","<stop>")
    text = re.sub("”","\"",text)
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    if "...." in text: text = text.replace("....","<prd><prd><prd><stop>")
    if " ..." in text: text = text.replace(" ...","<prd><prd><prd><stop>")
    if "...? ..." in text: text = text.replace("...? ...","<prd><prd><prd>?<prd><prd><prd><stop>")
    if "?...?..." in text: text = text.replace("?...?...","? <prd><prd><prd>?<prd><prd><prd><stop>")
    if "...? " in text: text = text.replace("...? ","<prd><prd><prd>?<stop>")
    if "...?\n" in text: text = text.replace("...?\n","<prd><prd><prd>?<stop>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    text = re.sub(" \[.[^]]*?Trad.\]","",text)
    text = re.sub(" \[.[^]]*?trad.\]","",text)
    text = re.sub(" - Ed.","",text)
    if "[A-Za-z].)" in text: text = text.replace("[A-Za-z].)","[A-Za-z])<stop>")
    if " ...\"]" in text: text = text.replace(" ...\"]","...\"]")
    if "[Blank.spot.on.tape.]" in text: text = text.replace("[Blank.spot.on.tape.]","[Blank<prd>spot<prd>on<prd>tape<prd>]")
    if "[Blank.spot.on.tape]" in text: text = text.replace("[Blank.spot.on.tape]","[Blank<prd>spot<prd>on<prd>tape]<stop>")
    if "[Blank.spot.on.tape]." in text: text = text.replace("[Blank.spot.on.tape].","[Blank<prd>spot<prd>on<prd>tape]<stop>")
    if "”" in text: text = text.replace(".”","”<stop>")
    if "”" in text: text = text.replace(".'”","'”<stop>")
    if "\"" in text: text = text.replace(".\"","\"<stop>")
    if "\"" in text: text = text.replace(".'\"","'\"<stop>")
    if "\”" in text: text = text.replace(".»\”","»\”<stop>")
    if "\"" in text: text = text.replace(".»\"","»\"<stop>")
    if ".»”" in text: text = text.replace(".»”","»\"<stop>")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if "..." in text: text = text.replace("... ","<prd><prd><prd><stop>")
    if "..." in text: text = text.replace("..., ","<prd><prd><prd><stop>")
    if "...? " in text: text = text.replace("...? ","<prd><prd><prd>?<stop>")
    if "... )" in text: text = text.replace("... )","<prd><prd><prd>)")
    if "... ?" in text: text = text.replace("... ?","<prd><prd><prd>?")
    if "I.\"" in text: text = text.replace("I.\"","I\"<stop>")
    if ".) " in text: text = text.replace(".) ",".) <stop>")
    if ".]" in text: text = text.replace(".]","].<stop>")
    if ".“)" in text: text = text.replace(".“)","\")<stop>")
    if "[Blank.spot.on.tape.]" in text: text = text.replace("[Blank.spot.on.tape.]","[Blank spot on tape.]<stop>")
    if "... " in text: text = text.replace("... ","<prd><prd><prd><stop>")
    text = text.replace(". ",".<stop>")
    text = text.replace("? ","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    #text = text.replace("<dot>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

    
def split_into_paragraphs(text):
    text = " " + text + "  "
    text = re.sub(" \[.[^]]*?Trad.\]","",text)
    text = re.sub(" \[.[^]]*?trad.\]","",text)
    #if "\n[\d]*[a-z]" in text: text = text.replace("\n[\d]*[a-z]","<stop>[\d]* [a-z]")
    #text = re.sub("\n[\d]*[a-z]","<stop>[\d]* [a-z]",text)   
    text = text.replace("\n","<stop>")
    sentences = text.split("<stop>")
    copy = []
    for sentence in sentences:
        if sentence != '':
            copy.append(sentence)
    copy = copy[:-1]
    copy = [s.strip() for s in copy]
    # using split() 
    # to count words in string
    for line in copy:
        line = bytes(line,'utf-8').decode('utf-8','ignore')
        if len(line.split()) >= 200:
            print("Line is over the limit of 200 words: \n" + line)
    return copy