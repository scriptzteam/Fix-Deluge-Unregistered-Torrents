# Fix-Deluge-Unregistered-Torrents

```
pip3 install deluge-client

cat ~/.config/deluge/auth

Replace in check-deluge-errors.py the HASHPASSWORD from the "~/.config/deluge/auth" file

In deluge web interface enable plugins -> execute

In plugin execute -> Add -> Event -> Torrrent added
                            Command -> /path/to/check-deluge-errors.py
```
