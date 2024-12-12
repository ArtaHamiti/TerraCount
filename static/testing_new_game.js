document.getElementById('addButton').addEventListener('click', function() {
  // Create a new div element to hold the new input field
  var newFormGroup = document.createElement('div');
  newFormGroup.className = 'form-group';

  players = document.getElementById('players').value;
  console.log("playerssss:", players)

  for (let i = 0; i <players; i++ ) {
    // Create a new input element
    var newField = document.createElement('input');
    newField.type = 'text';
    newField.name = 'dynamicField';

    console.log("iteration:", i)
    // Append the new input element to the new div
    newFormGroup.appendChild(newField);

    // Append the new div to the form
    document.getElementById('dynamicForm').appendChild(newFormGroup);
  }

});