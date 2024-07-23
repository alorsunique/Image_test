console.log('Hello World');

clicked_image = []

function change_image_property(image_id) {
    //document.getElementById(image_id).style.opacity = 0.5;
    document.getElementById(image_id).classList.add('test_class');

}

function bruhMoment() {
    //console.log(this.src)
    // alert("Bruh Moment");
    console.log("Bruh Moment");
    //console.log(this.id)

    if (clicked_image.includes(this.id)){
        console.log("Element was present")


        index = clicked_image.indexOf(this.id);
        if (index !== -1) {
            clicked_image.splice(index, 1);
        }

    }else{
        console.log("Element was absent")
        clicked_image.push(this.id)
    }

    change_image_property(this.id);
    console.log(clicked_image.length)
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

function send_list(){

    list_dict_values = {clicked_image}
    json_list = JSON.stringify(list_dict_values)

    console.log(json_list)

    fetch("/data", {
        method: "POST",
        body: json_list,
        headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
    })
    .then((response) => response.json())
    .then((json) => console.log(json));

}