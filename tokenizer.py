import re


def tokenize(text):
   token_spec = [
      ('TANIMLA', r'tanimla'),
      ('GOSTER', r'goster'),
      ('TOPLA', r'topla'),
      ('ESITTIR', r'='),
      ('ARTI', r'\+'),
      ('SAYI', r'\d+'),
      ('DEGISKEN', r'\w+'),
      ('BOSLUK', r'\s+'),
      ('UYUMSUZ', r'.'),
      ('ATLA', r'atla'),
   ]
   token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_spec)
   tokens = []
   for match in re.finditer(token_regex, text):
        kind = match.lastgroup
        value = match.group()
        if kind == 'BOSLUK':
            continue
        elif kind == 'UYUMSUZ':
            raise RuntimeError(f"Illegal character {value}")
        tokens.append((kind, value))
   return tokens
