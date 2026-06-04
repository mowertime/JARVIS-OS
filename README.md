[william@LServer3 JARVIS-OS]$ sudo bash distribution/installer/build-iso.sh
[sudo] password for william: 
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
[mkarchiso] INFO:         Working directory:   /tmp/jarvis-iso-build-69948
[mkarchiso] INFO:    Installation directory:   arch
[mkarchiso] INFO:                Build date:   2026-06-04T14:20-0500
[mkarchiso] INFO:          Output directory:   /home/william/.local/share/Trash/files/JARVIS-OS.2/dist
[mkarchiso] INFO:        Current build mode:   iso
[mkarchiso] INFO:               Build modes:   iso
[mkarchiso] INFO:                   GPG key:   None
[mkarchiso] INFO:                GPG signer:   None
[mkarchiso] INFO: Code signing certificates:   None
[mkarchiso] INFO:                   Profile:   /tmp/jarvis-iso-build-69948
[mkarchiso] INFO: Pacman configuration file:   /tmp/jarvis-iso-build-69948/pacman.conf
[mkarchiso] INFO:           Image file name:   jarvis-os-2.0.0-x86_64.iso
[mkarchiso] INFO:          ISO volume label:   JARVIS_OS_202606
[mkarchiso] INFO:             ISO publisher:   JARVIS OS
[mkarchiso] INFO:           ISO application:   JARVIS OS Live/Installation Environment
[mkarchiso] INFO:                Boot modes:   bios.syslinux uefi.systemd-boot
[mkarchiso] INFO:             Packages File:   /tmp/jarvis-iso-build-69948/packages.x86_64
[mkarchiso] INFO:                  Packages:   acl arch-install-scripts base bash btrfs-progs busybox coreutils cpio cryptsetup dmraid dosfstools e2fsprogs efibootmgr elinks exfatprogs f2fs-tools gawk gcc-libs gettext glibc gpgme gptfdisk grep grub gzip inetutils iproute2 iputils jfsutils less linux-lts logrotate lvm2 man-db man-pages mdadm memtest86+ nano ncurses netctl networkmanager nfs-utils nilfs-utils ntfs-3g openssh pacman pacman-contrib parted pciutils ppl procps-ng psmisc rsync sed shadow s-nail sysfsutils syslinux systemd systemd-resolvconf tar texinfo usbutils util-linux vim which xfsprogs xorg xorg-xinit zstd dhcpcd dnsmasq iwd wpa_supplicant wireless_tools python python-pip python-virtualenv python-setuptools python-wheel alsa-utils pulseaudio espeak-ng fwupd dmidecode hwinfo lshw docker docker-compose git curl wget
[mkarchiso] INFO: Copying custom pacman.conf to work directory...
[mkarchiso] INFO: Using pacman CacheDir: /var/cache/pacman/pkg/ 
[mkarchiso] INFO: Copying custom airootfs files...
[mkarchiso] INFO: Done!
[mkarchiso] INFO: Installing packages to '/tmp/jarvis-iso-build-69948/x86_64/airootfs/'...
==> Creating install root at /tmp/jarvis-iso-build-69948/x86_64/airootfs
==> Installing packages to /tmp/jarvis-iso-build-69948/x86_64/airootfs
:: Synchronizing package databases...
 core                                     125.8 KiB   128 KiB/s 00:01 [######################################] 100%
 extra                                   1792.0 KiB  1259 KiB/s 00:05 [#######-------------------------------]  21%
 extra                                      8.2 MiB  1572 KiB/s 00:05 [######################################] 100%
:: There are 49 members in group xorg:
:: Repository extra
   1) xf86-video-vesa  2) xorg-bdftopcf  3) xorg-docs  4) xorg-font-util  5) xorg-fonts-100dpi
   6) xorg-fonts-75dpi  7) xorg-fonts-encodings  8) xorg-iceauth  9) xorg-mkfontscale  10) xorg-server
   11) xorg-server-common  12) xorg-server-devel  13) xorg-server-src  14) xorg-server-xephyr
   15) xorg-server-xnest  16) xorg-server-xvfb  17) xorg-sessreg  18) xorg-setxkbmap  19) xorg-smproxy
   20) xorg-x11perf  21) xorg-xauth  22) xorg-xbacklight  23) xorg-xcmsdb  24) xorg-xcursorgen  25) xorg-xdpyinfo
   26) xorg-xdriinfo  27) xorg-xev  28) xorg-xgamma  29) xorg-xhost  30) xorg-xinput  31) xorg-xkbcomp
   32) xorg-xkbevd  33) xorg-xkbutils  34) xorg-xkill  35) xorg-xlsatoms  36) xorg-xlsclients  37) xorg-xmodmap
   38) xorg-xpr  39) xorg-xprop  40) xorg-xrandr  41) xorg-xrdb  42) xorg-xrefresh  43) xorg-xset
   44) xorg-xsetroot  45) xorg-xvinfo  46) xorg-xwayland  47) xorg-xwd  48) xorg-xwininfo  49) xorg-xwud

Enter a selection (default=all): 
resolving dependencies...
:: There are 2 providers available for libxtables.so=12-64:
:: Repository core
   1) iptables  2) iptables-legacy

Enter a number (default=1): 
:: There are 3 providers available for initramfs:
:: Repository core
   1) mkinitcpio
:: Repository extra
   2) booster  3) dracut

Enter a number (default=1): 
looking for conflicting packages...

Package (464)                         New Version                 Net Change  Download Size

extra/abseil-cpp                      20260107.1-1                  6.71 MiB               
extra/alsa-lib                        1.2.16-1                      1.75 MiB               
extra/alsa-topology-conf              1.2.5.1-4                     0.33 MiB               
extra/alsa-ucm-conf                   1.2.16-1                      0.67 MiB               
core/archlinux-keyring                20260420-1                    1.72 MiB               
core/attr                             2.5.2-2                       0.21 MiB               
core/audit                            4.1.4-2                       1.01 MiB               
extra/avahi                           1:0.9rc4-1                    2.00 MiB               
core/binutils                         2.46+r70+g155188ea10a7-1     44.00 MiB               
extra/bluez                           5.86-6                        1.62 MiB               
core/brotli                           1.2.0-1                       1.03 MiB               
core/bzip2                            1.0.8-6                       0.14 MiB               
core/ca-certificates                  20240618-1                    0.00 MiB               
core/ca-certificates-mozilla          3.124-1                       0.99 MiB               
core/ca-certificates-utils            20240618-1                    0.01 MiB               
extra/cairo                           1.18.4-1                      1.59 MiB               
extra/confuse                         3.3-5                         0.14 MiB               
extra/containerd                      2.3.1-1                      86.70 MiB               
core/db5.3                            5.3.28-7                      6.48 MiB               
core/dbus                             1.16.2-1                      0.98 MiB               
core/dbus-broker                      37-3                          0.35 MiB               
core/dbus-broker-units                37-3                          0.00 MiB               
core/dbus-units                       37-3                          0.00 MiB               
extra/dconf                           0.49.0-1                      0.45 MiB               
extra/default-cursors                 3-1                           0.00 MiB               
core/device-mapper                    2.03.41-1                     0.81 MiB               
core/diffutils                        3.12-2                        1.50 MiB               
core/ding-libs                        0.7.0-1                       0.28 MiB               
extra/duktape                         2.7.0-7                       0.78 MiB               
core/efivar                           39-2                          0.53 MiB               
extra/ell                             0.83-1                        0.65 MiB               
core/expat                            2.8.1-1                       0.48 MiB               
extra/fftw                            3.3.11-1                      8.83 MiB               
core/file                             5.47-3                       10.39 MiB               
core/filesystem                       2025.10.12-1                  0.02 MiB               
core/findutils                        4.10.0-3                      1.74 MiB               
extra/flac                            1.5.0-1                       1.14 MiB               
extra/flashrom                        1.7.0-1                       8.00 MiB               
extra/fontconfig                      2:2.18.1-1                    1.20 MiB               
extra/freetype2                       2.14.3-1                      1.66 MiB               
extra/fribidi                         1.0.16-2                      0.24 MiB               
extra/fuse-common                     3.18.2-1                      0.00 MiB               
extra/fuse2                           2.9.9-5                       0.44 MiB               
extra/fwupd-efi                       1.8-2                         0.07 MiB               
core/gdbm                             1.26-2                        0.72 MiB               
extra/glib-networking                 1:2.80.1-1                    0.65 MiB               
core/glib2                            2.88.1-1                     37.96 MiB               
extra/glpk                            5.0-3                         1.67 MiB               
core/gmp                              6.3.0-3                       1.01 MiB               
core/gnulib-l10n                      20241231-1                    0.61 MiB               
core/gnupg                            2.4.9-1                      10.28 MiB               
core/gnutls                           3.8.13-2                      8.11 MiB               
core/gpm                              1.20.7.r38.ge82d1a6-6         0.38 MiB               
extra/graphite                        1:1.3.15-1                    0.20 MiB       0.08 MiB
core/groff                            1.24.1-1                      9.01 MiB               
extra/gsettings-system-schemas        50.1-1                        0.02 MiB               
core/gssproxy                         0.9.2-3                       0.24 MiB               
extra/gtest                           1.17.0-2                      1.63 MiB               
extra/harfbuzz                        14.2.1-1                      4.77 MiB               
extra/hicolor-icon-theme              0.18-1                        0.05 MiB               
core/hwdata                           0.407-1                       9.89 MiB               
core/iana-etc                         20260530-1                    4.02 MiB               
core/icu                              78.3-1                       43.23 MiB               
core/iptables                         1:1.8.13-1                    2.35 MiB               
core/jansson                          2.15.0-1                      0.27 MiB               
core/json-c                           0.18-2                        0.18 MiB               
extra/json-glib                       1.10.8-1                      1.01 MiB               
core/kbd                              2.10.0-1                      3.29 MiB       1.28 MiB
core/keyutils                         1.6.3-4                       0.20 MiB               
core/kmod                             34.2-1                        0.33 MiB               
core/krb5                             1.22.2-1                      4.72 MiB               
extra/lame                            3.101.r6531-1                 1.09 MiB               
core/leancrypto                       1.7.2-1                       6.19 MiB               
core/libaio                           0.3.113-4                     0.04 MiB               
core/libarchive                       3.8.7-1                       1.23 MiB               
core/libasan                          16.1.1+r12+g301eb08fa2c5-1    1.88 MiB               
core/libassuan                        3.0.0-1                       0.23 MiB               
extra/libasyncns                      1:0.8+r3+g68cd5af-3           0.05 MiB               
core/libatomic                        16.1.1+r12+g301eb08fa2c5-1    0.04 MiB               
core/libbpf                           1.7.0-1                       0.82 MiB               
core/libcap                           2.78-1                        2.08 MiB               
core/libcap-ng                        0.9.3-1                       0.16 MiB               
extra/libcbor                         0.14.0-1                      0.18 MiB               
extra/libcss                          0.9.2-2                       0.60 MiB               
extra/libdaemon                       0.14-6                        0.06 MiB               
extra/libdatrie                       0.2.14-1                      0.49 MiB               
extra/libdecor                        0.2.5-1                       0.16 MiB               
extra/libdom                          0.4.2-2                       0.58 MiB               
extra/libdrm                          2.4.134-1                     1.28 MiB               
core/libedit                          20260512_3.1-1                0.27 MiB               
extra/libei                           1.6.0-1                       0.42 MiB               
core/libelf                           0.195-1                       3.23 MiB               
extra/libepoxy                        1.5.10-3                      2.64 MiB               
extra/libevdev                        1.13.6-1                      0.21 MiB               
core/libevent                         2.1.12-5                      1.12 MiB               
core/libffi                           3.5.2-1                       0.10 MiB               
extra/libfontenc                      1.1.9-1                       0.03 MiB               
extra/libftdi                         1.5-10                        0.51 MiB               
core/libgcc                           16.1.1+r12+g301eb08fa2c5-1    0.18 MiB               
core/libgcrypt                        1.12.2-1                      1.93 MiB               
core/libgfortran                      16.1.1+r12+g301eb08fa2c5-1    3.53 MiB               
extra/libglvnd                        1.7.0-3                       3.34 MiB               
core/libgomp                          16.1.1+r12+g301eb08fa2c5-1    0.43 MiB               
core/libgpg-error                     1.61-1                        1.14 MiB               
extra/libgudev                        238-3                         0.38 MiB               
extra/libhubbub                       0.3.8-2                       0.35 MiB               
extra/libice                          1.1.2-1                       0.36 MiB               
core/libidn2                          2.3.8-1                       0.37 MiB               
core/libinih                          62-2                          0.06 MiB               
extra/libinput                        1.31.3-1                      0.79 MiB       0.22 MiB
extra/libjcat                         0.2.6-1                       0.55 MiB               
core/libksba                          1.8.0-1                       0.34 MiB               
core/libldap                          2.6.13-1                      0.66 MiB               
core/liblsan                          16.1.1+r12+g301eb08fa2c5-1    0.55 MiB               
core/libmakepkg-dropins               20-1                          0.01 MiB               
extra/libmbim                         1.34.0-1                      3.62 MiB               
extra/libmm-glib                      1.24.2-1                      7.42 MiB               
core/libmnl                           1.0.5-2                       0.03 MiB               
extra/libndp                          1.9-1                         0.06 MiB               
core/libnetfilter_conntrack           1.1.1-1                       0.16 MiB               
extra/libnewt                         0.52.25-2                     0.28 MiB               
core/libnfnetlink                     1.0.2-2                       0.05 MiB               
core/libnftnl                         1.3.1-1                       0.25 MiB               
core/libnghttp2                       1.69.0-1                      0.39 MiB               
core/libnghttp3                       1.16.0-1                      0.27 MiB               
core/libngtcp2                        1.23.0-1                      0.74 MiB               
core/libnl                            3.12.0-1                      2.12 MiB               
extra/libnm                           1.56.1-1                      6.39 MiB               
core/libnsl                           2.0.1-2                       0.07 MiB               
extra/libntfs-3g                      2026.2.25-1                   0.60 MiB               
core/libobjc                          16.1.1+r12+g301eb08fa2c5-1    0.09 MiB               
extra/libogg                          1.3.6-1                       0.44 MiB               
core/libp11-kit                       0.26.2-1                      3.21 MiB               
extra/libparserutils                  0.2.5-2                       0.10 MiB               
core/libpcap                          1.10.6-1                      0.65 MiB               
extra/libpciaccess                    0.19-1                        0.06 MiB               
extra/libpgm                          5.3.128-4                     0.35 MiB               
core/libpipeline                      1.5.8-1                       0.09 MiB               
extra/libpng                          1.6.58-1                      0.58 MiB               
extra/libproxy                        0.5.12-1                      0.10 MiB               
core/libpsl                           0.21.5-2                      0.22 MiB               
extra/libpulse                        17.0+r98+gb096704c0-1         1.46 MiB               
extra/libqmi                          1.38.0-1                     21.52 MiB               
extra/libqrtr-glib                    1.4.0-1                       0.13 MiB               
core/libquadmath                      16.1.1+r12+g301eb08fa2c5-1    0.30 MiB               
extra/libsamplerate                   0.2.2-3                       1.55 MiB               
core/libsasl                          2.1.28-5                      0.50 MiB               
core/libseccomp                       2.6.0-1                       0.31 MiB               
core/libsecret                        0.21.7-1                      1.16 MiB               
extra/libsm                           1.2.6-1                       0.26 MiB               
extra/libsndfile                      1.2.2-4                       0.93 MiB               
extra/libsodium                       1.0.22-1                      0.64 MiB               
extra/libsonic                        0.2.0-2                       0.04 MiB               
extra/libsoup3                        3.6.6-2                       1.96 MiB               
extra/libsoxr                         0.1.3-4                       0.20 MiB               
core/libssh2                          1.11.1-1                      0.48 MiB               
core/libstdc++                        16.1.1+r12+g301eb08fa2c5-1    2.81 MiB               
extra/libstemmer                      3.1.1-1                       0.64 MiB               
extra/libsysprof-capture              50.0-2                        0.27 MiB               
core/libtasn1                         4.21.0-1                      0.27 MiB               
extra/libteam                         1.32-3                        0.33 MiB               
extra/libthai                         0.1.30-1                      1.24 MiB               
core/libtirpc                         1.3.7-1                       0.42 MiB               
core/libtool                          2.6.0+r23+gb08cb0a0-1         2.34 MiB               
core/libtsan                          16.1.1+r12+g301eb08fa2c5-1    1.45 MiB               
core/libubsan                         16.1.1+r12+g301eb08fa2c5-1    0.50 MiB               
core/libunistring                     1.4.2-1                       2.73 MiB               
extra/libunwind                       1.8.2-1                       0.29 MiB               
extra/liburcu                         0.15.6-1                      0.73 MiB               
core/libusb                           1.0.30-1                      0.23 MiB               
core/libverto                         0.3.2-6                       0.07 MiB               
extra/libvorbis                       1.3.7-4                       0.83 MiB               
extra/libwacom                        2.19.0-1                      1.60 MiB               
extra/libwapcaplet                    0.4.3-4                       0.03 MiB               
extra/libx11                          1.8.13-1                      9.78 MiB               
extra/libx86emu                       3.7-2                         0.16 MiB               
extra/libxau                          1.0.12-1                      0.02 MiB               
extra/libxaw                          1.0.16-2                      1.65 MiB               
extra/libxcb                          1.17.0-1                      3.87 MiB               
extra/libxcomposite                   0.4.7-1                       0.02 MiB               
core/libxcrypt                        4.5.2-1                       0.19 MiB               
extra/libxcursor                      1.2.3-1                       0.07 MiB               
extra/libxcvt                         0.1.3-1                       0.04 MiB               
extra/libxdmcp                        1.1.5-2                       0.13 MiB               
extra/libxext                         1.3.7-1                       0.30 MiB               
extra/libxfixes                       6.0.2-1                       0.04 MiB               
extra/libxfont2                       2.0.7-1                       0.23 MiB               
extra/libxft                          2.3.9-1                       0.13 MiB               
extra/libxi                           1.8.3-1                       0.49 MiB               
extra/libxinerama                     1.1.6-1                       0.02 MiB               
extra/libxkbfile                      1.2.0-1                       0.19 MiB               
core/libxml2                          2.15.3-1                      3.00 MiB               
extra/libxmlb                         0.3.27-1                      1.21 MiB               
extra/libxmu                          1.3.1-1                       0.34 MiB               
extra/libxpm                          3.5.19-1                      0.16 MiB               
extra/libxrandr                       1.5.5-1                       0.07 MiB               
extra/libxrender                      0.9.12-1                      0.09 MiB               
extra/libxshmfence                    1.3.3-1                       0.02 MiB               
extra/libxt                           1.3.1-1                       2.02 MiB               
extra/libxtst                         1.2.5-1                       0.11 MiB               
extra/libxv                           1.0.13-1                      0.06 MiB               
extra/libxxf86vm                      1.1.7-1                       0.03 MiB               
core/licenses                         20240728-1                    1.54 MiB               
core/linux-api-headers                7.0-1                         6.92 MiB       1.50 MiB
extra/llvm-libs                       22.1.6-1                    163.72 MiB               
extra/lm_sensors                      1:3.6.2-1                     0.48 MiB               
extra/lmdb                            0.9.35-1                      0.40 MiB               
extra/lua                             5.5.0-2                       1.57 MiB               
extra/lua54                           5.4.8-6                       1.50 MiB               
core/lz4                              1:1.10.0-2                    0.44 MiB               
core/lzo                              2.10-5                        0.38 MiB               
extra/mesa                            1:26.1.2-1                   52.57 MiB               
core/mkinitcpio                       41-4                          0.21 MiB               
core/mkinitcpio-busybox               1.36.1-1                      0.51 MiB               
extra/mobile-broadband-provider-info  20251101-1                    0.50 MiB               
core/mpdecimal                        4.0.1-3                       0.32 MiB               
core/mpfr                             4.2.2-1                       1.01 MiB               
extra/mpg123                          1.33.5-1                      1.18 MiB               
extra/mtdev                           1.1.7-1                       0.05 MiB               
core/nettle                           4.0-1                         1.03 MiB               
core/nfsidmap                         2.9.1-1                       0.17 MiB               
extra/nftables                        1:1.1.6-3                     1.11 MiB               
core/npth                             1.8-1                         0.08 MiB               
core/nspr                             4.39-1                        0.71 MiB               
core/nss                              3.124-1                       5.24 MiB               
core/openssl                          3.6.2-2                      11.98 MiB               
extra/opus                            1.6.1-1                       4.16 MiB               
extra/orc                             0.4.42-1                      1.36 MiB               
core/p11-kit                          0.26.2-1                      1.10 MiB               
core/pacman-mirrorlist                20260406-1                    0.03 MiB               
core/pam                              1.7.2-2                       2.92 MiB               
core/pambase                          20250719-1                    0.00 MiB               
extra/pango                           1:1.57.1-1                    2.33 MiB               
extra/passim                          0.1.11-1                      0.29 MiB               
extra/pcaudiolib                      1.3-1                         0.02 MiB               
core/pcre                             8.45-4                        3.50 MiB               
core/pcre2                            10.47-1                       7.00 MiB               
extra/pcsclite                        2.5.0-1                       0.31 MiB               
core/perl                             5.42.2-1                     70.11 MiB               
extra/perl-class-inspector            1.36-10                       0.03 MiB               
extra/perl-clone                      0.50-1                        0.03 MiB               
extra/perl-encode-locale              1.05-15                       0.02 MiB               
extra/perl-error                      0.17030-3                     0.04 MiB               
extra/perl-file-listing               6.16-6                        0.02 MiB               
extra/perl-file-sharedir              1.118-8                       0.02 MiB               
extra/perl-html-parser                3.85-1                        0.33 MiB               
extra/perl-html-tagset                3.24-4                        0.02 MiB               
extra/perl-http-cookiejar             0.014-5                       0.03 MiB               
extra/perl-http-cookies               6.11-4                        0.04 MiB               
extra/perl-http-daemon                6.17-1                        0.04 MiB               
extra/perl-http-date                  6.06-5                        0.01 MiB               
extra/perl-http-message               7.01-2                        0.16 MiB               
extra/perl-http-negotiate             6.01-16                       0.02 MiB               
extra/perl-io-html                    1.004-8                       0.02 MiB               
extra/perl-libwww                     6.83-1                        0.29 MiB               
extra/perl-lwp-mediatypes             6.04-8                        0.06 MiB               
extra/perl-mailtools                  2.22-3                        0.10 MiB               
extra/perl-net-http                   6.24-2                        0.04 MiB               
extra/perl-timedate                   2.35-1                        0.15 MiB               
extra/perl-try-tiny                   0.32-4                        0.03 MiB               
extra/perl-uri                        5.34-2                        0.21 MiB               
extra/perl-www-robotrules             6.03-1                        0.02 MiB               
extra/perl-xml-parser                 2.59-1                        0.68 MiB               
extra/perl-xml-writer                 0.900-6                       0.05 MiB               
core/pinentry                         1.3.2-2                       0.75 MiB               
extra/pixman                          0.46.4-1                      0.74 MiB               
extra/polkit                          127-3                         1.95 MiB               
core/popt                             1.19-2                        0.23 MiB               
extra/protobuf                        35.0-1                       18.73 MiB               
extra/protobuf-c                      1.5.2-10                      0.42 MiB               
extra/python-attrs                    26.1.0-1                      0.63 MiB               
extra/python-autocommand              2.2.2-9                       0.08 MiB               
extra/python-cffi                     2.0.0-2                       1.38 MiB               
extra/python-cryptography             48.0.0-1                      6.58 MiB               
extra/python-distlib                  0.4.1-1                       1.32 MiB               
extra/python-filelock                 3.29.0-1                      0.46 MiB               
extra/python-jaraco.collections       5.1.0-3                       0.11 MiB               
extra/python-jaraco.context           6.1.2-1                       0.06 MiB               
extra/python-jaraco.functools         4.1.0-3                       0.07 MiB               
extra/python-jaraco.text              4.0.0-4                       0.08 MiB               
extra/python-more-itertools           11.1.0-1                      0.77 MiB               
extra/python-packaging                26.2-1                        1.23 MiB               
extra/python-pkg_resources            81.0.0-1                      0.50 MiB               
extra/python-platformdirs             4.10.0-1                      0.45 MiB               
extra/python-pycparser                3.00-1                        0.71 MiB               
extra/python-python-discovery         1.4.0-1                       0.41 MiB               
extra/python-typing_extensions        4.15.0-3                      0.52 MiB               
core/readline                         8.3.003-1                     1.50 MiB               
core/rpcbind                          1.2.9-1                       0.10 MiB               
extra/rtkit                           0.14-1                        0.09 MiB               
extra/runc                            1.4.2-1                       9.77 MiB               
extra/shared-mime-info                2.4-3                         4.58 MiB               
extra/slang                           2.3.3-4                       3.36 MiB               
extra/speexdsp                        1.2.1-2                       0.54 MiB               
extra/spirv-tools                     1:1.4.350.0-1                 7.94 MiB               
core/sqlite                           3.53.2-1                     16.78 MiB       2.38 MiB
core/systemd-libs                     260.2-2                       3.48 MiB               
core/systemd-sysvcompat               260.2-2                       0.00 MiB               
extra/tdb                             1.4.15-1                      0.23 MiB               
core/thin-provisioning-tools          1.3.2-1                       3.07 MiB               
core/tpm2-tss                         4.1.3-1                       3.27 MiB               
extra/tre                             0.9.0-1                       0.16 MiB               
core/tzdata                           2026b-1                       1.64 MiB               
core/util-linux-libs                  2.42.1-1                      1.39 MiB               
extra/vim-runtime                     9.2.0573-1                   38.42 MiB               
extra/wayland                         1.25.0-1                      0.84 MiB               
extra/webrtc-audio-processing-1       1.3-5                         1.46 MiB               
extra/xcb-proto                       1.17.0-4                      1.03 MiB               
extra/xcb-util                        0.4.1-2                       0.03 MiB               
extra/xcb-util-image                  0.4.1-3                       0.05 MiB               
extra/xcb-util-keysyms                0.4.1-5                       0.02 MiB               
extra/xcb-util-renderutil             0.3.10-2                      0.03 MiB               
extra/xcb-util-wm                     0.4.2-2                       0.21 MiB               
extra/xf86-input-libinput             1.5.0-1                       0.10 MiB               
extra/xkeyboard-config                2.47-1                       10.23 MiB               
extra/xorg-fonts-alias-100dpi         1.0.6-1                       0.00 MiB               
extra/xorg-fonts-alias-75dpi          1.0.6-1                       0.00 MiB               
extra/xorg-util-macros                1.20.2-1                      0.09 MiB               
extra/xorgproto                       2025.1-1                      1.47 MiB               
extra/xxhash                          0.8.3-1                       0.39 MiB               
core/xz                               5.8.3-1                       2.97 MiB               
extra/zeromq                          4.3.5-3                       3.03 MiB               
core/zlib                             1:1.3.2-3                     0.22 MiB               
extra/zlib-ng                         2.3.3-1                       0.28 MiB               
core/acl                              2.3.2-2                       0.33 MiB               
extra/alsa-utils                      1.2.16-1                      2.47 MiB               
extra/arch-install-scripts            31-1                          0.04 MiB               
core/base                             3-3                           0.00 MiB               
core/bash                             5.3.9-1                       9.56 MiB               
core/btrfs-progs                      7.0-1                         6.73 MiB               
extra/busybox                         1.36.1-4                      1.76 MiB               
core/coreutils                        9.11-1                       27.50 MiB               
extra/cpio                            2.15-3                        0.98 MiB               
core/cryptsetup                       2.8.6-1                       3.29 MiB               
core/curl                             8.20.0-7                      2.18 MiB               
extra/dhcpcd                          10.3.2-1                      0.48 MiB               
extra/dmidecode                       3.7-1                         0.20 MiB               
core/dmraid                           1.0.0.rc16.3-15               0.31 MiB               
extra/dnsmasq                         2.92.rel2-2                   1.09 MiB               
extra/docker                          1:29.5.2-1                  113.08 MiB               
extra/docker-compose                  5.1.4-1                      28.30 MiB               
core/dosfstools                       4.2-5                         0.40 MiB               
core/e2fsprogs                        1.47.4-1                      5.28 MiB               
core/efibootmgr                       18-4                          0.08 MiB               
extra/elinks                          0.19.1-3                      4.06 MiB               
extra/espeak-ng                       1.52.0-1                     18.05 MiB               
extra/exfatprogs                      1.4.1-1                       0.34 MiB               
extra/f2fs-tools                      1.16.0-3                      0.57 MiB               
extra/fwupd                           2.1.4-2                      18.65 MiB               
core/gawk                             5.4.0-1                       4.02 MiB               
core/gcc-libs                         16.1.1+r12+g301eb08fa2c5-1    0.00 MiB               
core/gettext                          1.0-2                        20.79 MiB               
extra/git                             2.54.0-1                     30.26 MiB               
core/glibc                            2.43+r22+g8362e8ce10b2-2     50.35 MiB               
core/gpgme                            2.1.0-1                       0.77 MiB               
extra/gptfdisk                        1.0.10-2                      0.72 MiB               
core/grep                             3.12-2                        0.88 MiB               
core/grub                             2:2.14-1                     41.49 MiB               
core/gzip                             1.14-2                        0.16 MiB               
extra/hwinfo                          25.2-1                        3.91 MiB               
core/inetutils                        2.8-1                         1.08 MiB               
core/iproute2                         7.0.0-1                       3.01 MiB               
core/iputils                          20250605-1                    0.65 MiB               
extra/iwd                             3.12-1                        2.18 MiB               
core/jfsutils                         1.1.15-9                      0.93 MiB               
core/less                             1:702-1                       0.33 MiB               
core/linux-lts                        6.18.34-1                   144.49 MiB               
core/logrotate                        3.22.0-1                      0.10 MiB               
extra/lshw                            B.02.20-3                     8.09 MiB               
core/lvm2                             2.03.41-1                     5.18 MiB               
core/man-db                           2.13.1-1                      2.41 MiB               
core/man-pages                        6.18-1                        5.64 MiB               
core/mdadm                            4.6-2                         1.02 MiB               
extra/memtest86+                      7.20-2                        0.15 MiB               
core/nano                             9.0-1                         2.76 MiB               
core/ncurses                          6.6-2                         4.09 MiB               
extra/netctl                          1.29-2                        0.09 MiB               
extra/networkmanager                  1.56.1-1                     15.74 MiB               
core/nfs-utils                        2.9.1-1                       1.31 MiB               
core/nilfs-utils                      2.3.0-1                       0.38 MiB               
extra/ntfs-3g                         2026.2.25-1                   0.16 MiB               
core/openssh                          10.3p1-1                      5.46 MiB               
core/pacman                           7.1.0.r9.g54d9411-2           5.04 MiB               
extra/pacman-contrib                  1.13.1-1                      0.13 MiB               
extra/parted                          3.7-1                         2.55 MiB               
core/pciutils                         3.15.0-1                      0.41 MiB               
extra/ppl                             1.2-7                        17.09 MiB               
core/procps-ng                        4.0.6-1                       2.54 MiB               
core/psmisc                           23.7-2                        0.76 MiB               
extra/pulseaudio                      17.0+r98+gb096704c0-1         6.30 MiB               
core/python                           3.14.5-1                     73.34 MiB               
extra/python-pip                      26.1.2-1                     16.77 MiB               
extra/python-setuptools               1:82.0.1-1                    7.35 MiB               
extra/python-virtualenv               21.4.2-1                      8.64 MiB               
extra/python-wheel                    0.47.0-1                      0.33 MiB               
extra/rsync                           3.4.3-1                       0.71 MiB               
core/s-nail                           14.9.25-1                     1.01 MiB               
core/sed                              4.10-1                        0.78 MiB               
core/shadow                           4.18.0-1                      3.91 MiB               
extra/sysfsutils                      2.1.1-2                       0.09 MiB               
core/syslinux                         6.04.pre3.r3.g05ac953c-4      4.27 MiB               
core/systemd                          260.2-2                      37.39 MiB               
core/systemd-resolvconf               260.2-2                       0.00 MiB               
core/tar                              1.35-2                        2.80 MiB               
core/texinfo                          7.3-1                        12.67 MiB               
core/usbutils                         019-1                         0.37 MiB               
core/util-linux                       2.42.1-1                     19.70 MiB               
extra/vim                             9.2.0573-1                    5.34 MiB               
extra/wget                            1.25.0-5                      5.70 MiB               
core/which                            2.25-1                        0.03 MiB               
extra/wireless_tools                  30.pre9-5                     0.34 MiB               
core/wpa_supplicant                   2:2.11-5                      6.62 MiB               
extra/xf86-video-vesa                 2.6.0-3                       0.03 MiB               
core/xfsprogs                         7.0.1-1                       4.60 MiB               
extra/xorg-bdftopcf                   1.1.2-1                       0.04 MiB               
extra/xorg-docs                       1.7.3-3                       0.84 MiB               
extra/xorg-font-util                  1.4.2-1                       0.22 MiB               
extra/xorg-fonts-100dpi               1.0.4-3                      12.18 MiB               
extra/xorg-fonts-75dpi                1.0.4-2                      10.64 MiB               
extra/xorg-fonts-encodings            1.1.0-2                       0.61 MiB               
extra/xorg-iceauth                    1.0.11-1                      0.04 MiB               
extra/xorg-mkfontscale                1.2.4-1                       0.05 MiB               
extra/xorg-server                     21.1.23-1                     3.86 MiB               
extra/xorg-server-common              21.1.23-1                     0.12 MiB               
extra/xorg-server-devel               21.1.23-1                     1.20 MiB               
extra/xorg-server-src                 21.1.23-1                    21.32 MiB               
extra/xorg-server-xephyr              21.1.23-1                     2.36 MiB               
extra/xorg-server-xnest               21.1.23-1                     1.49 MiB               
extra/xorg-server-xvfb                21.1.23-1                     1.98 MiB               
extra/xorg-sessreg                    1.1.4-1                       0.02 MiB               
extra/xorg-setxkbmap                  1.3.5-1                       0.03 MiB               
extra/xorg-smproxy                    1.0.8-1                       0.03 MiB               
extra/xorg-x11perf                    1.7.0-1                       0.18 MiB               
extra/xorg-xauth                      1.1.5-1                       0.05 MiB               
extra/xorg-xbacklight                 1.2.4-1                       0.02 MiB               
extra/xorg-xcmsdb                     1.0.7-1                       0.03 MiB               
extra/xorg-xcursorgen                 1.0.9-1                       0.02 MiB               
extra/xorg-xdpyinfo                   1.4.0-1                       0.03 MiB               
extra/xorg-xdriinfo                   1.0.8-1                       0.02 MiB               
extra/xorg-xev                        1.2.7-1                       0.04 MiB               
extra/xorg-xgamma                     1.0.8-1                       0.02 MiB               
extra/xorg-xhost                      1.0.10-1                      0.02 MiB               
extra/xorg-xinit                      1.4.4-1                       0.04 MiB               
extra/xorg-xinput                     1.6.4-2                       0.06 MiB               
extra/xorg-xkbcomp                    1.5.0-1                       0.21 MiB               
extra/xorg-xkbevd                     1.1.6-1                       0.04 MiB               
extra/xorg-xkbutils                   1.0.6-2                       0.06 MiB               
extra/xorg-xkill                      1.0.7-1                       0.02 MiB               
extra/xorg-xlsatoms                   1.1.4-2                       0.02 MiB               
extra/xorg-xlsclients                 1.1.6-1                       0.02 MiB               
extra/xorg-xmodmap                    1.0.11-2                      0.05 MiB               
extra/xorg-xpr                        1.2.0-2                       0.06 MiB               
extra/xorg-xprop                      1.2.8-1                       0.05 MiB               
extra/xorg-xrandr                     1.5.4-1                       0.07 MiB               
extra/xorg-xrdb                       1.2.2-2                       0.04 MiB               
extra/xorg-xrefresh                   1.1.0-2                       0.02 MiB               
extra/xorg-xset                       1.2.5-2                       0.04 MiB               
extra/xorg-xsetroot                   1.1.3-2                       0.02 MiB               
extra/xorg-xvinfo                     1.1.5-2                       0.02 MiB               
extra/xorg-xwayland                   24.1.12-1                     2.35 MiB               
extra/xorg-xwd                        1.0.9-2                       0.03 MiB               
extra/xorg-xwininfo                   1.1.6-2                       0.05 MiB               
extra/xorg-xwud                       1.0.7-1                       0.03 MiB               
core/zstd                             1.5.7-3                       1.54 MiB               

Total Download Size:      5.47 MiB
Total Installed Size:  1906.46 MiB

:: Proceed with installation? [Y/n] 
:: Retrieving packages...
 graphite-1:1.3.15-1-x86_64                84.8 KiB  73.5 KiB/s 00:01 [######################################] 100%
 libinput-1.31.3-1-x86_64                 228.4 KiB   149 KiB/s 00:02 [######################################] 100%
 sqlite-3.53.2-1-x86_64                     2.4 MiB   622 KiB/s 00:04 [######################################] 100%
 linux-api-headers-7.0-1-x86_64          1533.9 KiB   368 KiB/s 00:04 [######################################] 100%
 kbd-2.10.0-1-x86_64                     1309.7 KiB   308 KiB/s 00:04 [######################################] 100%
 Total (5/5)                                5.5 MiB  1297 KiB/s 00:04 [######################################] 100%
(464/464) checking keys in keyring                                    [######################################] 100%
-( 17/464) checking package integrity                                  [#-------------------------------------]   3(464/464) checking package integrity                                  [######################################] 100%
(464/464) loading package files                                       [######################################] 100%
(464/464) checking for file conflicts                                 [######################################] 100%
(464/464) checking available disk space                               [######################################] 100%
:: Processing package changes...
(  1/464) installing linux-api-headers                                [######################################] 100%
(  2/464) installing tzdata                                           [######################################] 100%
Optional dependencies for tzdata
    bash: for tzselect [pending]
    glibc: for zdump, zic [pending]
(  3/464) installing iana-etc                                         [######################################] 100%
(  4/464) installing filesystem                                       [######################################] 100%
warning: /tmp/jarvis-iso-build-69948/x86_64/airootfs/etc/gshadow installed as /tmp/jarvis-iso-build-69948/x86_64/airootfs/etc/gshadow.pacnew
warning: /tmp/jarvis-iso-build-69948/x86_64/airootfs/etc/shadow installed as /tmp/jarvis-iso-build-69948/x86_64/airootfs/etc/shadow.pacnew
(  5/464) installing glibc                                            [######################################] 100%
Optional dependencies for glibc
    gd: for memusagestat
    perl: for mtrace [pending]
(  6/464) installing acl                                              [######################################] 100%
(  7/464) installing libgcc                                           [######################################] 100%
(  8/464) installing libstdc++                                        [######################################] 100%
(  9/464) installing ncurses                                          [######################################] 100%
Optional dependencies for ncurses
    bash: for ncursesw6-config [pending]
( 10/464) installing readline                                         [######################################] 100%
( 11/464) installing bash                                             [######################################] 100%
Optional dependencies for bash
    bash-completion: for tab completion
( 12/464) installing gmp                                              [######################################] 100%
( 13/464) installing mpfr                                             [######################################] 100%
( 14/464) installing gawk                                             [######################################] 100%
( 15/464) installing attr                                             [######################################] 100%
( 16/464) installing zlib                                             [######################################] 100%
( 17/464) installing sqlite                                           [######################################] 100%
( 18/464) installing util-linux-libs                                  [######################################] 100%
Optional dependencies for util-linux-libs
    python: python bindings to libmount [pending]
( 19/464) installing e2fsprogs                                        [######################################] 100%
Optional dependencies for e2fsprogs
    lvm2: for e2scrub [pending]
    util-linux: for e2scrub [pending]
    smtp-forwarder: for e2scrub_fail script
( 20/464) installing keyutils                                         [######################################] 100%
( 21/464) installing gdbm                                             [######################################] 100%
( 22/464) installing brotli                                           [######################################] 100%
( 23/464) installing xz                                               [######################################] 100%
( 24/464) installing lz4                                              [######################################] 100%
( 25/464) installing zstd                                             [######################################] 100%
( 26/464) installing openssl                                          [######################################] 100%
Optional dependencies for openssl
    ca-certificates [pending]
    perl [pending]
( 27/464) installing libsasl                                          [######################################] 100%
( 28/464) installing libldap                                          [######################################] 100%
( 29/464) installing libevent                                         [######################################] 100%
Optional dependencies for libevent
    python: event_rpcgen.py [pending]
( 30/464) installing libverto                                         [######################################] 100%
( 31/464) installing lmdb                                             [######################################] 100%
( 32/464) installing krb5                                             [######################################] 100%
( 33/464) installing libcap-ng                                        [######################################] 100%
( 34/464) installing audit                                            [######################################] 100%
Optional dependencies for audit
    audispd-plugins: for audit event dispatcher plugins
    audispd-plugins-zos: for z/OS audit event dispatcher plugin
( 35/464) installing libxcrypt                                        [######################################] 100%
( 36/464) installing libtirpc                                         [######################################] 100%
( 37/464) installing libnsl                                           [######################################] 100%
( 38/464) installing pambase                                          [######################################] 100%
( 39/464) installing libgpg-error                                     [######################################] 100%
( 40/464) installing libgcrypt                                        [######################################] 100%
( 41/464) installing systemd-libs                                     [######################################] 100%
( 42/464) installing pam                                              [######################################] 100%
( 43/464) installing libcap                                           [######################################] 100%
( 44/464) installing coreutils                                        [######################################] 100%
( 45/464) installing bzip2                                            [######################################] 100%
( 46/464) installing pcre2                                            [######################################] 100%
Optional dependencies for pcre2
    sh: for pcre2-config [installed]
( 47/464) installing grep                                             [######################################] 100%
( 48/464) installing findutils                                        [######################################] 100%
( 49/464) installing libtasn1                                         [######################################] 100%
( 50/464) installing libffi                                           [######################################] 100%
( 51/464) installing libp11-kit                                       [######################################] 100%
( 52/464) installing p11-kit                                          [######################################] 100%
( 53/464) installing ca-certificates-utils                            [######################################] 100%
( 54/464) installing ca-certificates-mozilla                          [######################################] 100%
( 55/464) installing ca-certificates                                  [######################################] 100%
( 56/464) installing libunistring                                     [######################################] 100%
( 57/464) installing libidn2                                          [######################################] 100%
( 58/464) installing libnghttp2                                       [######################################] 100%
( 59/464) installing libnghttp3                                       [######################################] 100%
( 60/464) installing nettle                                           [######################################] 100%
( 61/464) installing leancrypto                                       [######################################] 100%
( 62/464) installing gnutls                                           [######################################] 100%
Optional dependencies for gnutls
    tpm2-tss: support for TPM2 wrapped keys [pending]
( 63/464) installing libngtcp2                                        [######################################] 100%
( 64/464) installing libpsl                                           [######################################] 100%
( 65/464) installing libssh2                                          [######################################] 100%
( 66/464) installing curl                                             [######################################] 100%
( 67/464) installing json-c                                           [######################################] 100%
( 68/464) installing libgomp                                          [######################################] 100%
( 69/464) installing gnulib-l10n                                      [######################################] 100%
( 70/464) installing icu                                              [######################################] 100%
( 71/464) installing libxml2                                          [######################################] 100%
Optional dependencies for libxml2
    python: Python bindings [pending]
( 72/464) installing gettext                                          [######################################] 100%
Optional dependencies for gettext
    git: for autopoint infrastructure updates [pending]
    appstream: for appstream support
( 73/464) installing libksba                                          [######################################] 100%
( 74/464) installing libusb                                           [######################################] 100%
( 75/464) installing libassuan                                        [######################################] 100%
( 76/464) installing libsysprof-capture                               [######################################] 100%
( 77/464) installing glib2                                            [######################################] 100%
Optional dependencies for glib2
    dconf: GSettings storage backend [pending]
    glib2-devel: development tools
    gvfs: most gio functionality
( 78/464) installing tpm2-tss                                         [######################################] 100%
( 79/464) installing libsecret                                        [######################################] 100%
Optional dependencies for libsecret
    org.freedesktop.secrets: secret storage backend
( 80/464) installing pinentry                                         [######################################] 100%
Optional dependencies for pinentry
    gcr: GNOME backend
    gtk3: GTK backend
    qt5-x11extras: Qt5 backend
    kwayland5: Qt5 backend
    kguiaddons: Qt6 backend
    kwindowsystem: Qt6 backend
( 81/464) installing npth                                             [######################################] 100%
( 82/464) installing gnupg                                            [######################################] 100%
Optional dependencies for gnupg
    pcsclite: for using scdaemon not with the gnupg internal card driver [pending]
( 83/464) installing gpgme                                            [######################################] 100%
( 84/464) installing libarchive                                       [######################################] 100%
( 85/464) installing pacman-mirrorlist                                [######################################] 100%
( 86/464) installing device-mapper                                    [######################################] 100%
( 87/464) installing popt                                             [######################################] 100%
( 88/464) installing cryptsetup                                       [######################################] 100%
( 89/464) installing expat                                            [######################################] 100%
( 90/464) installing dbus                                             [######################################] 100%
( 91/464) installing dbus-broker                                      [######################################] 100%
( 92/464) installing dbus-broker-units                                [######################################] 100%
( 93/464) installing dbus-units                                       [######################################] 100%
( 94/464) installing sed                                              [######################################] 100%
( 95/464) installing gzip                                             [######################################] 100%
Optional dependencies for gzip
    less: zless support [pending]
    util-linux: zmore support [pending]
    diffutils: zdiff/zcmp support [pending]
( 96/464) installing kbd                                              [######################################] 100%
( 97/464) installing kmod                                             [######################################] 100%
( 98/464) installing hwdata                                           [######################################] 100%
( 99/464) installing libelf                                           [######################################] 100%
(100/464) installing libseccomp                                       [######################################] 100%
(101/464) installing file                                             [######################################] 100%
(102/464) installing shadow                                           [######################################] 100%
(103/464) installing util-linux                                       [######################################] 100%
Optional dependencies for util-linux
    words: default dictionary for look
(104/464) installing systemd                                          [######################################] 100%
Initializing machine ID from random generator.
Creating group 'sys' with GID 3.
Creating group 'mem' with GID 8.
Creating group 'ftp' with GID 11.
Creating group 'mail' with GID 12.
Creating group 'log' with GID 19.
Creating group 'smmsp' with GID 25.
Creating group 'proc' with GID 26.
Creating group 'games' with GID 50.
Creating group 'lock' with GID 54.
Creating group 'network' with GID 90.
Creating group 'floppy' with GID 94.
Creating group 'scanner' with GID 96.
Creating group 'power' with GID 98.
Creating group 'nobody' with GID 65534.
Creating group 'adm' with GID 999.
Creating group 'wheel' with GID 998.
Creating group 'empower' with GID 997.
Creating group 'utmp' with GID 996.
Creating group 'audio' with GID 995.
Creating group 'clock' with GID 994.
Creating group 'disk' with GID 993.
Creating group 'input' with GID 992.
Creating group 'kmem' with GID 991.
Creating group 'kvm' with GID 990.
Creating group 'lp' with GID 989.
Creating group 'optical' with GID 988.
Creating group 'render' with GID 987.
Creating group 'sgx' with GID 986.
Creating group 'storage' with GID 985.
Creating group 'tty' with GID 5.
Creating group 'uucp' with GID 984.
Creating group 'video' with GID 983.
Creating group 'users' with GID 982.
Creating group 'groups' with GID 981.
Creating group 'systemd-journal' with GID 980.
Creating group 'rfkill' with GID 979.
Creating group 'bin' with GID 1.
Creating user 'bin' (n/a) with UID 1 and GID 1.
Creating group 'daemon' with GID 2.
Creating user 'daemon' (n/a) with UID 2 and GID 2.
Creating user 'mail' (n/a) with UID 8 and GID 12.
Creating user 'ftp' (n/a) with UID 14 and GID 11.
Creating group 'http' with GID 33.
Creating user 'http' (n/a) with UID 33 and GID 33.
Creating user 'nobody' (Kernel Overflow User) with UID 65534 and GID 65534.
Creating group 'dbus' with GID 81.
Creating user 'dbus' (System Message Bus) with UID 81 and GID 81.
Creating group 'systemd-coredump' with GID 978.
Creating user 'systemd-coredump' (systemd Core Dumper) with UID 978 and GID 978.
Creating group 'systemd-network' with GID 977.
Creating user 'systemd-network' (systemd Network Management) with UID 977 and GID 977.
Creating group 'systemd-oom' with GID 976.
Creating user 'systemd-oom' (systemd Userspace OOM Killer) with UID 976 and GID 976.
Creating group 'systemd-journal-remote' with GID 975.
Creating user 'systemd-journal-remote' (systemd Journal Remote) with UID 975 and GID 975.
Creating group 'systemd-resolve' with GID 974.
Creating user 'systemd-resolve' (systemd Resolver) with UID 974 and GID 974.
Creating group 'systemd-timesync' with GID 973.
Creating user 'systemd-timesync' (systemd Time Synchronization) with UID 973 and GID 973.
Creating group 'tss' with GID 972.
Creating user 'tss' (tss user for tpm2) with UID 972 and GID 972.
Creating group 'uuidd' with GID 971.
Creating user 'uuidd' (UUID generator helper daemon) with UID 971 and GID 971.
Created symlink '/etc/systemd/system/autovt@.service' → '/usr/lib/systemd/system/getty@.service'.
Created symlink '/etc/systemd/system/getty.target.wants/getty@tty1.service' → '/usr/lib/systemd/system/getty@.service'.
Created symlink '/etc/systemd/system/multi-user.target.wants/remote-fs.target' → '/usr/lib/systemd/system/remote-fs.target'.
Created symlink '/etc/systemd/system/sockets.target.wants/systemd-userdbd.socket' → '/usr/lib/systemd/system/systemd-userdbd.socket'.
Optional dependencies for systemd
    libmicrohttpd: systemd-journal-gatewayd and systemd-journal-remote
    apparmor: additional security features
    quota-tools: kernel-level quota management
    systemd-sysvcompat: symlink package to provide sysvinit binaries [pending]
    systemd-ukify: combine kernel and initrd into a signed Unified Kernel Image
    polkit: allow administration as unprivileged user [pending]
    curl: systemd-journal-upload, machinectl pull-tar and pull-raw [installed]
    gnutls: systemd-journal-gatewayd and systemd-journal-remote [installed]
    qrencode: show QR codes
    iptables: firewall features [pending]
    libarchive: convert DDIs to tarballs [installed]
    libbpf: support BPF programs [pending]
    libpwquality: check password quality
    libfido2: unlocking LUKS2 volumes with FIDO2 token
    libp11-kit: support PKCS#11 [installed]
    tpm2-tss: unlocking LUKS2 volumes with TPM2 [installed]
(105/464) installing jansson                                          [######################################] 100%
(106/464) installing binutils                                         [######################################] 100%
Optional dependencies for binutils
    debuginfod: for debuginfod server/client functionality
    perl: for gprofng-display-html [pending]
(107/464) installing libmakepkg-dropins                               [######################################] 100%
(108/464) installing pacman                                           [######################################] 100%
Optional dependencies for pacman
    base-devel: required to use makepkg
    perl-locale-gettext: translation support in makepkg-template
(109/464) installing arch-install-scripts                             [######################################] 100%
(110/464) installing libasan                                          [######################################] 100%
(111/464) installing libatomic                                        [######################################] 100%
(112/464) installing libgfortran                                      [######################################] 100%
(113/464) installing liblsan                                          [######################################] 100%
(114/464) installing libobjc                                          [######################################] 100%
(115/464) installing libquadmath                                      [######################################] 100%
(116/464) installing libtsan                                          [######################################] 100%
(117/464) installing libubsan                                         [######################################] 100%
(118/464) installing gcc-libs                                         [######################################] 100%
(119/464) installing procps-ng                                        [######################################] 100%
(120/464) installing tar                                              [######################################] 100%
(121/464) installing pciutils                                         [######################################] 100%
Optional dependencies for pciutils
    which: for update-pciids [pending]
    grep: for update-pciids [installed]
    curl: for update-pciids [installed]
(122/464) installing psmisc                                           [######################################] 100%
(123/464) installing licenses                                         [######################################] 100%
(124/464) installing archlinux-keyring                                [######################################] 100%
(125/464) installing systemd-sysvcompat                               [######################################] 100%
(126/464) installing iputils                                          [######################################] 100%
(127/464) installing libmnl                                           [######################################] 100%
(128/464) installing libnfnetlink                                     [######################################] 100%
(129/464) installing libnetfilter_conntrack                           [######################################] 100%
(130/464) installing libnftnl                                         [######################################] 100%
(131/464) installing libnl                                            [######################################] 100%
(132/464) installing libpcap                                          [######################################] 100%
(133/464) installing nftables                                         [######################################] 100%
Optional dependencies for nftables
    python: Python bindings [pending]
    python-jsonschema: Python bindings
(134/464) installing iptables                                         [######################################] 100%
(135/464) installing libbpf                                           [######################################] 100%
(136/464) installing iproute2                                         [######################################] 100%
Optional dependencies for iproute2
    db: userspace arp daemon
    linux-atm: ATM support
    python: for routel [pending]
(137/464) installing base                                             [######################################] 100%
Optional dependencies for base
    linux: bare metal support
(138/464) installing lzo                                              [######################################] 100%
(139/464) installing btrfs-progs                                      [######################################] 100%
Optional dependencies for btrfs-progs
    python: libbtrfsutil python bindings [pending]
    e2fsprogs: btrfs-convert [installed]
(140/464) installing busybox                                          [######################################] 100%
(141/464) installing cpio                                             [######################################] 100%
(142/464) installing dmraid                                           [######################################] 100%
(143/464) installing dosfstools                                       [######################################] 100%
(144/464) installing efivar                                           [######################################] 100%
(145/464) installing efibootmgr                                       [######################################] 100%
(146/464) installing gpm                                              [######################################] 100%
(147/464) installing lua                                              [######################################] 100%
(148/464) installing libparserutils                                   [######################################] 100%
(149/464) installing libhubbub                                        [######################################] 100%
(150/464) installing libwapcaplet                                     [######################################] 100%
(151/464) installing libdom                                           [######################################] 100%
(152/464) installing libcss                                           [######################################] 100%
(153/464) installing tre                                              [######################################] 100%
(154/464) installing elinks                                           [######################################] 100%
(155/464) installing exfatprogs                                       [######################################] 100%
(156/464) installing f2fs-tools                                       [######################################] 100%
(157/464) installing gptfdisk                                         [######################################] 100%
(158/464) installing grub                                             [######################################] 100%
:: Install your bootloader and generate configuration with:
     # grub-install ...
     # grub-mkconfig -o /boot/grub/grub.cfg
Optional dependencies for grub
    dosfstools: For grub-mkrescue FAT FS and EFI support [installed]
    efibootmgr: For grub-install EFI support [installed]
    freetype2: For grub-mkfont usage [pending]
    fuse3: For grub-mount usage
    libisoburn: Provides xorriso for generating grub rescue iso using grub-mkrescue
    libusb: For grub-emu USB support [installed]
    lzop: For grub-mkrescue LZO support
    mtools: For grub-mkrescue FAT FS support
    os-prober: To detect other OSes when generating grub.cfg in BIOS systems
    sdl: For grub-emu SDL support
(159/464) installing inetutils                                        [######################################] 100%
(160/464) installing jfsutils                                         [######################################] 100%
(161/464) installing less                                             [######################################] 100%
(162/464) installing mkinitcpio-busybox                               [######################################] 100%
(163/464) installing diffutils                                        [######################################] 100%
(164/464) installing mkinitcpio                                       [######################################] 100%
Optional dependencies for mkinitcpio
    xz: Use lzma or xz compression for the initramfs image [installed]
    bzip2: Use bzip2 compression for the initramfs image [installed]
    lzop: Use lzo compression for the initramfs image
    lz4: Use lz4 compression for the initramfs image [installed]
    mkinitcpio-nfs-utils: Support for root filesystem on NFS
    systemd-ukify: alternative UKI generator
(165/464) installing linux-lts                                        [######################################] 100%
Optional dependencies for linux-lts
    wireless-regdb: to set the correct wireless channels of your country
    linux-firmware: firmware images needed for some devices
    scx-scheds: to use sched-ext schedulers
(166/464) installing logrotate                                        [######################################] 100%
(167/464) installing libaio                                           [######################################] 100%
(168/464) installing thin-provisioning-tools                          [######################################] 100%
(169/464) installing lvm2                                             [######################################] 100%
(170/464) installing db5.3                                            [######################################] 100%
(171/464) installing perl                                             [######################################] 100%
(172/464) installing groff                                            [######################################] 100%
Optional dependencies for groff
    netpbm: for use together with man -H command interaction in browsers
    psutils: for use together with man -H command interaction in browsers
    libxaw: for gxditview [pending]
    perl-file-homedir: for use with glilypond
(173/464) installing libpipeline                                      [######################################] 100%
(174/464) installing man-db                                           [######################################] 100%
Optional dependencies for man-db
    gzip [installed]
(175/464) installing man-pages                                        [######################################] 100%
(176/464) installing mdadm                                            [######################################] 100%
Optional dependencies for mdadm
    bash: mdcheck [installed]
(177/464) installing memtest86+                                       [######################################] 100%
(178/464) installing nano                                             [######################################] 100%
(179/464) installing systemd-resolvconf                               [######################################] 100%
(180/464) installing netctl                                           [######################################] 100%
Optional dependencies for netctl
    dialog: for the menu based wifi assistant
    dhclient: for DHCP support (or dhcpcd)
    dhcpcd: for DHCP support (or dhclient) [pending]
    wpa_supplicant: for wireless networking support [pending]
    ifplugd: for automatic wired connections through netctl-ifplugd
    ppp: for PPP connections
    openvswitch: for Open vSwitch connections
    wireguard-tools: for WireGuard connections
(181/464) installing libmm-glib                                       [######################################] 100%
(182/464) installing libndp                                           [######################################] 100%
(183/464) installing pcre                                             [######################################] 100%
(184/464) installing slang                                            [######################################] 100%
(185/464) installing libnewt                                          [######################################] 100%
Optional dependencies for libnewt
    python: libnewt support with the _snack module [pending]
    tcl: whiptcl support
(186/464) installing nspr                                             [######################################] 100%
(187/464) installing nss                                              [######################################] 100%
(188/464) installing libnm                                            [######################################] 100%
(189/464) installing libdaemon                                        [######################################] 100%
(190/464) installing libsodium                                        [######################################] 100%
(191/464) installing libpgm                                           [######################################] 100%
(192/464) installing zeromq                                           [######################################] 100%
Optional dependencies for zeromq
    cppzmq: C++ binding for libzmq
(193/464) installing libteam                                          [######################################] 100%
(194/464) installing mobile-broadband-provider-info                   [######################################] 100%
(195/464) installing duktape                                          [######################################] 100%
(196/464) installing polkit                                           [######################################] 100%
(197/464) installing pcsclite                                         [######################################] 100%
Optional dependencies for pcsclite
    python: API call trace logging with the pcsc-spy [pending]
    ccid: USB Chip/Smart Card Interface Devices driver
(198/464) installing wpa_supplicant                                   [######################################] 100%
(199/464) installing networkmanager                                   [######################################] 100%
Optional dependencies for networkmanager
    bluez: Bluetooth support [pending]
    dhcpcd: alternative DHCP client [pending]
    dnsmasq: connection sharing [pending]
    firewalld: firewall support
    iptables: connection sharing [installed]
    iwd: wpa_supplicant alternative [pending]
    libnvme: NBFT support
    modemmanager: cellular network support
    nftables: connection sharing [installed]
    openresolv: alternative resolv.conf manager [installed]
    pacrunner: PAC proxy support
    polkit: let non-root users control networking [installed]
    ppp: dialup connection support
(200/464) installing rpcbind                                          [######################################] 100%
(201/464) installing nfsidmap                                         [######################################] 100%
(202/464) installing ding-libs                                        [######################################] 100%
(203/464) installing gssproxy                                         [######################################] 100%
(204/464) installing nfs-utils                                        [######################################] 100%
Optional dependencies for nfs-utils
    sqlite: for nfsdcltrack and fsidd usage [installed]
    python: for rpcctl, nfsiostat, nfsdclnts and mountstats usage [pending]
(205/464) installing nilfs-utils                                      [######################################] 100%
(206/464) installing fuse-common                                      [######################################] 100%
(207/464) installing fuse2                                            [######################################] 100%
(208/464) installing libntfs-3g                                       [######################################] 100%
(209/464) installing ntfs-3g                                          [######################################] 100%
Optional dependencies for ntfs-3g
    ntfsprogs: userspace utilities
(210/464) installing libedit                                          [######################################] 100%
(211/464) installing openssh                                          [######################################] 100%
Optional dependencies for openssh
    libfido2: FIDO/U2F support
    sh: for ssh-copy-id and findssl.sh [installed]
    x11-ssh-askpass: input passphrase in X
    xorg-xauth: X11 forwarding [pending]
(212/464) installing pacman-contrib                                   [######################################] 100%
Optional dependencies for pacman-contrib
    diffutils: for pacdiff [installed]
    fakeroot: for checkupdates
    findutils: for pacdiff --find [installed]
    mlocate: for pacdiff --locate
    plocate: faster mlocate alternative
    perl: for pacsearch [installed]
    sudo: privilege elevation for several scripts
    vim: default diff program for pacdiff [pending]
    neovim: default diff program for pacdiff if EDITOR=nvim
(213/464) installing parted                                           [######################################] 100%
(214/464) installing glpk                                             [######################################] 100%
(215/464) installing ppl                                              [######################################] 100%
Optional dependencies for ppl
    swi-prolog: SWI Prolog interface
(216/464) installing xxhash                                           [######################################] 100%
(217/464) installing rsync                                            [######################################] 100%
Optional dependencies for rsync
    python: for rrsync [pending]
(218/464) installing s-nail                                           [######################################] 100%
Optional dependencies for s-nail
    smtp-forwarder: for sending mail
(219/464) installing sysfsutils                                       [######################################] 100%
(220/464) installing syslinux                                         [######################################] 100%

==> For setting up Syslinux BIOS using the syslinux-install_update script follow
    https://wiki.archlinux.org/index.php/Syslinux#Automatic_Install

==> For setting up Syslinux EFI follow
    https://wiki.archlinux.org/index.php/Syslinux#UEFI_Systems

==> The syslinux-install_update script does not currently support EFI install

Optional dependencies for syslinux
    perl-crypt-passwdmd5: For md5pass
    perl-digest-sha1: For sha1pass
    mtools: For mkdiskimage and syslinux support
    gptfdisk: For GPT support [installed]
    util-linux: For isohybrid [installed]
    efibootmgr: For EFI support [installed]
    dosfstools: For EFI support [installed]
(221/464) installing texinfo                                          [######################################] 100%
Optional dependencies for texinfo
    perl-archive-zip: EPUB file output via texi2any
(222/464) installing usbutils                                         [######################################] 100%
Optional dependencies for usbutils
    coreutils: for lsusb.py usage [installed]
    python: for lsusb.py usage [pending]
    sh: for usb-devices [installed]
(223/464) installing vim-runtime                                      [######################################] 100%
Optional dependencies for vim-runtime
    sh: support for some tools and macros [installed]
    python: demoserver example tool [pending]
    gawk: mve tools support [installed]
(224/464) installing vim                                              [######################################] 100%
Optional dependencies for vim
    python: Python language support [pending]
    ruby: Ruby language support
    lua: Lua language support [installed]
    perl: Perl language support [installed]
    tcl: Tcl language support
(225/464) installing which                                            [######################################] 100%
(226/464) installing libinih                                          [######################################] 100%
(227/464) installing liburcu                                          [######################################] 100%
(228/464) installing xfsprogs                                         [######################################] 100%
Optional dependencies for xfsprogs
    icu: for xfs_scrub [installed]
    python-dbus: for xfs_scrub_all script
    smtp-forwarder: for xfs_scrub_fail script
(229/464) installing xf86-video-vesa                                  [######################################] 100%
(230/464) installing xorg-bdftopcf                                    [######################################] 100%
(231/464) installing xorg-docs                                        [######################################] 100%
(232/464) installing xorg-font-util                                   [######################################] 100%
(233/464) installing xorg-fonts-alias-100dpi                          [######################################] 100%
(234/464) installing xorg-fonts-100dpi                                [######################################] 100%
(235/464) installing xorg-fonts-alias-75dpi                           [######################################] 100%
(236/464) installing xorg-fonts-75dpi                                 [######################################] 100%
(237/464) installing xorg-fonts-encodings                             [######################################] 100%
(238/464) installing xorgproto                                        [######################################] 100%
(239/464) installing libice                                           [######################################] 100%
(240/464) installing xorg-iceauth                                     [######################################] 100%
(241/464) installing libpng                                           [######################################] 100%
(242/464) installing freetype2                                        [######################################] 100%
Optional dependencies for freetype2
    harfbuzz: Improved autohinting [pending]
(243/464) installing libfontenc                                       [######################################] 100%
(244/464) installing xorg-mkfontscale                                 [######################################] 100%
Creating X fontdir indices... done.
(245/464) installing xcb-proto                                        [######################################] 100%
(246/464) installing libxdmcp                                         [######################################] 100%
(247/464) installing libxau                                           [######################################] 100%
(248/464) installing libxcb                                           [######################################] 100%
(249/464) installing libx11                                           [######################################] 100%
(250/464) installing libxext                                          [######################################] 100%
(251/464) installing libpciaccess                                     [######################################] 100%
(252/464) installing libdrm                                           [######################################] 100%
Optional dependencies for libdrm
    cairo: needed for modetest tool [pending]
(253/464) installing libxshmfence                                     [######################################] 100%
(254/464) installing libxxf86vm                                       [######################################] 100%
(255/464) installing llvm-libs                                        [######################################] 100%
(256/464) installing lm_sensors                                       [######################################] 100%
Optional dependencies for lm_sensors
    rrdtool: for logging with sensord
    perl: for sensor detection and configuration convert [installed]
(257/464) installing spirv-tools                                      [######################################] 100%
(258/464) installing default-cursors                                  [######################################] 100%
Optional dependencies for default-cursors
    adwaita-cursors: default cursor theme
(259/464) installing wayland                                          [######################################] 100%
(260/464) installing mesa                                             [######################################] 100%
Optional dependencies for mesa
    opengl-man-pages: for the OpenGL API man pages
(261/464) installing libglvnd                                         [######################################] 100%
(262/464) installing libepoxy                                         [######################################] 100%
(263/464) installing libxfont2                                        [######################################] 100%
(264/464) installing pixman                                           [######################################] 100%
(265/464) installing xkeyboard-config                                 [######################################] 100%
(266/464) installing libxkbfile                                       [######################################] 100%
(267/464) installing xorg-xkbcomp                                     [######################################] 100%
(268/464) installing libxrender                                       [######################################] 100%
(269/464) installing libxrandr                                        [######################################] 100%
(270/464) installing xorg-setxkbmap                                   [######################################] 100%
(271/464) installing xorg-server-common                               [######################################] 100%
(272/464) installing libunwind                                        [######################################] 100%
(273/464) installing libevdev                                         [######################################] 100%
(274/464) installing libgudev                                         [######################################] 100%
(275/464) installing libwacom                                         [######################################] 100%
Optional dependencies for libwacom
    python-libevdev: for libwacom-show-stylus
    python-pyudev: for libwacom-show-stylus
(276/464) installing lua54                                            [######################################] 100%
(277/464) installing mtdev                                            [######################################] 100%
(278/464) installing libinput                                         [######################################] 100%
Optional dependencies for libinput
    libinput-tools: debug utilities
(279/464) installing xf86-input-libinput                              [######################################] 100%
(280/464) installing libxcvt                                          [######################################] 100%
(281/464) installing xorg-server                                      [######################################] 100%
>>> xorg-server has now the ability to run without root rights with
    the help of systemd-logind. xserver will fail to run if not launched
    from the same virtual terminal as was used to log in.
    Without root rights, log files will be in ~/.local/share/xorg/ directory.

    Old behavior can be restored through Xorg.wrap config file.
    See Xorg.wrap man page (man xorg.wrap).
(282/464) installing xorg-util-macros                                 [######################################] 100%
(283/464) installing xorg-server-devel                                [######################################] 100%
(284/464) installing xorg-server-src                                  [######################################] 100%
(285/464) installing xcb-util                                         [######################################] 100%
(286/464) installing xcb-util-image                                   [######################################] 100%
(287/464) installing xcb-util-renderutil                              [######################################] 100%
(288/464) installing xcb-util-wm                                      [######################################] 100%
(289/464) installing xcb-util-keysyms                                 [######################################] 100%
(290/464) installing xorg-server-xephyr                               [######################################] 100%
(291/464) installing xorg-server-xnest                                [######################################] 100%
(292/464) installing libsm                                            [######################################] 100%
(293/464) installing libxt                                            [######################################] 100%
(294/464) installing libxmu                                           [######################################] 100%
(295/464) installing xorg-xauth                                       [######################################] 100%
(296/464) installing xorg-server-xvfb                                 [######################################] 100%
(297/464) installing xorg-sessreg                                     [######################################] 100%
(298/464) installing xorg-smproxy                                     [######################################] 100%
(299/464) installing fontconfig                                       [######################################] 100%
Creating fontconfig configuration...
Rebuilding fontconfig cache...
(300/464) installing libxft                                           [######################################] 100%
(301/464) installing xorg-x11perf                                     [######################################] 100%
(302/464) installing xorg-xbacklight                                  [######################################] 100%
(303/464) installing xorg-xcmsdb                                      [######################################] 100%
(304/464) installing libxfixes                                        [######################################] 100%
(305/464) installing libxcursor                                       [######################################] 100%
(306/464) installing xorg-xcursorgen                                  [######################################] 100%
(307/464) installing libxi                                            [######################################] 100%
(308/464) installing libxtst                                          [######################################] 100%
(309/464) installing libxcomposite                                    [######################################] 100%
(310/464) installing libxinerama                                      [######################################] 100%
(311/464) installing xorg-xdpyinfo                                    [######################################] 100%
(312/464) installing xorg-xdriinfo                                    [######################################] 100%
(313/464) installing xorg-xev                                         [######################################] 100%
(314/464) installing xorg-xgamma                                      [######################################] 100%
(315/464) installing xorg-xhost                                       [######################################] 100%
(316/464) installing xorg-xrandr                                      [######################################] 100%
(317/464) installing xorg-xinput                                      [######################################] 100%
(318/464) installing xorg-xkbevd                                      [######################################] 100%
(319/464) installing libxpm                                           [######################################] 100%
(320/464) installing libxaw                                           [######################################] 100%
(321/464) installing xorg-xkbutils                                    [######################################] 100%
(322/464) installing xorg-xkill                                       [######################################] 100%
(323/464) installing xorg-xlsatoms                                    [######################################] 100%
(324/464) installing xorg-xlsclients                                  [######################################] 100%
(325/464) installing xorg-xmodmap                                     [######################################] 100%
(326/464) installing xorg-xpr                                         [######################################] 100%
(327/464) installing xorg-xprop                                       [######################################] 100%
(328/464) installing xorg-xrdb                                        [######################################] 100%
Optional dependencies for xorg-xrdb
    gcc: for preprocessing
    mcpp: a lightweight alternative for preprocessing
(329/464) installing xorg-xrefresh                                    [######################################] 100%
(330/464) installing xorg-xset                                        [######################################] 100%
(331/464) installing xorg-xsetroot                                    [######################################] 100%
(332/464) installing libxv                                            [######################################] 100%
(333/464) installing xorg-xvinfo                                      [######################################] 100%
(334/464) installing libei                                            [######################################] 100%
(335/464) installing cairo                                            [######################################] 100%
(336/464) installing fribidi                                          [######################################] 100%
(337/464) installing graphite                                         [######################################] 100%
Optional dependencies for graphite
    graphite-docs: Documentation
(338/464) installing harfbuzz                                         [######################################] 100%
Optional dependencies for harfbuzz
    harfbuzz-utils: utilities
(339/464) installing libdatrie                                        [######################################] 100%
(340/464) installing libthai                                          [######################################] 100%
(341/464) installing pango                                            [######################################] 100%
(342/464) installing libdecor                                         [######################################] 100%
Optional dependencies for libdecor
    gtk3: gtk3 support
(343/464) installing xorg-xwayland                                    [######################################] 100%
(344/464) installing xorg-xwd                                         [######################################] 100%
(345/464) installing xorg-xwininfo                                    [######################################] 100%
(346/464) installing xorg-xwud                                        [######################################] 100%
(347/464) installing xorg-xinit                                       [######################################] 100%
Optional dependencies for xorg-xinit
    xorg-twm
    xterm
(348/464) installing dhcpcd                                           [######################################] 100%
Optional dependencies for dhcpcd
    openresolv: resolvconf support [installed]
(349/464) installing dnsmasq                                          [######################################] 100%
(350/464) installing ell                                              [######################################] 100%
(351/464) installing iwd                                              [######################################] 100%
Optional dependencies for iwd
    qrencode: for displaying QR code after DPP is started
(352/464) installing wireless_tools                                   [######################################] 100%
(353/464) installing mpdecimal                                        [######################################] 100%
(354/464) installing python                                           [######################################] 100%
Optional dependencies for python
    python-setuptools: for building Python packages using tooling that is usually bundled with Python [pending]
    python-pip: for installing Python packages using tooling that is usually bundled with Python [pending]
    python-pipx: for installing Python software not packaged on Arch Linux
    sqlite: for a default database integration [installed]
    xz: for lzma [installed]
    tk: for tkinter
(355/464) installing python-attrs                                     [######################################] 100%
(356/464) installing python-pycparser                                 [######################################] 100%
(357/464) installing python-cffi                                      [######################################] 100%
Optional dependencies for python-cffi
    python-setuptools: "limited api" version checking in cffi.setuptools_ext [pending]
(358/464) installing python-cryptography                              [######################################] 100%
(359/464) installing python-filelock                                  [######################################] 100%
(360/464) installing python-packaging                                 [######################################] 100%
(361/464) installing python-wheel                                     [######################################] 100%
Optional dependencies for python-wheel
    python-keyring: for wheel.signatures
    python-xdg: for wheel.signatures
    python-setuptools: for legacy bdist_wheel subcommand [pending]
(362/464) installing python-pip                                       [######################################] 100%
(363/464) installing python-distlib                                   [######################################] 100%
(364/464) installing python-platformdirs                              [######################################] 100%
(365/464) installing python-python-discovery                          [######################################] 100%
(366/464) installing python-virtualenv                                [######################################] 100%
(367/464) installing python-more-itertools                            [######################################] 100%
(368/464) installing python-jaraco.functools                          [######################################] 100%
(369/464) installing python-jaraco.context                            [######################################] 100%
(370/464) installing python-autocommand                               [######################################] 100%
(371/464) installing python-jaraco.text                               [######################################] 100%
Optional dependencies for python-jaraco.text
    python-inflect: for show-newlines script
(372/464) installing python-jaraco.collections                        [######################################] 100%
(373/464) installing python-typing_extensions                         [######################################] 100%
(374/464) installing python-pkg_resources                             [######################################] 100%
(375/464) installing python-setuptools                                [######################################] 100%
(376/464) installing alsa-topology-conf                               [######################################] 100%
(377/464) installing alsa-ucm-conf                                    [######################################] 100%
(378/464) installing alsa-lib                                         [######################################] 100%
(379/464) installing fftw                                             [######################################] 100%
Optional dependencies for fftw
    fftw-openmpi: for OpenMPI integration
(380/464) installing libsamplerate                                    [######################################] 100%
(381/464) installing alsa-utils                                       [######################################] 100%
(382/464) installing libasyncns                                       [######################################] 100%
(383/464) installing libogg                                           [######################################] 100%
(384/464) installing flac                                             [######################################] 100%
(385/464) installing mpg123                                           [######################################] 100%
Optional dependencies for mpg123
    sdl2: for sdl audio support
    jack: for jack audio support
    libpulse: for pulse audio support [pending]
    perl: for conplay [installed]
(386/464) installing lame                                             [######################################] 100%
(387/464) installing libvorbis                                        [######################################] 100%
(388/464) installing opus                                             [######################################] 100%
(389/464) installing libsndfile                                       [######################################] 100%
Optional dependencies for libsndfile
    alsa-lib: for sndfile-play [installed]
(390/464) installing libpulse                                         [######################################] 100%
Optional dependencies for libpulse
    pulse-native-provider: PulseAudio backend [pending]
(391/464) installing libtool                                          [######################################] 100%
(392/464) installing libsoxr                                          [######################################] 100%
(393/464) installing orc                                              [######################################] 100%
(394/464) installing rtkit                                            [######################################] 100%
(395/464) installing speexdsp                                         [######################################] 100%
(396/464) installing tdb                                              [######################################] 100%
Optional dependencies for tdb
    python: for python bindings [installed]
(397/464) installing gtest                                            [######################################] 100%
Optional dependencies for gtest
    python: gmock generator [installed]
(398/464) installing abseil-cpp                                       [######################################] 100%
(399/464) installing webrtc-audio-processing-1                        [######################################] 100%
(400/464) installing pulseaudio                                       [######################################] 100%
Created symlink '/etc/systemd/user/sockets.target.wants/pulseaudio.socket' → '/usr/lib/systemd/user/pulseaudio.socket'.
Optional dependencies for pulseaudio
    pulseaudio-alsa: ALSA configuration (recommended)
    pulseaudio-bluetooth: Bluetooth support
    pulseaudio-equalizer: Graphical equalizer
    pulseaudio-jack: Jack support
    pulseaudio-lirc: IR (lirc) support
    pulseaudio-rtp: RTP and RAOP support
    pulseaudio-zeroconf: Zeroconf support
(401/464) installing pcaudiolib                                       [######################################] 100%
(402/464) installing libsonic                                         [######################################] 100%
(403/464) installing espeak-ng                                        [######################################] 100%
(404/464) installing bluez                                            [######################################] 100%
(405/464) installing confuse                                          [######################################] 100%
(406/464) installing libftdi                                          [######################################] 100%
Optional dependencies for libftdi
    python: library bindings [installed]
(407/464) installing flashrom                                         [######################################] 100%
Optional dependencies for flashrom
    dmidecode: for SMBIOS/DMI table decoder support [pending]
(408/464) installing fwupd-efi                                        [######################################] 100%
(409/464) installing hicolor-icon-theme                               [######################################] 100%
(410/464) installing json-glib                                        [######################################] 100%
(411/464) installing libcbor                                          [######################################] 100%
(412/464) installing libjcat                                          [######################################] 100%
(413/464) installing libmbim                                          [######################################] 100%
(414/464) installing libqrtr-glib                                     [######################################] 100%
(415/464) installing libqmi                                           [######################################] 100%
(416/464) installing libstemmer                                       [######################################] 100%
(417/464) installing libxmlb                                          [######################################] 100%
(418/464) installing avahi                                            [######################################] 100%
Optional dependencies for avahi
    gtk3: avahi-discover, avahi-discover-standalone, bshell, bssh, bvnc
    libevent: libevent bindings [installed]
    nss-mdns: NSS support for mDNS
    python-dbus: avahi-bookmarks, avahi-discover
    python-gobject: avahi-bookmarks, avahi-discover
    python-twisted: avahi-bookmarks
(419/464) installing dconf                                            [######################################] 100%
(420/464) installing gsettings-system-schemas                         [######################################] 100%
(421/464) installing libproxy                                         [######################################] 100%
(422/464) installing glib-networking                                  [######################################] 100%
(423/464) installing libsoup3                                         [######################################] 100%
Optional dependencies for libsoup3
    samba: Windows Domain SSO
(424/464) installing passim                                           [######################################] 100%
(425/464) installing protobuf                                         [######################################] 100%
(426/464) installing protobuf-c                                       [######################################] 100%
(427/464) installing shared-mime-info                                 [######################################] 100%
(428/464) installing fwupd                                            [######################################] 100%
Optional dependencies for fwupd
    python-dbus: Firmware packaging tools
    python-gobject: Firmware packaging tools
    udisks2: UEFI firmware upgrade support
(429/464) installing dmidecode                                        [######################################] 100%
(430/464) installing libx86emu                                        [######################################] 100%
(431/464) installing perl-class-inspector                             [######################################] 100%
(432/464) installing perl-file-sharedir                               [######################################] 100%
(433/464) installing perl-encode-locale                               [######################################] 100%
(434/464) installing perl-timedate                                    [######################################] 100%
(435/464) installing perl-http-date                                   [######################################] 100%
(436/464) installing perl-file-listing                                [######################################] 100%
(437/464) installing perl-html-tagset                                 [######################################] 100%
(438/464) installing perl-clone                                       [######################################] 100%
(439/464) installing perl-io-html                                     [######################################] 100%
(440/464) installing perl-lwp-mediatypes                              [######################################] 100%
(441/464) installing perl-uri                                         [######################################] 100%
(442/464) installing perl-http-message                                [######################################] 100%
(443/464) installing perl-html-parser                                 [######################################] 100%
(444/464) installing perl-http-cookies                                [######################################] 100%
(445/464) installing perl-http-daemon                                 [######################################] 100%
(446/464) installing perl-http-cookiejar                              [######################################] 100%
(447/464) installing perl-http-negotiate                              [######################################] 100%
(448/464) installing perl-net-http                                    [######################################] 100%
(449/464) installing perl-try-tiny                                    [######################################] 100%
(450/464) installing perl-www-robotrules                              [######################################] 100%
(451/464) installing perl-libwww                                      [######################################] 100%
Optional dependencies for perl-libwww
    perl-lwp-protocol-https: for https:// url schemes
(452/464) installing perl-xml-parser                                  [######################################] 100%
(453/464) installing perl-xml-writer                                  [######################################] 100%
(454/464) installing hwinfo                                           [######################################] 100%
(455/464) installing lshw                                             [######################################] 100%
Optional dependencies for lshw
    gtk3
(456/464) installing runc                                             [######################################] 100%
Optional dependencies for runc
    criu: checkpoint support
(457/464) installing containerd                                       [######################################] 100%
(458/464) installing docker                                           [######################################] 100%
Optional dependencies for docker
    btrfs-progs: btrfs backend support [installed]
    pigz: parallel gzip compressor support
    docker-buildx: extended build capabilities
(459/464) installing docker-compose                                   [######################################] 100%
(460/464) installing perl-error                                       [######################################] 100%
(461/464) installing perl-mailtools                                   [######################################] 100%
(462/464) installing zlib-ng                                          [######################################] 100%
(463/464) installing git                                              [######################################] 100%
Optional dependencies for git
    git-zsh-completion: upstream zsh completion
    tk: gitk and git gui
    openssh: ssh transport and crypto [installed]
    man: show help with `git command --help` [installed]
    perl-libwww: git svn [installed]
    perl-term-readkey: git svn and interactive.singlekey setting
    perl-io-socket-ssl: git send-email TLS support
    perl-authen-sasl: git send-email TLS support
    perl-cgi: gitweb (web interface) support
    python: git svn & git p4 [installed]
    subversion: git svn
    org.freedesktop.secrets: keyring credential helper
    libsecret: libsecret credential helper [installed]
    less: the default pager for git [installed]
(464/464) installing wget                                             [######################################] 100%
Optional dependencies for wget
    ca-certificates: HTTPS downloads [installed]
:: Running post-transaction hooks...
( 1/21) Creating system user accounts...
Creating group 'docker' with GID 970.
Creating group 'polkitd' with GID 102.
Creating group 'alpm' with GID 969.
Creating user 'alpm' (Arch Linux Package Management) with UID 969 and GID 969.
Creating group 'avahi' with GID 968.
Creating user 'avahi' (Avahi mDNS/DNS-SD daemon) with UID 968 and GID 968.
Creating group 'dhcpcd' with GID 967.
Creating user 'dhcpcd' (dhcpcd privilege separation) with UID 967 and GID 967.
Creating group 'dnsmasq' with GID 966.
Creating user 'dnsmasq' (dnsmasq daemon) with UID 966 and GID 966.
Creating group 'fwupd' with GID 965.
Creating user 'fwupd' (Firmware update daemon) with UID 965 and GID 965.
Creating group 'git' with GID 964.
Creating user 'git' (git daemon user) with UID 964 and GID 964.
Creating group '_talkd' with GID 963.
Creating user '_talkd' (User for legacy talkd server) with UID 963 and GID 963.
Creating group 'passim' with GID 962.
Creating user 'passim' (Local Caching Server) with UID 962 and GID 962.
Creating group 'pcscd' with GID 961.
Creating user 'pcscd' (PC/SC Smart Card Daemon) with UID 961 and GID 961.
Creating user 'polkitd' (User for polkitd) with UID 102 and GID 102.
Creating group 'rpc' with GID 32.
Creating user 'rpc' (Rpcbind Daemon) with UID 32 and GID 32.
Creating group 'rpcuser' with GID 34.
Creating user 'rpcuser' (RPC Service User) with UID 34 and GID 34.
Creating group 'rtkit' with GID 960.
Creating user 'rtkit' (RealtimeKit) with UID 960 and GID 960.
( 2/21) Creating temporary files...
( 3/21) Updating journal message catalog...
( 4/21) Updating udev hardware database...
( 5/21) Applying kernel sysctl settings...
  Skipped: Running in chroot.
( 6/21) Reloading system manager configuration...
  Skipped: Running in chroot.
( 7/21) Reloading user manager configuration...
  Skipped: Running in chroot.
( 8/21) Updating the MIME type database...
( 9/21) Reloading device manager configuration...
  Skipped: Running in chroot.
(10/21) Arming ConditionNeedsUpdate...
(11/21) Updating fontconfig configuration...
(12/21) Rebuilding certificate stores...
(13/21) Updating module dependencies...
(14/21) Updating linux initcpios...
==> Building image from preset: /etc/mkinitcpio.d/linux-lts.preset: 'default'
==> Using default configuration file: '/etc/mkinitcpio.conf'
  -> -k /boot/vmlinuz-linux-lts -g /boot/initramfs-linux-lts.img
==> Starting build: '6.18.34-1-lts'
  -> Running build hook: [base]
  -> Running build hook: [systemd]
  -> Running build hook: [autodetect]
==> ERROR: failed to detect root filesystem
  -> Running build hook: [microcode]
  -> Running build hook: [modconf]
  -> Running build hook: [kms]
==> WARNING: Possibly missing firmware for module: 'nouveau'
  -> Running build hook: [keyboard]
  -> Running build hook: [sd-vconsole]
==> WARNING: sd-vconsole: "/etc/vconsole.conf" not found, will use default values
  -> Running build hook: [block]
  -> Running build hook: [filesystems]
  -> Running build hook: [fsck]
==> Generating module dependencies
==> Creating zstd-compressed initcpio image: '/boot/initramfs-linux-lts.img'
  -> Early uncompressed CPIO image generation successful
==> Initcpio image generation successful
(15/21) Reloading system bus configuration...
  Skipped: Running in chroot.
(16/21) Checking for old perl modules...
(17/21) Updating fontconfig cache...
(18/21) Updating GIO module cache...
(19/21) Compiling GSettings XML schema files...
(20/21) Updating the info directory file...
(21/21) Updating X fontdir indices...
[mkarchiso] INFO: Done! Packages installed successfully.
[mkarchiso] INFO: Creating version files...
[mkarchiso] INFO: Done!
[mkarchiso] INFO: Running customize_airootfs.sh in '/tmp/jarvis-iso-build-69948/x86_64/airootfs' chroot...
[mkarchiso] WARNING: customize_airootfs.sh is deprecated! Support for it will be removed in a future archiso version.
==> WARNING: /tmp/jarvis-iso-build-69948/x86_64/airootfs is not a mountpoint. This may have undesirable side effects.
JARVIS OS v2.0.0 - Customizing AI root filesystem
Generating locales...
  en_US.UTF-8... done
Generation complete.
useradd: warning: the home directory /opt/jarvis already exists.
useradd: Not copying any file from skel directory into it.
Created symlink '/etc/systemd/system/jarvis.target.wants/jarvis-api.service' → '/etc/systemd/system/jarvis-api.service'.
Created symlink '/etc/systemd/system/jarvis.target.wants/jarvis-router.service' → '/etc/systemd/system/jarvis-router.service'.
Created symlink '/etc/systemd/system/jarvis.target.wants/jarvis-executor.service' → '/etc/systemd/system/jarvis-executor.service'.
Created symlink '/etc/systemd/system/jarvis.target.wants/jarvis-memory.service' → '/etc/systemd/system/jarvis-memory.service'.
Created symlink '/etc/systemd/system/jarvis.target.wants/jarvis-hal.service' → '/etc/systemd/system/jarvis-hal.service'.
Created symlink '/etc/systemd/system/dbus-org.freedesktop.resolve1.service' → '/usr/lib/systemd/system/systemd-resolved.service'.
Created symlink '/etc/systemd/system/sysinit.target.wants/systemd-resolved.service' → '/usr/lib/systemd/system/systemd-resolved.service'.
Created symlink '/etc/systemd/system/sockets.target.wants/systemd-resolved-varlink.socket' → '/usr/lib/systemd/system/systemd-resolved-varlink.socket'.
Created symlink '/etc/systemd/system/sockets.target.wants/systemd-resolved-monitor.socket' → '/usr/lib/systemd/system/systemd-resolved-monitor.socket'.
Created symlink '/etc/systemd/system/dbus-org.freedesktop.timesync1.service' → '/usr/lib/systemd/system/systemd-timesyncd.service'.
Created symlink '/etc/systemd/system/sysinit.target.wants/systemd-timesyncd.service' → '/usr/lib/systemd/system/systemd-timesyncd.service'.
Created symlink '/etc/systemd/system/multi-user.target.wants/docker.service' → '/usr/lib/systemd/system/docker.service'.
/root/customize_airootfs.sh: line 42: /etc/security/limits.d/99-jarvis.conf: No such file or directory
[william@LServer3 JARVIS-OS]$ 
