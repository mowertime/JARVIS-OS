#!/bin/bash
set -euo pipefail

echo "JARVIS OS v2.0.0 - Customizing AI root filesystem"

# Set locale
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf

# Set hostname
echo "jarvis-os" > /etc/hostname
cat > /etc/hosts << 'EOF'
127.0.0.1   localhost
::1         localhost
127.0.1.1   jarvis-os.localdomain jarvis-os
EOF

# Create jarvis user
useradd -r -m -d /opt/jarvis -s /usr/bin/nologin jarvis
usermod -aG audio,video,optical,storage,docker jarvis

# Set up systemd services
systemctl enable jarvis.target
systemctl enable jarvis-api jarvis-router jarvis-executor jarvis-memory jarvis-hal
systemctl enable systemd-resolved
systemctl enable systemd-timesyncd
systemctl enable docker

# Configure sysctl for JARVIS
cat > /etc/sysctl.d/99-jarvis.conf << 'EOF'
# JARVIS OS performance tuning
kernel.nmi_watchdog=0
kernel.sched_autogroup_enabled=0
vm.swappiness=10
vm.vfs_cache_pressure=50
net.core.somaxconn=65535
net.ipv4.tcp_fastopen=3
EOF

# Configure limits
mkdir -p /etc/security/limits.d
cat > /etc/security/limits.d/99-jarvis.conf << 'EOF'
jarvis soft nofile 65535
jarvis hard nofile 65535
jarvis soft nproc 32768
jarvis hard nproc 32768
EOF

# Set up JARVIS directories
mkdir -p /opt/jarvis/{backend,frontend,data,logs,etc}
chown -R jarvis:jarvis /opt/jarvis

# Clean up
rm -f /var/cache/pacman/pkg/*.pkg.tar.zst
rm -rf /root/.cache
echo "JARVIS OS customization complete"
