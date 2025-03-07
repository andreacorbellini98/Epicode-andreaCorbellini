import requests
import json

def send_request():
    print("\n--- HTTP Request Tester ---")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")

    choice = input("Seleziona il tipo di richiesta (1-4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Scelta non valida. Riprova.")
        return

    url = input("Inserisci l'URL: ").strip()

    data = None
    if choice in ['2', '3']:  # POST e PUT richiedono i dati
        raw_data = input("Inserisci i dati (in formato JSON, es. {\"chiave\": \"valore\"}): ")
        try:
            data = json.loads(raw_data)  # Conversione sicura da JSON
        except json.JSONDecodeError:
            print("Formato dati non valido. Devono essere in formato JSON valido.")
            return

    try:
            # Mappiamo le richieste HTTP a funzioni corrispondenti
        http_methods = {
            '1': requests.get,
            '2': requests.post,
            '3': requests.put,
            '4': requests.delete
            }

        method = http_methods[choice]
        if data:  # Invia dati solo per POST e PUT
            response = method(url, json=data)
        else:
            response = method(url)

        print("\n--- Risposta dal server ---")
        print(f"Status Code: {response.status_code}")
        print("Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")
        print("\nBody:")
        print(response.text)

    except requests.exceptions.MissingSchema:
        print("Errore: L'URL non è valido. Assicurati di includere 'http://' o 'https://'.")
    except requests.exceptions.ConnectionError:
        print("Errore: Non è stato possibile connettersi al server. Controlla l'URL.")
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta: {e}")
      
if __name__ == "__main__":
    while True:
        send_request()
        another = input("\nVuoi inviare un'altra richiesta? (s/n): ").strip().lower()
        if another != 's':
            print("Programma terminato.")
            break