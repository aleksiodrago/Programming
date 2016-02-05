/*Name this external file gallery.js*/
var divs = document.getElementById("image")
function upDate(previewPic){

divs.innerHTML = previewPic.alt;

divs.style.backgroundImage = "url("+ previewPic.src +")"



}
function unDo(){
divs.innerHTML= "Hover over an image below to display here";
divs.style.background = "#8e68ff";
}
 /* In this function you should
    1) change the url for the background image of the div with the id = "image"
    to the source file of the preview image

    2) Change the text  of the div with the id = "image"
    to the alt text of the preview image
    */
