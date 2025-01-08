
function ask_for_terrapoints(players) {

        terraformingPointsDiv = document.getElementById("terraforming points")
        terraformingPointsDiv.innerHTML = " ";

        for (let i = 1; i <players+1; i++ ) {
            var newTerraField = document.createElement('input');
            newTerraField.type = 'number';
            newTerraField.name = 'terrapoints field';
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