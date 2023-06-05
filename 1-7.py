from bs4 import BeautifulSoup
with open("file.html") as file:
    r=file.read()
soup=BeautifulSoup(r,"lxml")
p=soup.find_all("p")
con=len(p)
Fir_p=soup.find("p")
Len_p=Fir_p.text
P_con=len(Len_p)
A=soup.find("a")
Href=soup.find("a")["href"]
print(soup.find_all("title"))
print(p)
print(con)
print(Fir_p)
print(P_con)
print(A)
print(Href)

