function hoverAnimation() {
  var menuItemsShape = $(".js-shape"),
    linksWrapper = $(".js-menu-items-wrapper"),
    linksItems = $(".js-menu-item"),
    activeItem = $(".js-menu-item.is-active"),
    activeItemPosition = activeItem.position().top,
    menuItemsShapePath = $(".js-items-shape-path"),
      info = $(".js-info");
  TweenMax.set(menuItemsShape, {
    y: activeItemPosition
  });
  linksItems.on({
    mouseenter: function() {
      _self = $(this);
      var selfParent = _self.closest(linksWrapper),
        targetCircle = selfParent.find(menuItemsShape),
        circlePosition;
      if ($(window).width() < 600) {
        circlePosition = _self.position().top;
        TweenMax.to(targetCircle, 0.6, {
          y: circlePosition,
          ease: Power2.easeOut
        });
      } else {
        circlePosition = _self.position().left;
        TweenMax.to(targetCircle, 0.6, {
          x: circlePosition,
          ease: Power2.easeOut
        });
      }
      TweenMax.to(menuItemsShapePath, 1, { morphSVG: this.dataset.morph });
    }
  });
  $(window).resize(function() {
    info.show();
  });
}
hoverAnimation();