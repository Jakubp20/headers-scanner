# headers-scanner
# Security Headers Scanner

Narzędzie konsolowe w Pythonie, które sprawdza, czy strona ustawia
najważniejsze nagłówki bezpieczeństwa HTTP. Wystawia ocenę (A–D)
i podpowiada, jak naprawić braki.

## Co sprawdza

| Nagłówek | Przed czym chroni |
|----------|-------------------|
| Content-Security-Policy | XSS |
| Strict-Transport-Security | wymusza HTTPS |
| X-Frame-Options | clickjacking |
| X-Content-Type-Options | zgadywanie typu pliku |
| Referrer-Policy | wyciek adresu strony |
| Permissions-Policy | dostęp do kamery, mikrofonu |

## Użycie

    pip install requests
    python scan_headers.py https://example.com

## Przykładowe wyniki

Strona dobrze zabezpieczona (github.com):

![github](wynik-github.png)

Strona bez zabezpieczeń (example.com):

![example](wynik-example.png)

## Jak działa

Skrypt wysyła żądanie GET, odczytuje nagłówki odpowiedzi i porównuje je
z listą zalecanych nagłówków. Liczy wynik procentowy i wypisuje
rekomendacje dla brakujących pozycji.
