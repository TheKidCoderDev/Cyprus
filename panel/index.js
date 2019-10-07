function addDomain() {
  var ip = document.getElementById("ip").value;
  var domain = document.getElementById("domain").value;
  const http = new XMLHttpRequest();
  const url = 'http://admin.cyp/api/newDomain';
  var params = 'ip='+ip+'&domain='+domain;
  http.open('POST', url, true);
  console.log(params)

  //Send the proper header information along with the request
  http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  http.send(params);
}

function delDomain() {
  var domain = document.getElementById("remdomain").value;
  const http = new XMLHttpRequest();
  const url = 'http://admin.cyp/api/delDomain';
  var params = 'domain='+domain;
  http.open('POST', url, true);
  console.log(params)

//Send the proper header information along with the request
http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
http.send(params);
}

function restart() {
  const http = new XMLHttpRequest();
  const url = 'http://admin.cyp/api/restart';
  http.open('get', url, true);

//Send the proper header information along with the request
http.send();
}
