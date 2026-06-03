#!/usr/bin/env bash
iso_name="jarvis-os"
iso_label="JARVIS_OS_$(date +%Y%m)"
iso_publisher="JARVIS OS"
iso_application="JARVIS OS Live/Installation Environment"
iso_version="2.0.0"
install_dir="arch"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito' 'uefi-ia32.systemd-boot.esp' 'uefi-x64.systemd-boot.esp' 'uefi-ia32.systemd-boot.eltorito' 'uefi-x64.systemd-boot.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86')
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
  ["/root"]="0:0:750"
  ["/root/.automated_script.sh"]="0:0:755"
  ["/opt/jarvis"]="1000:1000:755"
  ["/usr/lib/jarvis/jarvis-hal"]="0:0:755"
)
