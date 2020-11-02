

def removePuncuation(args):
    newText = ''
    puncuation = ''';"'^<>(){}&%$#@!~_)(/*-+'''
    text, case, removePunc, space, newline= [args[i] for i in ('text', 'case', 'removePunc', 'space', 'newline')]
    if text:
        removePunc = True if removePunc == 'on' else False
        space = True if space == 'on' else False
        newline = True if newline == 'on' else False
        
        if removePunc or space or newline:
            i = 0
            length = len(text)
            while i < length:
                flg = True
                if removePunc:
                    if text[i] in puncuation:
                        flg = False
                if newline:
                    if text[i] == "\n" or text[i] == "\r":
                        flg = False
                if space:
                    if text[i] == ' ' and text[i+1] == ' ':
                        flg = False
                if flg:
                    newText += text[i]
                i += 1
        else:
            newText = text
        if case == 'upper':
            newText = newText.upper()
        elif case == 'lower':
            newText = newText.lower()
        return newText
    return newText
