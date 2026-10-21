#porneste de la o imagine care are deja Python instalat
FROM python:3.12-alpine

#creeaza si intra in folderul app din container
#aici sta proiectul meu cu bossul
WORKDIR /app

#copiaza doar atat mai intai ca sa stie ce librarii trebui instalate
COPY requirements.txt .

#instaleaza Flask
RUN pip install --no-cache-dir -r requirements.txt

#copiaza restul in container
COPY . .

#aplicatia foloseste fix acest port
EXPOSE 5000

#da comanda din linux care ruleaza aplicatia
CMD ["python3", "server.py"]