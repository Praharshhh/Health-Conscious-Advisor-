document.addEventListener("DOMContentLoaded", function() {
    // Get elements
    var profileDropdown = document.getElementById("profile-dropdown");
    var viewProfileLink = document.getElementById("view-profile");
    var editProfileLink = document.getElementById("edit-profile");
    var logoutLink = document.getElementById("logout");

    // Simulate user data (replace with actual data from your application)
    var userData = {
        username: "John Doe",
        profilePicture: "profile-picture.jpg",
        profileLink: "#", // Replace with the actual link to the user's profile page
        editProfileLink: "#", // Replace with the actual link to the edit profile page
        logoutLink: "#" // Replace with the actual logout link
    };

    // Update profile information
    document.getElementById("username").innerText = userData.username;
    document.getElementById("profile-picture").src = userData.profilePicture;

    // Add click event listeners to menu items
    viewProfileLink.addEventListener("click", function(event) {
        event.preventDefault();
        window.location.href = userData.profileLink;
    });

    editProfileLink.addEventListener("click", function(event) {
        event.preventDefault();
        window.location.href = userData.editProfileLink;
    });

    logoutLink.addEventListener("click", function(event) {
        event.preventDefault();
        window.location.href = userData.logoutLink;
    });

    // Close dropdown when clicking outside of it
    document.addEventListener("click", function(event) {
        if (!event.target.matches('.dropbtn')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    });

    // Show dropdown on button click
    profileDropdown.addEventListener("click", function() {
        document.getElementById("profile-dropdown").classList.toggle("show");
    });
});
