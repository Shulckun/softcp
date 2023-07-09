    // Current date - http://stackoverflow.com/a/4929629/412329
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
        dd='0'+dd
        } 

    if(mm<10) {
        mm='0'+mm
        } 

    today = yyyy+'-'+mm+'-'+dd;


    function saveFormAsTextFile()
        // Based on https://thiscouldbebetter.wordpress.com/2012/12/18/loading-editing-and-saving-a-text-file-in-html5-using-javascrip/
        {
        var textToSave =
          'first name: ' + document.getElementById('first name').value + '\n' + // =first name
          'last name: ' + document.getElementById('last name').value + '\n' + // =last name
          'date: ' + today + '\n' + // =date - automatically puts today's date =todo: fix bug allowing going over 60 seconds, i.e. 61 seconds
          'gender: ' + document.getElementById('gender').value + '\n' + // =gender - select menu
          'gmail: ' + document.getElementById('gmail').value.replace(/,\s/g, "\n- ") + '\n' + 
            // =gmail
          'age: ' + document.getElementById('age').value // =age;
            // The replace() bit above converts 'tag,tag' to '- tag\n- tag\n' with regular expressions
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp

        var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
        var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
        var fileNameToSaveAs = document.getElementById("filename").value;

        var downloadLink = document.createElement("a");
        downloadLink.download = fileNameToSaveAs;
        downloadLink.innerHTML = "Download File";
        downloadLink.href = textToSaveAsURL;
        downloadLink.onclick = destroyClickedElement;
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);

        downloadLink.click();
        }

    function destroyClickedElement(event)
        {
        document.body.removeChild(event.target);
        }