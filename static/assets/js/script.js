createhostelmenu = document.getElementById('create-hstl-menu');
createadminmenu = document.getElementById('create-admin-menu');

createroom = document.getElementById('createhstl');
createroom.addEventListener('click', ()=>{
    console.log("hello");
    createadminmenu.style.display = 'none'
    createhostelmenu.style.display = 'initial'
});

createroom = document.getElementById('createadmin');
createroom.addEventListener('click', ()=>{
    console.log("hello");
    createhostelmenu.style.display = 'none'
    createadminmenu.style.display = 'initial'
});