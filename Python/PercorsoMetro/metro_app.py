import tkinter as tk
from tkinter import ttk, messagebox
from metro_lines import metro_lines_milano, metro_lines_roma
from metro_map import find_shortest_path, calculate_stops


class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Finder")

        self.metro_choice = tk.StringVar(value='Milano')  # Default choice is Milano

        # Frame per selezionare la metro
        selection_frame = ttk.LabelFrame(self.root, text="Seleziona Metropolitana")
        selection_frame.pack(padx=10, pady=10, fill="x")

        ttk.Radiobutton(selection_frame, text="Milano", variable=self.metro_choice, value="Milano",
                        command=self.update_stations).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(selection_frame, text="Roma", variable=self.metro_choice, value="Roma",
                        command=self.update_stations).pack(side=tk.LEFT, padx=5)

        # Frame per le stazioni e i risultati
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        ttk.Label(main_frame, text="Stazione di partenza:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.start_station = ttk.Combobox(main_frame, values=[], width=30)
        self.start_station.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Stazione di arrivo:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.end_station = ttk.Combobox(main_frame, values=[], width=30)
        self.end_station.grid(row=1, column=1, padx=5, pady=5)

        self.calculate_button = ttk.Button(main_frame, text="Calcola Percorso", command=self.calculate_route)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(main_frame, wrap=tk.WORD, width=50, height=15, font=("Arial", 12))
        self.result_text.grid(row=3, column=0, columnspan=2, pady=10)

        self.metro_lines = metro_lines_milano  # Imposta la metro di Milano come predefinita
        self.update_stations()

    def update_stations(self):
        #Aggiorna la lista delle stazioni in base alla selezione
        if self.metro_choice.get() == "Milano":
            self.metro_lines = metro_lines_milano
        else:
            self.metro_lines = metro_lines_roma

        all_stations = sorted(set(station for line in self.metro_lines.values() for station in line))
        self.start_station['values'] = all_stations
        self.end_station['values'] = all_stations

    def calculate_route(self):
        start = self.start_station.get()
        end = self.end_station.get()

        if not start or not end:
            messagebox.showerror("Errore", "Per favore, seleziona sia la stazione di partenza che quella di arrivo.")
            return

        path = find_shortest_path(start, end, self.metro_lines)

        if path:
            total_stops, line_stops, changes = calculate_stops(path)
            result = f"Percorso più breve da {start} a {end}:\n"
            result += " -> ".join(path) + f"\n\nNumero totale di fermate: {total_stops}\n"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        else:
            messagebox.showerror("Errore", "Non è stato possibile trovare un percorso tra le fermate specificate.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()