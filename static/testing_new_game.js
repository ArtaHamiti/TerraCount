point_types = ["terraforming points", "milestones", "awards", "trees", "city points", "card points"]

function ask_for_points(players, point_type, iter) {

        para = document.getElementById("p2")
        para.innerHTML =" <br>What is each player's "+ point_type +" score?";
        PointsDiv = document.getElementById("points")

        for (let i = 1; i <players+1; i++ ) {
            var newTerraField = document.createElement('input');
            newTerraField.type = 'number';
            newTerraField.name = point_type;
            newTerraField.max = 500;
            newTerraField.min = 20;

            const paragraph = document.createElement("a");
            const pText = document.createTextNode("Player "+ i + " ");
            paragraph.appendChild(pText);


            PointsDiv.appendChild(paragraph);
            PointsDiv.appendChild(newTerraField);
            var breakLine = document.createElement("br");
            PointsDiv.appendChild(breakLine);

        }

        var x = document.createElement("INPUT");
        x.setAttribute("type", "submit");
        PointsDiv.appendChild(x);
        x.onclick = function() {
        PointsDiv.innerHTML = " ";
        para.innerHTML = " ";
        iter +=1
        }



}


document.getElementById('playerButton').addEventListener('click', function() {

    players = Number(document.getElementById('players').value);

    if (players == 1) {
        document.getElementById("p1").innerHTML = "<br> Great, you went solo!";
    }  else {

        document.getElementById("p1").innerHTML = "<br> Okay, I have registered "
        + players + " players."

        var iteration = 0


        ask_for_points(players, point_types[iteration], iteration)
        




    }
});