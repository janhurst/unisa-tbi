/* Plugin to integrate in your js. By djibe, MIT license */
function bootstrapClearButton() {
    $('.position-relative :input').on('keydown focus', function() {
      if ($(this).val().length > 0) {
        $(this).nextAll('.form-clear').removeClass('d-none');
      }
    }).on('keydown keyup blur', function() {
      if ($(this).val().length === 0) {
        $(this).nextAll('.form-clear').addClass('d-none');
      }
    });
    $('.form-clear').on('click', function() {
      $(this).addClass('d-none').prevAll(':input').val('');
    });
  }
  
  // Init the script on the pages you need
  bootstrapClearButton();