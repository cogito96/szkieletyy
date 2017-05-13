
function clock() {
    var today = new Date();
    var day = today.getDate();
    var mounth = today.getMonth() + 1;
    var year = today.getFullYear();
    var hours = today.getHours();
    var minutes = today.getMinutes();
    var secs = today.getSeconds();

    document.getElementById("zegar").innerHTML =
        day+"/"+mounth+"/"+year+" | "+hours+"/"+minutes+"/"+secs;
    //document.getElementById("zegar").innerHTML = today
    setTimeout("clock()",1000);
}
