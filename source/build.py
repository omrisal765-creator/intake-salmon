import os, sys
B=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(B,'src.html'),encoding='utf8').read()
logo=open(os.path.join(B,'logo.datauri')).read().strip()
HEAD='<!doctype html>\n<html lang="he" dir="rtl">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<style>body{margin:0}</style>\n</head>\n<body>\n'
TAIL='\n</body>\n</html>\n'
out=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(B)
for mode,title,h1,path in [('intake','שאלון הקבלה של ד״ר שלמון','שאלון קבלה ומיפוי התפתחותי','index.html'),
                           ('contract','חוזה טיפולי של ד״ר שלמון','חוזה טיפולי וויתור סודיות','contract/index.html')]:
  b=src.replace("'__MODE__'","'%s'"%mode).replace('__TITLE__',title).replace('__H1__',h1).replace('__LOGO__',logo)
  assert '__' not in ''.join(t for t in ['__MODE__','__TITLE__','__H1__','__LOGO__'] if t in b) 
  fp=os.path.join(out,path); os.makedirs(os.path.dirname(fp),exist_ok=True)
  open(fp,'w',encoding='utf8').write(HEAD+b+TAIL); print('wrote',fp,len(b))
