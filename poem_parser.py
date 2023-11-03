import re
import csv

POEM_NAME = 'dontbothertheearthspirit'
POEM_TEXT = POEM_NAME+'.txt'


def text_to_stanzas(poem):
    stanzas = re.split('\n*\d+',poem)
    return stanzas

def stanzas_to_lines(stanzas):
    lines_list = []
    stanza_num = 0
    for stanza in stanzas:
        lines = stanza.split('\n')
        while '' in lines:
            lines.remove('')
        for line in lines:
            if line != '\n':
                lines_list.append({'stanza': stanza_num,
                'line': lines.index(line)+1,
                'line-within-stanza': line}) #drop linebreaks
        stanza_num += 1
    return lines_list

def lines_to_csv(lines_list):
    with open(POEM_NAME+'.csv', 'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['stanza','line','line-within-stanza'])
        writer.writeheader()
        writer.writerows(lines_list)
    return -1


if __name__ == '__main__':
    with open(POEM_TEXT,'r') as poem_file:
        poem = poem_file.read()
        stanzas = text_to_stanzas(poem)
        lines = stanzas_to_lines(stanzas)
        lines_to_csv(lines)


