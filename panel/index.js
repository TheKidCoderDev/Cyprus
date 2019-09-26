function addDomain() {
  var ip = document.getElementById("ip").value;
  var domain = document.getElementById("domain").value;
  const http = new XMLHttpRequest();
  const url = 'http://127.0.0.1:30/newDomain';
  var params = 'ip='+ip+'&domain='+domain;
  http.open('POST', url, true);
  console.log(params)

//Send the proper header information along with the request
http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
http.send(params);
}
