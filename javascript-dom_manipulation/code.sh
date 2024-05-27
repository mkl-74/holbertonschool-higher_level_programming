#!/bin/bash

# Configuration du projet
repo_name="holbertonschool-higher_level_programming"
dir_name="javascript-dom_manipulation"

# Création des répertoires
mkdir -p $repo_name/$dir_name
cd $repo_name/$dir_name

# Création du fichier README.md
cat <<EOL > README.md
# JavaScript DOM Manipulation
This project contains scripts to manipulate the DOM using JavaScript.
EOL

# Script 0
cat <<EOL > 0-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelector('header').style.color = '#FF0000';
});
EOL

cat <<EOL > 0-main.html
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

# Script 1
cat <<EOL > 1-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('red_header').onclick = function() {
    document.querySelector('header').style.color = '#FF0000';
  };
});
EOL

cat <<EOL > 1-main.html
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

# Script 2
cat <<EOL > 2-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('red_header').onclick = function() {
    document.querySelector('header').classList.add('red');
  };
});
EOL

cat <<EOL > 2-main.html
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

# Script 3
cat <<EOL > 3-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('toggle_header').onclick = function() {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  };
});
EOL

cat <<EOL > 3-main.html
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

# Script 4
cat <<EOL > 4-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('add_item').onclick = function() {
    const ul = document.querySelector('.my_list');
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  };
});
EOL

cat <<EOL > 4-main.html
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

# Script 5
cat <<EOL > 5-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('update_header').onclick = function() {
    document.querySelector('header').textContent = 'New Header!!!';
  };
});
EOL

cat <<EOL > 5-main.html
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

# Script 6
cat <<EOL > 6-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      document.getElementById('character').textContent = data.name;
    });
});
EOL

cat <<EOL > 6-main.html
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

# Script 7
cat <<EOL > 7-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      const ul = document.getElementById('list_movies');
      movies.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        ul.appendChild(li);
      });
    });
});
EOL

cat <<EOL > 7-main.html
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

# Script 8
cat <<EOL > 8-script.js
document.addEventListener('DOMContentLoaded', (event) => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    });
});
EOL

cat <<EOL > 8-main.html
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

# Message de succès
echo "All files have been created successfully in $repo_name/$dir_name"
