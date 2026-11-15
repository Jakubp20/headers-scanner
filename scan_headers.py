import sys
import requests

NAGLOWKI = {
    "Content-Security-Policy": ("ochrona przed XSS", "dodaj np. default-src 'self'"),
    "Strict-Transport-Security": ("wymusza HTTPS", "dodaj max-age=31536000; includeSubDomains"),
    "X-Frame-Options": ("ochrona przed clickjackingiem", "ustaw DENY lub SAMEORIGIN"),
    "X-Content-Type-Options": ("blokuje zgadywanie typu pliku", "ustaw nosniff"),
    "Referrer-Policy": ("ogranicza wyciek adresu strony", "ustaw strict-origin-when-cross-origin"),
    "Permissions-Policy": ("ogranicza dostep do kamery, mikrofonu", "dodaj np. camera=(), microphone=()"),
}

if len(sys.argv) != 2:
    print("Uzycie: python scan_headers.py <adres>")
    print("Przyklad: python scan_headers.py https://example.com")
    sys.exit(1)

url = sys.argv[1]

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    odpowiedz = requests.get(url, timeout=10)
except requests.exceptions.RequestException as blad:
    print("Nie udalo sie polaczyc z", url)
    print("Powod:", blad)
    sys.exit(1)

print("Skan:", url)
print("Kod odpowiedzi:", odpowiedz.status_code)
print()

obecne = 0
brakujace = []

for nazwa, (opis, naprawa) in NAGLOWKI.items():
    if nazwa in odpowiedz.headers:
        print("[OK]  ", nazwa)
        obecne = obecne + 1
    else:
        print("[BRAK]", nazwa)
        brakujace.append(nazwa)

procent = round(obecne / len(NAGLOWKI) * 100)

if procent >= 80:
    ocena = "A"
elif procent >= 50:
    ocena = "B"
elif procent >= 25:
    ocena = "C"
else:
    ocena = "D"

print()
print("Wynik:", obecne, "z", len(NAGLOWKI), "(", procent, "% )  Ocena:", ocena)

if brakujace:
    print()
    print("Rekomendacje:")
    for nazwa in brakujace:
        opis, naprawa = NAGLOWKI[nazwa]
        print(" -", nazwa, ":", opis)
        print("   Naprawa:", naprawa)