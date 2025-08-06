import pandas as pd
from izlusceni_igralci import preberi_in_izlusci_podatke  # <- to je ključno

def izvozi_v_json(sezona='2022-23'):
    tabela = preberi_in_izlusci_podatke(sezona)
    if tabela is not None:
        json_filename = f'nba_igralci_{sezona.replace("-", "")}.json'
        tabela.to_json(json_filename, orient='records', force_ascii=False, indent=4)
        print(f"JSON datoteka shranjena kot {json_filename}")

if __name__ == '__main__':
    izvozi_v_json()

