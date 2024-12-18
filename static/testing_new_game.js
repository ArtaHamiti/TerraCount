document.getElementById('playerButton').addEventListener('click', function() {

    players = document.getElementById('players').value;

    if (players == 1) {
        document.getElementById("second p").innerHTML = "<br> Great, you went solo!";
    }  else {
        document.getElementById("second p").innerHTML = "<br> Okay, I have registered "
        + players + " players. <br> <br>What is each player's terraforming points score?";

        terraformingPointsDiv = document.getElementById("terraforming points")
        terraformingPointsDiv.innerHTML = " ";

        for (let i = 0; i <players; i++ ) {
            var newTerraField = document.createElement('input');
            newTerraField.type = 'number';
            newTerraField.name = 'terrapoints field';
            newTerraField.max = 500;
            newTerraField.min = 20;
            //newTerraField.defaultValue = 3;

            terraformingPointsDiv.appendChild(newTerraField);

        document.getElementById('dynamicForm').appendChild(terraformingPointsDiv);



        }
    }
});