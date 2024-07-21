console.log('Hello World');

function bruhMoment() {
    //console.log(this.src)
    alert("Bruh Moment");
    console.log("Bruh Moment")
}

function initialize_image_list(){
    image_set = document.querySelectorAll(".row-image");
    return image_set
}

function add_image_listener(image_set){
    image_set.forEach(element => {
        // console.log(element)
        element.addEventListener('click',bruhMoment)
    });
}

function startup(){
    image_set = initialize_image_list();
    // console.log(image_set)
    add_image_listener(image_set);
}

//image_box[0].addEventListener("click", bruhMoment());

//image_box.addEventListener("click", bruhMoment());

//document.getElementsByClassName("row-image").addEventListener("click", bruhMoment());

