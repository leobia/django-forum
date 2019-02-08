function selezionaNumeroPagina() {
    var navigator = document.getElementById("paginatorId");
    var bottoniPaginazione = navigator.getElementsByClassName("page-item");
    var numeroPagina = window.location.href.substr(window.location.href.indexOf('=') + 1, window.location.href.length);
    for (var i = 0; i < bottoniPaginazione.length; i++) {
        if (page = '' && bottoniPaginazione.length >= 1) {
            bottoniPaginazione[1].className += "active"
        }
        if (bottoniPaginazione[i].textContent == page) {
            bottoniPaginazione[i].className += " active";
        } else {
            if (bottoniPaginazione[i].className.includes("active")) {
                bottoniPaginazione[i].className.replace("active", "");
            }
        }
    }
}