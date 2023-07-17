(function(){
    const modal = new bootstrap.Modal(document.getElementById("modal"))
    htmx.on("htmx:afterSwap", e=>{
        if (e.target.detail.target.id === "dialog") {modal.classList.add("modal fade"); modal.show();
    }
})()