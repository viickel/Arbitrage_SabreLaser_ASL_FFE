$(document).ready(function() {
    const objectList = $('#object-list');

    // Add Object
    $('#add-button').click(function() {
        $.post('/add-object', function(newObject) {
            const newDiv = `
                <div class="object" data-id="${newObject.id}">
                    <div>
                        <strong>${newObject.label1}</strong><br>
                        <strong>${newObject.label2}</strong>
                    </div>
                    <div>
                        <input type="text" class="value1 readonly" value="${newObject.value1}" readonly>
                        <input type="text" class="value2 readonly" value="${newObject.value2}" readonly>
                    </div>
                    <button class="edit-button">Edit</button>
                    <button class="save-button" style="display: none;">Save</button>
                </div>`;
            objectList.append(newDiv);
        }).fail(function() {
            alert('Failed to add object.');
        });
    });

    // Remove Object
    $('#remove-button').click(function() {
        $.post('/remove-object', function(response) {
            const lastObject = objectList.children('.object').last();
            if (lastObject.length) {
                lastObject.remove();
                alert(response.message);
            }
        }).fail(function(xhr) {
            alert(xhr.responseJSON.message);
        });
    });

    // Toggle edit mode
    $(document).on('click', '.edit-button', function() {
        const container = $(this).closest('.object');
        container.find('input').removeClass('readonly').prop('readonly', false);
        $(this).hide();
        container.find('.save-button').show();
    });

    // Save changes
    $(document).on('click', '.save-button', function() {
        const container = $(this).closest('.object');
        const id_arene = container.data('id');
        const nom_cbt_rouge = container.find('.nom_cbt_rouge').val();
        const nom_cbt_vert = container.find('.nom_cbt_vert').val();

        $.ajax({
            url: `/changer-nom/${id_arene}`,
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ nom_cbt_rouge, nom_cbt_vert }),
            success: function(response) {
                alert("Sauvegardé");
                container.find('input').addClass('readonly').prop('readonly', true);
                container.find('.save-button').hide();
                container.find('.edit-button').show();
            },
            error: function(xhr) {
                alert('Error: ' + xhr.responseJSON.error);
            }
        });
    });
});