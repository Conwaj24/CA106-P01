//Scripts by Jordan
// toggle visiblity of items based on id
function toggle(id) {
    var x = document.getElementById(id);
    up = x.style.display === "none";
    x.style.display = up ? "block" : "none";
}
function swap(id0, id1){
    toggle(id0);
    toggle(id1);
}
function swapNext(id){
    var x = document.getElementById(id).nextSibling;
    toggle(id);
    x.style.display = "block";
}
function swapPrev(id){
    var x = document.getElementById(id).prevSibling;
    toggle(id);
    x.style.display = "block";
}
 // toggle contact form visibility
function contact() {
    swap("contact", "contact-button");
}
// toggle visibility of specific lightbox slide
function lightbox(id) {
    swap('lightbox', id);
}