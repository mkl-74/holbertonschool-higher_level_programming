document.getElementById('add_item').onclick = function() {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('ul.my_list').appendChild(li);
};
