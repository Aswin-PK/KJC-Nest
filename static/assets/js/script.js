createhostelmenu = document.getElementById('create-hstl-menu');
createadminmenu = document.getElementById('create-admin-menu');

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



// For highlighting the currently viewing sidebar menu items

document.addEventListener('DOMContentLoaded', function() {
    const menuitems = document.querySelectorAll('.sidebar-link');

    // Function to save the active menu item to localStorage
    const saveActiveMenuItem = (index) => {
        localStorage.setItem('activeMenuItem', index);
    };

    // Function to retrieve the active menu item from localStorage
    const getActiveMenuItem = () => {
        return localStorage.getItem('activeMenuItem');
    };

    // Initialize the active menu item based on localStorage or set the first item as active by default
    const activeMenuItemIndex = getActiveMenuItem() || 0;
    menuitems[activeMenuItemIndex].classList.add('active');

    // Event listener for menu item clicks
    menuitems.forEach((li, index) => {
        li.addEventListener('click', () => {
            menuitems.forEach(item => {
                item.classList.remove('active');
            });
            li.classList.add('active');
            saveActiveMenuItem(index);
        });
    });
});



// create options in hostel dashboard
let menu_options = document.getElementById('moreoptions');
let menuitem = document.getElementById('create-option');
menuitem.addEventListener('click', ()=>{
    menu_options.style.display = 'initial'
});



// MANAGE THE GRAPH DETAILS

const circle_percentage = document.querySelectorAll('.number .percentage'); /* will be an array of html div */
const display_circles = document.querySelectorAll('.displayCircle'); /* will be an array of html div */


circle_percentage.forEach((percentage, index) => {

    // Get the corresponding display_circle
    const display_circle = display_circles[index];
    
    // Calculate the change for each element
    let change = 376.991118 - (376.991118 * (75 * parseInt(percentage.innerText) / 100)) / 100;
    
    // Update the stroke-dashoffset for each display_circle
    display_circle.style.strokeDashoffset = change;
});
