function test(){
    alert("Hi ok")
    return false
};

function addFields(){
    // Generate a dynamic number of inputs
    var number = document.getElementById("players").value;
    // Get the element where the inputs will be added to
    alert("third")
    var container = document.getElementById("container");
    // Remove every children it had before
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){
        // Append a node with a random text
        container.appendChild(document.createTextNode("Member " + (i+1)));
        // Create an <input> element, set its type and name attributes
        var input = document.createElement("input");
        input.type = "text";
        input.name = "member" + i;
        container.appendChild(input);
        // Append a line break
        container.appendChild(document.createElement("br"));
    }
    return false
    };