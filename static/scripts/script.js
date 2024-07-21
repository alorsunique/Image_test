console.log('Hello World');

function bruhMoment() {
    console.log(this.src)
    alert("Bruh Moment");
}

function note_image() {
    const image_box = document.getElementsByClassName("row-image");
    //console.log(image_box);
    console.log("Here")
    return image_box
}

document.addEventListener("DOMContentLoaded", note_image);

console.log(image_box)




image_box.array.forEach(element => {
    element.addEventListener('click',bruhMoment)
});


//image_box[0].addEventListener("click", bruhMoment());

//image_box.addEventListener("click", bruhMoment());

//document.getElementsByClassName("row-image").addEventListener("click", bruhMoment());

