from datetime import datetime


class LogAktivitas:
    def __init__(self, path_file=None):        
        self._path_file = path_file
        self.daftar_log = []
        if path_file:
            try:
                with open(path_file, "r", encoding="utf-8") as f:
                    self.daftar_log = [baris.rstrip("\n") for baris in f]
            except FileNotFoundError:
                pass  

    def catat(self, pesan):
        waktu = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")
        baris = f"[{waktu}] {pesan}"            
        self.daftar_log.append(baris)
        if self._path_file:                    
            with open(self._path_file, "a", encoding="utf-8") as f:
                f.write(baris + "\n")