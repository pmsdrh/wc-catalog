$(document).ready(function () {


    $("#update-selected").click(function (e) {
        var products_data = [];
        $(".select:not(.select-all):checked").each(function (e, f) {
            var checkbox = $(this).parent().parent();
            var id = checkbox.siblings(".id").text();
            var name = checkbox.siblings(".name").text();
            var price = checkbox.siblings(".price").text();
            products_data.push({'id': id, 'name': name, 'regular_price': price})

        });

        var data = {
            product_data: JSON.stringify(products_data),
            csrfmiddlewaretoken: csrfcookie

        };
        $.ajax({
            type: "POST",
            url: "/api/multi/update-products/",
            cache: false,
            dataType: 'json',
            data: data,
            success: function (msg) {
                Swal.fire({
                    title: 'انجام شد',
                    icon: 'success',
                    text: 'با موفقیت اپدیت شد!',
                    showCancelButton: true,
                    confirmButtonText: 'باشه',
                    denText: 'مشاهده جزئیات'
                }).then((result) => {
                    if (result.isDenied) {
                        Swal.fire('Saved!', '', 'success')
                    }
                })


            },
            error: function (msg) {
                console.log(msg)
            }
        });
    });
    $("#edit-selected").click(function (e) {
        $(".select:not(.select-all):checked").each(function (e, f) {
            var handler = $(this).parents(".selectbox").siblings(".handler");
            if (handler.siblings("td.selectbox").children("input:checked")) {
                handler.each(function (e, f) {
                    var id = f.id.replace("handler-", "");
                    $("#tr-" + id).attr('contenteditable', 'true');
                    handler.html(
                        '<button type="button" class="btn btn-outline-success" onclick="edit_success(' + id + ')">تایید</button>/' +
                        '<button type="button" class="btn btn-outline-danger" onclick="edit_error(' + id + ')">لغو</button>'
                    );
                })
            }


        });
    });
    $("#edit-price").click(function (e) {
        Swal.fire({
            title: 'عدد خود را وارد کنید',
            input: 'text',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'Look up',
        }).then((result) => {
            if (result.isConfirmed) {
                $(".select:not(.select-all):checked").parents(".selectbox").siblings(".price").each(function (e, f) {
                    if ($(this).text()) {
                        $(this).text(parseInt($(this).text()) + parseInt($(this).text()) * parseInt(result.value) / 100);
                    }
                })
            }
        });
    });

    $("#export-excel").click(function (e) {
        Swal.fire({
            title: 'لطفا فیلتر و نام اکسل را وارد کنید.',
            html:
                '<input id="excel-product-filter" class="swal2-input">' +
                '<input id="excel-name" class="swal2-input">',
            preConfirm: () => {
                data = {
                    'excel-name': $("#excel-name").val(),
                    'excel-product-filter': $("#excel-product-filter").val(),
                    'csrfmiddlewaretoken': csrfcookie()
                };
                $.ajax({
                    type: "POST",
                    url: "export/excel/",
                    cache: false,
                    dataType: 'json',
                    data: data,

                })
            }
        });
    });
    $("#export-PDF").click(function (e) {
        function downloadFile(filePath){
            var link=document.createElement('a');
            link.href = filePath;
            link.target = "_blank";
            link.download = filePath.substr(filePath.lastIndexOf('/') + 1);
            link.click();
        }
        Swal.fire({
            title: 'لطفا فیلتر و نام PDF را وارد کنید.',
            html:
                '<input id="pdf-product-filter" class="swal2-input">' +
                '<input id="pdf-name" class="swal2-input">',
            preConfirm: () => {
                console.log(csrfcookie());

                data = {
                    'pdf-name': $("#pdf-name").val(),
                    'pdf-product-filter': $("#pdf-product-filter").val(),
                    'csrfmiddlewaretoken': csrfcookie()
                };
                $.ajax({
                    type: "POST",
                    url: "export/pdf/",
                    cache: false,
                    dataType: 'json',
                    data: data,
                    success: function (msg) {

                        downloadFile("/static/download/pdf/" + msg["name"])
                    }, error: function (msg) {
                        console.log(msg);
                    }

                })
            }
        });
    });

});
