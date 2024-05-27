#!/bin/bash

# 1. Installation et démarrage de MySQL
echo "Installing MySQL server..."
sudo apt-get update
sudo apt-get install -y mysql-server

echo "Starting MySQL server..."
sudo systemctl start mysql
sudo systemctl enable mysql

# 2. Configuration de MySQL
echo "Configuring MySQL..."
sudo mysql -e "CREATE USER 'mkl'@'localhost' IDENTIFIED BY 'mkl';"
sudo mysql -e "CREATE DATABASE data_light_life;"
sudo mysql -e "GRANT ALL PRIVILEGES ON data_light_life.* TO 'mkl'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"

# 3. Créer la table users
echo "Creating users table..."
sudo mysql -u mkl -pmkl -e "
USE data_light_life;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);
"

# 4. Création des fichiers et dossiers nécessaires
echo "Creating project directories and files..."
mkdir -p javascript-dom_manipulation
cd javascript-dom_manipulation

# Création des scripts JavaScript
cat <<EOL >0-script.js
document.querySelector('header').style.color = '#FF0000';
EOL

cat <<EOL >1-script.js
document.getElementById('red_header').onclick = function() {
  document.querySelector('header').style.color = '#FF0000';
};
EOL

cat <<EOL >2-script.js
document.getElementById('red_header').onclick = function() {
  document.querySelector('header').classList.add('red');
};
EOL

cat <<EOL >3-script.js
document.getElementById('toggle_header').onclick = function() {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
};
EOL

cat <<EOL >4-script.js
document.getElementById('add_item').onclick = function() {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('ul.my_list').appendChild(li);
};
EOL

cat <<EOL >5-script.js
document.getElementById('update_header').onclick = function() {
  document.querySelector('header').textContent = 'New Header!!!';
};
EOL

cat <<EOL >6-script.js
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  });
EOL

cat <<EOL >7-script.js
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const ul = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      ul.appendChild(li);
    });
  });
EOL

cat <<EOL >8-script.js
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())
  .then(data => {
    document.getElementById('hello').textContent = data.hello;
  });
EOL

# Création des fichiers HTML
cat <<EOL >0-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >1-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >2-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >3-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >4-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >5-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >6-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >7-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
EOL

cat <<EOL >8-main.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
EOL

echo "All files have been created successfully."

# Open VS Code
code .

echo "VS Code has been opened with all the project files."
