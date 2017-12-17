$(document).ready(function () {
    var form = $('#form_buying_product');
    form.on('submit',function (e) {
        e.preventDefault();

        var nmb=$('#number').val();
        var submit_btn=$('#submit_btn');
        var product_id=submit_btn.data("product_id");
        var product_name=submit_btn.data("name");
        var product_price=submit_btn.data("price");
        var total_price=product_price*nmb;


        var data = {};
        data.product_id=product_id;
        data.nmb=nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        console.log(data);
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                // console.log(data.products_total_nmb);
                // if (data.products_total_nmb ){
                     //|| data.products_total_nmb == 0){
                 //   $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                   // console.log(data.products);
                   //  $('.basket-items ul').html("");
                   //  $.each(data.products, function(k, v){
                     //   $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + ' pieces ' + v.price + 'usd ' +
                          //  '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                     //       '</li>');
                   //  });
                 }

            // }
             ,
             error: function(){
                 console.log("error")
             }
         })
        $('.basket-items ul').append('<li>'+product_name+', ' + nmb + ' pieces '  + total_price + ' usd ' +
            '<a class="delete-item" href="">x</a>'+
            '</li>')
    })
    function ShowingBasket() {

        $('.basket-items').removeClass('hidden');
        
    }
    $('.basket-container').on('click',function (e)
    {
        e.preventDefault();
        ShowingBasket();

    })
    $('.basket-container').mouseover(function ()
    {
       ShowingBasket();
    })
     $('.basket-container').mouseout(function ()
    {

    //ShowingBasket();

    })
      $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         $(this).closest('li').remove();
     })
});