/*
Theme Name:       JobX - Bootstrap HTML5 Job Portal Template
Author:           UIdeck
Author URI:       http://uideck.com
Text Domain:      UIdeck
Domain Path:      /languages/

JS INDEX
================================================
1. preloader js
2. scroll to top js
3. slick menu js
4. sticky menu js
5. counter js
6. Testimonial owl carousel
7. New Products owl carouse
================================================*/

(function($) {

  "use strict";

    var $main_window = $(window);
    
    /*====================================
    preloader js
    ======================================*/
    $main_window.on("load", function() {
        $("#preloader").fadeOut("slow");
    });

    /*====================================
    scroll to top js
    ======================================*/
    $main_window.on("scroll", function() {
      if ($(this).scrollTop() > 250) {
        $(".back-to-top").fadeIn(200);
      } else {
        $(".back-to-top").fadeOut(200);
      }
    });
    $(".back-to-top").on("click", function() {
      $("html, body").animate(
        {
          scrollTop: 0
        },
        "slow"
      );
      return false;
    });

    /*====================================
    slick menu js
    ======================================*/
    var logo_path=$('.mobile-menu').data('logo');
    $('#main-navbar').slicknav({
        appendTo:'.mobile-menu',
        removeClasses:false,
        label:'',
        closedSymbol:'<i class="lni-chevron-right"><i/>',
        openedSymbol:'<i class="lni-chevron-down"><i/>',
        brand:'<a href="index.html"><img src="'+logo_path+'" class="img-responsive" alt="logo"></a>'
    });
      
    /*====================================
    sticky menu js
    ======================================*/
    $main_window.on('scroll', function () {  
      var scroll = $(window).scrollTop();
      if (scroll >= 100) {
          $(".scrolling-navbar").addClass("top-nav-collapse");
      } else {
          $(".scrolling-navbar").removeClass("top-nav-collapse");
      }
    });

    /*=======================================
    counter
    ======================================= */
    if ($(".fact-count").length > 0) {
      $(".counter").counterUp({
        delay: 10,
        time: 500
      });
    }


    /*====================================
    Testimonials Carousel 
    ======================================*/
    var testiOwl = $("#testimonials");
    testiOwl.owlCarousel({
        autoplay:true,
        margin:30,
        dots:true,
        autoplayHoverPause:true,
        nav:false,
        loop:true,
        responsiveClass:true,
        responsive:{
            0: {
                items:1,
            },
            991:{
                items:1
          }
        }
    });

    /*====================================
    New Products Owl Carousel
    ======================================*/
    var newproducts = $("#new-products");
      newproducts.owlCarousel({
        autoplay: true,
        nav: true,
        autoplayHoverPause:true,
        smartSpeed: 350,
        dots: false,
        margin:30,
        loop: true,
        navText: [
          '<i class="lni-chevron-left"></i>',
          '<i class="lni-chevron-right"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
            },
            575: {
                items: 2,
            },
            991: {
                items: 3,
            }
          }
      });

  })(jQuery);
  $('.counter-count').each(function () {
    $(this).prop('Counter',0).animate({
        Counter: $(this).text()
    }, {
        duration: 5000,
        easing: 'swing',
        step: function (now) {
            $(this).text(Math.ceil(now));
        }
    });
});


// ============================================================================================add more button 
// 
// add more field
$(document).ready(function () {
  //@naresh action dynamic childs
  var next = 0;
  $("#add-more").click(function(e){
      e.preventDefault();
      var addto = "#field" + next;
      var addRemove = "#field" + (next);
      next = next + 1;
      var newIn = ' <div id="field'+ next +'" name="field'+ next +'"> <div class="form-group"><input type="text" class="form-control" placeholder="Degree" ></div><div class="form-group"><div class="form-group"><input type="text" class="form-control" placeholder="CGPA   "></div><input type="text" class="form-control" placeholder="Field of Study"></div><div class="form-group"><input type="text" class="form-control" placeholder="College/University "></div><div class="form-group"><input type="text" class="form-control" placeholder="State  "></div><div class="form-group"><div class="row"><div class="col-md-6"><label class="control-label">From</label><input type="text" class="form-control" placeholder="e.g 2014"></div><div class="col-md-6"><label class="control-label">To</label><input type="text" class="form-control" placeholder="e.g 2020"></div></div></div>';
      var newInput = $(newIn)
    
      var removeBtn = '<div class="float-right"><button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" ><i class="fa-solid fa-trash"></i> Delete This </button></div></div></div><div id="field">';
      


      
      var removeButton = $(removeBtn);
      $(addto).after(newInput);
      $(addRemove).after(removeButton);
      $("#field" + next).attr('data-source',$(addto).attr('data-source'));
      $("#count").val(next);  
      
          $('.remove-me').click(function(e){
              e.preventDefault();
              var fieldNum = this.id.charAt(this.id.length-1);
              var fieldID = "#field" + fieldNum;
              $(this).remove();
              $(fieldID).remove();
          });
          
          $('#submit').click(function(){
            $.ajax({
              url:'{% url "jobseeker_create_cv" %}',
              type:'POST',
              data:{
                   field 
              },
              success:function(data)
              {
                alert(data);
                $('field').html(data)
                $('#add')[0].reset()
              }

            });

          });
  });

});

// experience fileds
$(document).ready(function () {
  //@naresh action dynamic childs
  var next = 0;
  $("#addb").click(function(e){
      e.preventDefault();
      var addto = "#f" + next;
      var addRemove = "#f" + (next);
      next = next + 1;
      var newIn = ' <div id="f'+ next +'" name="f'+ next +'"> <div class="form-group"><input type="text" class="form-control" placeholder="Company name"></div><div class="form-group"><input type="text" class="form-control" placeholder="Job Position"></div><div class="form-group"><input type="text" class="form-control" placeholder="Location "></div><div class="form-group"><div class="row"><div class="col-md-6"><label class="control-label">From </label><input type="text" class="form-control" placeholder="e.g 2014"></div><div class="col-md-6"><label class="control-label">To</label><input type="text" class="form-control" placeholder="e.g 2020"></div></div></div>';
      var newInput = $(newIn);
      var removeBtn = '<div class="float-right"><button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" ><i class="fa-solid fa-trash"></i> Delete This </button></div></div></div><div id="f">';
      


      
      var removeButton = $(removeBtn);
      $(addto).after(newInput);
      $(addRemove).after(removeButton);
      $("#f" + next).attr('data-source',$(addto).attr('data-source'));
      $("#count").val(next);  
      
          $('.remove-me').click(function(e){
              e.preventDefault();
              var fieldNum = this.id.charAt(this.id.length-1);
              var fieldID = "#f" + fieldNum;
              $(this).remove();
              $(fieldID).remove();
          });
  });

});
// ====================================================================================













