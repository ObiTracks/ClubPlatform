function showMenu() {
    console.log("Button pressed");
    var menu = document.getElementById("Menu");

    if (menu.style.opacity == 0) {
      menu.style.opacity = 1;
      menu.style.display = "flex";
    } else {
      menu.style.opacity = 0;
      menu.style.display = "none";
    }

}

function showForm(formName){
    var form = document.getElementById(formName);
    form.style.display = "flex";

    var modal = document.getElementById("formModal");
    modal.style.display = "flex";

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {

        form.style.display = "none";
        modal.style.display = "none";
        }
    }
}
