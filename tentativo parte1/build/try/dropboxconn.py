from pathlib import Path
import os

try:
    import dropbox
    import dropbox.files
    DROPBOX_AVAILABLE = True
except ImportError:
    dropbox = None
    DROPBOX_AVAILABLE = False


class DropConn:
    def __init__(self, image_transfer=None, user=None):
        self.image_transfer = image_transfer
        self.user = user
        self.dbx = None
        self.is_offline = True

        token_candidates = [
            Path("token.txt"),
            Path(__file__).resolve().parent.parent.parent / "token.txt",
            Path(__file__).resolve().parent / "token.txt"
        ]
        token = ""
        for tc in token_candidates:
            if tc.exists():
                try:
                    token = tc.read_text(encoding="utf-8").strip()
                    break
                except Exception:
                    pass

        if DROPBOX_AVAILABLE and token:
            try:
                self.dbx = dropbox.Dropbox(token)
                self.is_offline = False
            except Exception as e:
                print(f"[Dropbox Adapter] Connection notice: {e}. Running in local mock mode.")

    def upload_image(self):
        if not self.dbx or not self.image_transfer:
            print("[Dropbox Adapter] Upload skipped (offline mode).")
            return
        try:
            with open(self.image_transfer, 'rb') as f:
                data = f.read()
                self.dbx.files_upload(data, f'/{self.user}_image.png')
                self.dbx.close()
        except Exception as e:
            print(f"[Dropbox Adapter] Upload failed: {e}")

    def download_image(self):
        if not self.dbx:
            print("[Dropbox Adapter] Download skipped (offline mode).")
            return
        try:
            local_dir = Path(__file__).resolve().parent.parent.parent / "local_temp_files"
            local_dir.mkdir(parents=True, exist_ok=True)
            for entry in self.dbx.files_list_folder('').entries:
                self.dbx.files_download_to_file(str(local_dir / entry.name), f'/{entry.name}')
                self.dbx.close()
        except Exception as e:
            print(f"[Dropbox Adapter] Download failed: {e}")

    def downlaod_onlyimage(self, name_file=None):
        if not self.dbx:
            print("[Dropbox Adapter] Image download skipped (offline mode).")
            return
        try:
            local_file_path = Path(__file__).resolve().parent.parent.parent / "local_downloaded_image.png"
            dropbox_file_path = f'/{name_file}.png'
            with open(local_file_path, 'wb') as local_file:
                metadata, res = self.dbx.files_download(dropbox_file_path)
                local_file.write(res.content)
            self.dbx.close()
        except Exception as e:
            print(f"[Dropbox Adapter] Image download failed: {e}")
