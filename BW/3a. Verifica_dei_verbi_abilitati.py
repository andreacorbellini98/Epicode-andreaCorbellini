import requests

def check_all_http_methods():
    print("\n--- Verifica di tutti i metodi HTTP abilitati e non abilitati ---")
    url = input("Inserisci l'URL (es. https://example.com): ").strip()

    # Lista di metodi HTTP comuni
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH', 'HEAD']
    results = {}

    for method in methods:
        try:
            # Invia una richiesta con il metodo specifico
            response = requests.request(method, url)

            # Se il metodo è supportato, aggiungi il codice di stato
            if response.status_code != 405:  # 405 significa "Method Not Allowed"
                results[method] = f"Abilitato (Status Code: {response.status_code})"
            else:
                results[method] = "Non abilitato (405 Method Not Allowed)"
        except requests.exceptions.RequestException as e:
            results[method] = f"Errore durante la richiesta: {e}"

    # Stampa i risultati
    print("\n--- Risultati ---")
    for method, status in results.items():
        print(f"{method}: {status}")

    # Dettagli aggiuntivi: prova a ottenere metodi supportati tramite OPTIONS
    try:
        print("\n--- Tentativo con OPTIONS per recuperare i metodi supportati ---")
        response_options = requests.options(url)
        if "Allow" in response_options.headers:
            allowed_methods = response_options.headers["Allow"]
            print("Metodi dichiarati dal server nell'header 'Allow':")
            for method in allowed_methods.split(","):
                print(f"- {method.strip()}")
        else:
            print("Il server non ha restituito l'header 'Allow'.")
    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta OPTIONS: {e}")

if __name__ == "__main__":
    while True:
        check_all_http_methods()
        another = input("\nVuoi verificare un altro URL? (s/n): ").strip().lower()
        if another != 's':
            print("Programma terminato.")
            break
