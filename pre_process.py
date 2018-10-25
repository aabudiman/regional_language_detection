from urllib.parse import urlparse
import re

def tokenize1(teks):
#     kata = teks.decode('unicode_escape').encode('ascii','ignore')
    kata = teks.lower()
    kata = re.sub(r'[^\x00-\x7F]+',' ', kata)
    kata = re.sub(r'\d+', "", kata)
    kata = kata.replace("rt", "")
    kata = kata.replace(".", "")
    kata = kata.replace(",", "")
    kata = kata.replace(":", "")
    kata = kata.replace(";", "")
    kata = kata.replace("|", "")
    kata = kata.replace("%", "")
    kata = kata.replace("!", "")
    kata = kata.replace("/", " ")
    kata = kata.replace("?", "")
    kata = kata.replace("'", "")
    kata = kata.replace("&", "")
    kata = kata.replace("\"", "")
    kata = kata.replace("(", " ")
    kata = kata.replace(")", "")
    kata = kata.replace("\\", " ")
    kata = kata.replace("[", "")
    kata = kata.replace("]", "")
    kata = kata.replace("=", "")
    kata = kata.replace("_", "")
    kata = kata.replace("-__-", "")
    kata = kata.replace("--", "")
    kata = kata.replace(" -", "")
    kata = kata.replace("*", "")
    kata = kata.replace("  ", " ")
    kata = kata.replace("@", "")

    kalimat = kata.strip()

    return kalimat

def tokenize2(teks):
    new_string = ''
    for i in teks.split():
        s, n, p, pa, q, f = urlparse(i)
        if s and n:
            pass
        elif i[:1] == '@':
            pass
        elif i[:1] == '#':
            new_string = new_string.strip() + ' ' + i[1:]
        else:
            new_string = new_string.strip() + ' ' + i
    return new_string