createhostelmenu = document.getElementById('create-hstl-menu');
createadminmenu = document.getElementById('create-admin-menu');

createroom = document.getElementById('createhstl');
createroom.addEventListener('click', ()=>{
    console.log("hello");
    createadminmenu.style.visibility = 'hidden'
    createhostelmenu.style.visibility = 'visible'
});

createroom = document.getElementById('createadmin');
createroom.addEventListener('click', ()=>{
    createadminmenu.style.visibility = 'visible'
    createhostelmenu.style.visibility = 'hidden'
});

function previewImage(event) {
    const input = event.target;
    const image = document.getElementById('hstlimage');

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            image.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        // Handle the case when no file is selected
        image.src = "{% static 'assets/img/logo.png' %}";
    }
}

// close_btn = document.querySelectorAll('#close_btn');
// close_btn.forEach((btn) => {
//     btn.addEventListener('click', () => {
//         console.log();
//     });
// });

function close_btn(modal_type){
    if(modal_type === 'hstl'){
        console.log('clicked hstl');
        document.querySelectorAll('#create-hstl-menu').display = 'none';
    }
    if(modal_type === 'admin'){
        console.log('clicked admin');
        document.querySelectorAll('#create-admin-menu').display = 'none';
    }
    // if(modal_type === 'hstl'){
        
    // }
    // if(modal_type === 'hstl'){
        
    // }
    // if(modal_type === 'hstl'){
        
    // }
}