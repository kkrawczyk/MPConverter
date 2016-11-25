class StringUtils(object):
    @staticmethod
    def encode(f, t, text):
        try:
            return unicode(text, f).encode(t)
        except:
            return text

    @staticmethod
    def encodeWin2Utf(text):
        return StringUtils.encode("cp1250", "UTF-8", text)

    @staticmethod
    def split2KeyVal(text):
        idx = text.find('=')
        k = text[:idx]
        v = text[idx+1:]
        return (k, v)
