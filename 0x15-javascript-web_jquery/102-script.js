$(document).ready(function() {
    $("INPUT#btn_translate").on('click', function () {
        let inputValue = $("INPUT#language_code").val();

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
    });
});
