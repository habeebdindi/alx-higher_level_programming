$(document).ready(function() {
    $("INPUT#btn_translate").on('click', function () {
        translateHello();
    });

    $("INPUT#language_code").on('keypress', function(event) {
        if (event.which === 13) {
            translateHello();
        }
    });

    function translateHello() {
        var inputValue = $("INPUT#language_code").val();

        $.ajax({
            url: `https://hellosalut.stefanbohacek.dev/?lang=${inputValue}`,
            method: "GET",
            dataType: "json",
            success: function(data) {
                $("DIV#hello").text(data.hello);
            },
            error: function(xhr, status, error) {
                console.log(xhr.statusText);
            }
        });
    }
});
