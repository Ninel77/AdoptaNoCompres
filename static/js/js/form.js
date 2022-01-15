/*
var animal = {
    items : {
        animal:'',
        adoptante:'',
        documentos:'',
        edadAnimal:'',
        fotoAdopcion:'',
        descripcionAdop:'',
        fechaRegistroAdop:'',
        animalProd:[]
    },

};
$(function () {
    $('select').select2({
        theme: 'bootstrap4',
        lenguage: 'es'
    });
    $('#fechaRegistroAdop').datetimepicker({
        //format: 'YYYY-MM-DD',
        //date: moment().format("YYYY-MM-DD"),
        locale: 'es',
    });

    //Buscar Animales de compañia
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_animales',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {
            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            console.log(ui.item);
        }
    });

});*/