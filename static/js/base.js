$(document).ready(function () {

    // ===== MÁSCARAS ===== //
    $('.cpf input').mask('000.000.000-00', {reverse: true, placeholder: 'Somente números'});
    $('.cnpj input').mask('00.000.000/0000-00', {reverse: true});
    $('.hora input').mask('00:00');
    $('.data input').mask('00/00/0000');
    $('.dois_digitos input').mask('00');
    $('.dez_digitos input').mask('0000000000', {placeholder: 'Somente números'});
    $('.cep input').mask('00000-000', {placeholder: 'Somente números'});
    $('.rg input').mask('000000000', {placeholder: 'Somente números'});
    $('.fone_ddd_9digitos input').mask('(00) 00000-0000', {placeholder: '(XX) XXXXX-XXXX'});
    $('.fone_ddd_8digitos input').mask('(00) 0000-0000', {placeholder: '(XX) XXXX-XXXX'});
    $('.crm input').mask('00000000000000000000000000000000');
    $('.valor input').mask('00000000000000000,00', {reverse: true});
    $('.somente_numeros input').mask('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', {placeholder: 'Somente números'});
    $('.somente_letras input').mask('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS', {
        'translation': {
            S: {pattern: /[A-Za-zÀ-ú ]/},
        },
        placeholder: 'Somente letras'
    });

    // ===== ESTILIZAR DROPDOWNS ===== //
    $('select').dropdown();

    $('.ui.dropdown').dropdown();
});

$('.message .close').on('click', function () {
    window.history.back();
});

// $('.abrirModalCadCid').click(function () {
//     $('.modalCadCid').modal('show');
// });

// function atualiza_select_cargo(id_cargo) {
//     $.ajax({
//         type: 'POST',
//         url: '/coleta/atualiza/cargo/',
//         data: {
//             sec: $("input[name='cargo']").val(),
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         dataType: 'json',
//         success: function (dado) {
//             var options = '';
//             for (var i = dado.length - 1; i >= 0; i--) {
//                 options += '<option value="' + dado[i].pk + '">' + dado[i].fields['nome'] + '</option>';
//             }
//             console.log(dado);
//             $("select#id_cargo").html(options);
//         },
//     });
// }
