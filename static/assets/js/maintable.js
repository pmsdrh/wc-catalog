function edit(id) {
    $("#tr-" + id).attr('contenteditable', 'true');
    var handler = $("#tr-" + id + " .handler");
    handler.html(
        '<button type="button" class="btn btn-outline-success" onclick="edit_success(' + id + ')">تایید</button>/' +
        '<button type="button" class="btn btn-outline-danger" onclick="edit_error(' + id + ')">لغو</button>'
    );

};

function edit_error(id) {
    $("#tr-" + id).attr('contenteditable', 'false');
    $("#tr-" + id + " .handler").html(
        '<button type="button" class="btn btn-outline-success edit" id="edit-' + id + '" onclick="edit(' + id + ')">ویرایش</button>\n' + '/' +
        '<button type="button" class="btn btn-outline-danger delete" id="delete-' + id + '">حذف</button>'
    )
}

function edit_success(id) {
    update(id);
}


function update(id) {
    alert($("#tr-" + id + ' .name').text())
    var data = {
        'id': id,
        'name': $("#tr-" + id + ' .name').text(),
        'regular_price': $("#tr-" + id + ' .price').text(),
        csrfmiddlewaretoken: csrfcookie

    };
    $.ajax({
        type: "POST",
        url: "/api/update-product/",
        cache: false,
        dataType: 'application/json, charset=utf-8',
        data: data
    });
}

$(document).ready(function () {

    var selectall = $('.select-all');
    var select = $('.select');
    selectall.click(
        function (e) {

            if ($(this).is(':checked')) {
                select.prop('checked', true);
            } else {
                select.prop('checked', false);
            }
        }
    );
});
