# Testy Automatyczne Lab 2

## Opis Repo

Projekt zawiera scenariusze testowe napisane przy użyciu biblioteki Selenium w Pythonie.



# 1. Test Scenariusza Sklepu Wina-Bachus.pl z wykorzystaniem przegladarki Edge

## Przegląd

### Kroki wstępne
1. Otwórz przeglądarkę Edge.
2. Przejdź na stronę [Wina Bachus](https://www.wina-bachus.pl).
3. Akceptuj komunikat o wieku 18 lat, jeśli widoczny.
4. Ustaw ciasteczko za pomocą JavaScript.

### Akcje użytkownika
5. Potwierdź pliki cookies, jeśli widoczne.
6. Kliknij przycisk wyszukiwarki.
7. Wpisz wyszukiwany przez ciebie produkt np. "PINTIA Vega Sicilia" w pole wyszukiwania.
8. Zatwierdź wyszukiwanie klikając w lupke.

### Dodatkowa Weryfikacja
9. Ponownie zamknij komunikat wiekowy na nowej stronie, jeśli widoczny.

### Kliknięcie w Produkt
10. Kliknij w wybrany produkt na nowej stronie.

### Zakończenie Testu
11. Oczekuj przed zamknięciem przeglądarki.





# 2. Test Scenariusza Wyszukiwania w Google w przegladarce Chrome

## Przegląd

### Kroki wstępne
1. Otwórz przeglądarkę Chrome.
2. Przejdź na stronę [Google](https://www.google.pl).
3. Akceptuj pliki cookies, jeśli widoczne.

### Akcje użytkownika
4. Wpisz "Selenium Tutorial" w pole wyszukiwania.
5. Naciśnij Enter.

### Weryfikacja
6. Sprawdź, czy wyniki zawierają oczekiwane słowo kluczowe "Selenium".

### Zakończenie Testu
7. Oczekuj przed zamknięciem przeglądarki.