$(document).ready(function() {
    const objectList = $('#object-list');

    // Add Object
    $('#add-button').click(function() {
        $.post('/ajouter-arene', function(response) {
            const newDiv = `
                <div class="object" data-id="${response.arene._id}">
                    <div class="object-id">#${response.arene._id}</div>
                    <input type="text" class="nom_cbt_rouge readonly" value="${response.arene.combattants['rouge'].nom}" readonly>
                    <span class="label red-label">Rouge: ${response.arene.score['rouge']}</span>
                    <button class="edit-button">Edit</button>
                    <button class="save-button" style="display: none;">Save</button>
                    <span class="label green-label">Vert: ${response.arene.score['vert']}</span>
                    <input type="text" class="nom_cbt_vert readonly" value="${response.arene.combattants['vert'].nom}" readonly>
                </div>`;
            objectList.append(newDiv);
        }).fail(function() {
            alert('Erreur dans l\'ajout de l\'arène.');
        });
    });

    // Remove Object
    $('#remove-button').click(function() {
        $.post('/supprimer-arene', function(response) {
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