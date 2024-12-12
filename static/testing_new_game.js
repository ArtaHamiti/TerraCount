document.getElementById('addButton').addEventListener('click', function() {
  // Create a new div element to hold the new input field
  var newFormGroup = document.createElement('div');
  newFormGroup.className = 'form-group';

  // Create a new input element
  var newField = document.createElement('input');
  newField.type = 'text';
  newField.name = 'dynamicField';

  // Append the new input element to the new div
  newFormGroup.appendChild(newField);

  // Append the new div to the form
  document.getElementById('dynamicForm').appendChild(newFormGroup);
});