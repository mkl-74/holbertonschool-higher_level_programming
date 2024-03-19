sudo service mysql start
sudo mysql-server
USE mysql;
UPDATE user SET authentication_string=PASSWORD('votre_nouveau_mot_de_passe') WHERE User='root';
UPDATE user SET plugin='mysql_native_password' WHERE User='root';
FLUSH PRIVILEGES;
