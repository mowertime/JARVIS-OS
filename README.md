[william@LServer3 JARVIS-OS]$ sudo bash distribution/installer/build-iso.sh
JARVIS OS v2.0.0 ISO Builder
[*] Preparing build directory...
[*] Copying backend code...
[*] Copying frontend code...
[*] Copying shared modules...
[*] Copying systemd services...
[*] Copying HAL and managers...
[*] Creating JARVIS config...
[*] Copying ISO profile...

========================================
  Building JARVIS OS ISO...
========================================

[mkarchiso] INFO: Validating options...
[mkarchiso] INFO: 'edk2-shell' is not in the package list. The ISO will not contain a bootable UEFI shell.
[mkarchiso] INFO: Validating 'uefi.systemd-boot': 'memtest86+-efi' is not in the package list. Memory testing will not be available from the UEFI boot loader.
[mkarchiso] INFO: Done!
[mkarchiso] INFO: mkarchiso configuration settings
[mkarchiso] INFO:              Architecture:   x86_64
[mkarchiso] INFO:         Working directory:   /tmp/jarvis-iso-build-14460
[mkarchiso] INFO:    Installation directory:   arch
[mkarchiso] INFO:                Build date:   2026-06-03T17:34-0500
[mkarchiso] INFO:          Output directory:   /home/william/JARVIS-OS/dist
[mkarchiso] INFO:        Current build mode:   iso
[mkarchiso] INFO:               Build modes:   iso
[mkarchiso] INFO:                   GPG key:   None
[mkarchiso] INFO:                GPG signer:   None
[mkarchiso] INFO: Code signing certificates:   None
[mkarchiso] INFO:                   Profile:   /tmp/jarvis-iso-build-14460
[mkarchiso] INFO: Pacman configuration file:   /tmp/jarvis-iso-build-14460/pacman.conf
[mkarchiso] INFO:           Image file name:   jarvis-os-2.0.0-x86_64.iso
[mkarchiso] INFO:          ISO volume label:   JARVIS_OS_202606
[mkarchiso] INFO:             ISO publisher:   JARVIS OS
[mkarchiso] INFO:           ISO application:   JARVIS OS Live/Installation Environment
[mkarchiso] INFO:                Boot modes:   bios.syslinux uefi.systemd-boot
[mkarchiso] INFO:             Packages File:   /tmp/jarvis-iso-build-14460/packages.x86_64
[mkarchiso] INFO:                  Packages:   acl arch-install-scripts base bash btrfs-progs busybox coreutils cpio cryptsetup dmraid dosfstools e2fsprogs efibootmgr elinks exfatprogs f2fs-tools fdisk gawk gcc-libs gettext glibc gpgme gptfdisk grep grub gzip inetutils iproute2 iputils jfsutils less linux-lts logrotate lvm2 man-db man-pages mdadm memtest86+ nano ncurses netctl networkmanager nfs-utils nilfs-utils ntfs-3g openssh pacman pacman-contrib parted pciutils ppl procps-ng psmisc reiserfsprogs rsync sed shadow s-nail sysfsutils syslinux systemd systemd-resolvconf tar texinfo usbutils util-linux vim which xfsprogs xorg xorg-xinit zstd dhcpcd dnsmasq iwd wpa_supplicant wireless_tools python python-pip python-virtualenv python-setuptools python-wheel alsa-utils pulseaudio espeak fwupd dmidecode hwinfo lshw docker docker-compose git curl wget
[mkarchiso] INFO: Copying custom pacman.conf to work directory...
[mkarchiso] INFO: Using pacman CacheDir: /var/cache/pacman/pkg/ 
[mkarchiso] INFO: Copying custom airootfs files...
[mkarchiso] WARNING: Cannot change permissions of '/tmp/jarvis-iso-build-14460/x86_64/airootfs/root/.automated_script.sh'. The file or directory does not exist.
[mkarchiso] WARNING: Cannot change permissions of '/tmp/jarvis-iso-build-14460/x86_64/airootfs/etc/shadow'. The file or directory does not exist.
[mkarchiso] WARNING: Cannot change permissions of '/tmp/jarvis-iso-build-14460/x86_64/airootfs/etc/gshadow'. The file or directory does not exist.
[mkarchiso] INFO: Done!
[mkarchiso] INFO: Installing packages to '/tmp/jarvis-iso-build-14460/x86_64/airootfs/'...
==> Creating install root at /tmp/jarvis-iso-build-14460/x86_64/airootfs
==> Installing packages to /tmp/jarvis-iso-build-14460/x86_64/airootfs
:: Synchronizing package databases...
 core                                     125.8 KiB   187 KiB/s 00:01 [######################################] 100%
 extra                                      8.2 MiB  1363 KiB/s 00:06 [######################################] 100%
 community.db failed to download
 multilib                                 128.1 KiB   174 KiB/s 00:01 [######################################] 100%
error: failed retrieving file 'community.db' from losangeles.mirror.pkgbuild.com : The requested URL returned error: 404
error: failed retrieving file 'community.db' from us.arch.niranjan.co : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirror.givebytes.net : The requested URL returned error: 404
error: failed retrieving file 'community.db' from arch.mirror.constant.com : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirror2.givebytes.net : The requested URL returned error: 404
error: failed retrieving file 'community.db' from zxcvfdsa.com : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirror.akane.network : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirrors.lug.mtu.edu : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirrors.logal.dev : The requested URL returned error: 404
error: failed retrieving file 'community.db' from iad.mirrors.misaka.one : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirrors.rit.edu : The requested URL returned error: 404
error: failed retrieving file 'community.db' from repo.ialab.dsu.edu : The requested URL returned error: 404
error: failed retrieving file 'community.db' from arch.hu.fo : Connection timed out after 10002 milliseconds
error: failed retrieving file 'community.db' from mirror.adectra.com : The requested URL returned error: 404
error: failed retrieving file 'community.db' from arch.mirror.marcusspencer.us:4443 : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirror.theash.xyz : The requested URL returned error: 404
error: failed retrieving file 'community.db' from us.mirrors.cicku.me : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirror.tzulo.com : The requested URL returned error: 404
error: failed retrieving file 'community.db' from plug-mirror.rcac.purdue.edu : The requested URL returned error: 404
error: failed retrieving file 'community.db' from mirror.zackmyers.io : The requested URL returned error: 404
error: failed to synchronize all databases (failed to retrieve some files)
==> ERROR: Failed to install packages to new root
[william@LServer3 JARVIS-OS]$ 
