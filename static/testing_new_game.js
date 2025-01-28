point_types = ["terraforming points", "milestones", "awards", "trees", "city points", "card points"]

function ask_for_points(players, point_type, paragraph) {

        document.getElementById(paragraph).innerHTML =" <br>What is each player's "+ point_type +" score?";

        terraformingPointsDiv = document.getElementById(point_type)
        terraformingPointsDiv.innerHTML = " ";

        for (let i = 1; i <players+1; i++ ) {
            var newTerraField = document.createElement('input');
            newTerraField.type = 'number';
            newTerraField.name = point_type;
            newTerraField.max = 500;
            newTerraField.min = 20;

            const paragraph = document.createElement("a");
            const pText = document.createTextNode("Player "+ i + " ");
            paragraph.appendChild(pText);


            terraformingPointsDiv.appendChild(paragraph);
            terraformingPointsDiv.appendChild(newTerraField);
            var breakLine = document.createElement("br");
            terraformingPointsDiv.appendChild(breakLine);

        }


}


document.getElementById('playerButton').addEventListener('click', function() {

    players = Number(document.getElementById('players').value);

    if (players == 1) {
        document.getElementById("p1").innerHTML = "<br> Great, you went solo!";
    }  else {

        document.getElementById("p1").innerHTML = "<br> Okay, I have registered "
        + players + " players."

        ask_for_points(players, point_types[0], "p2")

        ask_for_points(players, point_types[1], "p3")



    }
});