setTimeout(function () {
    $('.alert').remove();
}, 10000);


document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = sessionStorage.getItem('scrollpos');
    if (scrollpos) {
        window.scrollTo(0, scrollpos);
        sessionStorage.removeItem('scrollpos');
    }
});

window.addEventListener("beforeunload", function (e) {
    sessionStorage.setItem('scrollpos', window.scrollY);
});

if (location.href.includes('dashboard')) {
    var uploadField = document.getElementById("data");
    uploadField.onchange = function() {
        if(this.files[0].size > 1048576*2)
        {
            alertbox = document.getElementById('show-this')
            alertbox.innerHTML = '<div class="alert alert-danger" role="alert">File size cannot be greater than 2MB!</div>'
            this.value = "";
        };
    };
  }
