document.getElementById('addButton').addEventListener('click', function() {

    players = document.getElementById('players').value;
    console.log("Players:", players)

    if (players == 1) {
        document.write("Great, you went solo!");
        console.log("if statement DONE");
    }  else {
        document.write("Okay, I have registered ", players, " players!");

        // Create a new div element to hold the new input field
        var newFormGroup = document.createElement('div');
        newFormGroup.className = 'form-group';

        for (let i = 0; i <players; i++ ) {
            console.log("check number 1")
            // Create a new input element
            /*
            var newField = document.createElement('input');
            newField.type = 'text';
            newField.name = 'dynamicField';

            console.log("iteration:", i)
            // Append the new input element to the new div
            newFormGroup.appendChild(newField);

            // Append the new div to the form
            document.getElementById('dynamicForm').appendChild(newFormGroup); */
        }
    }
});