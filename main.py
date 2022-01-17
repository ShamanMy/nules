tekst=input("Ievadiet tekstu:")
def replaceTwos(tekst):
  if tekst.count("2")>0:
    tekst=tekst.replace("2","divi")
    print (tekst)
  else:
    tekst = "Nekas netika aizvetots"
    print(tekst)
  return tekst
replaceDivi(tekst)
