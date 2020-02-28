class sample {
    sendRequest() {
        var xhttp = new XMLHttpRequest();
        console.log('hello');
        xhttp.open("GET", "http://127.0.0.1:8082", true);
        xhttp.onreadystatechange = function() {
          console.log('onreadystatechange');
          if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log('this.responseText: '+ xhttp.responseText);
            document.getElementById("demo").innerHTML = xhttp.responseText;
          }
        };
        xhttp.send();
        var xhttp = new XMLHttpRequest();
        xhttp.open("GET", "http://127.0.0.1:8082/user_info", true);
        xhttp.onreadystatechange = function() {
          console.log('onreadystatechange');
          if (xhttp.readyState == 4 && xhttp.status == 200) {
            console.log('this.responseText: '+ xhttp.responseText);
            document.getElementById("demo").innerHTML = xhttp.responseText;
          }
        };
        xhttp.send();

      }
};
s = new sample();
s.sendRequest()

