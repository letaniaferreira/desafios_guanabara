print('app das vogais')
palavras = ('feliz', 'triste', 'avocada', 'bff', 'roblox', 'tik tok', 'python', 'caneta', 'musica', 'love', 'harry potter')
for c in palavras:
  for letra in c:
   if letra in 'aeiou':
       print('na palavra {} nos temos {}'.format(c, letra))
