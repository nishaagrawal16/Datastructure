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
        var xhttp1 = new XMLHttpRequest();
        xhttp1.open("POST", "http://127.0.0.1:8082/employe_data", true);
        xhttp1.onreadystatechange = function() {
          console.log('POST onreadystatechange');
          if (xhttp1.readyState == 4 && xhttp1.status == 200) {
            console.log('this.responseText: '+ xhttp1.responseText);
            document.getElementById("demo").innerHTML = xhttp1.responseText;
          }
        };
        // xhttp1.setRequestHeader("Content-Type", "application/json");
        //xhttp1.setRequestHeader("Access-Control-Allow-Origin", "*");
        // Converting JSON data to string 
        var data = JSON.stringify({ "name": "nisha", "email": "nisha.agrawal1@gmail.com" }); 
        console.log('data: ', data);
        // Sending data with the request 
        xhttp1.send(data);       
      }
};
s = new sample();
//s.sendPostRequest();
s.sendRequest();


