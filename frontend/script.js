document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("whatsappBtn");
    const popup = document.getElementById("popup");
    const closeBtn = document.querySelector(".close-btn");
    const joinNow = document.getElementById("joinNow");

    // 🔴 PUT YOUR REAL WHATSAPP GROUP LINK HERE
    const whatsappLink = "https://docs.google.com/forms/d/e/1FAIpQLSeuQSMeGm0BTItmhDwzBcju87dd3i1yDtwpMnwL61xtYN406Q/viewform?usp=header";

    // OPEN POPUP
    btn.addEventListener("click", function(e) {
        e.preventDefault();
        popup.style.display = "flex";
    });

    // CLOSE POPUP
    closeBtn.addEventListener("click", function() {
        popup.style.display = "none";
    });

    // CLOSE ON OUTSIDE CLICK
    window.addEventListener("click", function(e) {
        if (e.target === popup) {
            popup.style.display = "none";
        }
    });

    // GO TO WHATSAPP
    joinNow.addEventListener("click", function(e) {
        e.preventDefault();
        window.open(whatsappLink, "_blank");
    });

});