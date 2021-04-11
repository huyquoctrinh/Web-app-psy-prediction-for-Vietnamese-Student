// Input ID
$(document).ready(function () {
  $(
    ".input-group input[required], .input-group textarea[required], .input-group select[required]"
  ).on("keyup change", function () {
    var $form = $(this).closest("form"),
      $group = $(this).closest(".input-group"),
      $addon = $group.find(".input-group-addon"),
      $icon = $addon.find("span"),
      state = false;

    if (!$group.data("validate")) {
      state = $(this).val() ? true : false;
    }

    if (state) {
      $addon.removeClass("danger");
      $addon.addClass("success");
      $icon.attr("class", "glyphicon glyphicon-ok");
    } else {
      $addon.removeClass("success");
      $addon.addClass("danger");
      $icon.attr("class", "glyphicon glyphicon-remove");
    }

    if ($form.find(".input-group-addon.danger").length == 0) {
      $form.find('[type="submit"]').prop("disabled", false);
    } else {
      $form.find('[type="submit"]').prop("disabled", true);
    }
  });

  $(
    ".input-group input[required], .input-group textarea[required], .input-group select[required]"
  ).trigger("change");
});

// sign
