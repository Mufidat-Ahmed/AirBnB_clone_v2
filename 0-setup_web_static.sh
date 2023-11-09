#!/usr/bin/env bash
#on some webstatic business

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This is a test file oo" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start

# Install Nginx if not already installed
if ! dpkg --get-selections | grep -q nginx; then
    sudo apt update && sudo apt install nginx -y
fi

# Create necessary directories
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/current
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file for testing
sudo echo "<html><body>This is a test file oo</body></html>" > /data/web_static/releases/test/index.html

# Create a symbolic link to the test folder
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Set ownership of the /data directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration to serve content from /data/web_static/current/ to hbnb_static
sudo cat > /etc/nginx/sites-available/hbnb_static <<EOF
 EOF
server {
    listen 80;
    server_name anealx.tech;

    location /hbnb_static {
	alias /data/web_static/current/;
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/hnbn_static

# Restart Nginx to apply the new configuration
sudo systemctl restart nginx
EOF
