//Scripts by Jordan
// toggle visiblity of items based on id
function toggle(id) {
    var x = document.getElementById(id);
    up = x.style.display === "none";
    x.style.display = up ? "block" : "none";
}
 // toggle contact form visibility
function contact() {
    toggle("contact");
    toggle("contact-button");
}