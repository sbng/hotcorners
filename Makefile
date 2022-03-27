#
# Makefile
# sbng, 2022-03-27 22:25
#

install:
	@echo "[INFO] copy python script to ~/.local/bin/"
	cp ./mouse.py ~/.local/bin/
	@echo "[INFO] copy systemd startup file to user directory"
	cp hotcorner.service ~/.config/systemd/user/
	@echo "[INFO] Starting hot corner service"
	systemctl --user daemon-reload
	systemctl --user restart hotcorner.service
	systemctl --user status hotcorner.service 

# vim:ft=make
#
