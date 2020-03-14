$(document).ready(function(){

   "use strict"
  $(".goods .input-select").change(function(){
        var data_goods=$(this).val;
        console.log(data_goods);

  })
  
if($(".goods .input-select option:selected").text="端子")
   {
    $(".goods-color").hide();
    $(".goods-pin").hide();
    $(".goods-lock").hide();
    $(".goods-weld").show();
    $(".goods-sex").show();
   }

   if($(".goods .input-select option:selected").text="胶壳")
   {
    $(".goods-color").show();
    $(".goods-pin").show();
    $(".goods-lock").show();
    $(".goods-weld").hide();
    $(".goods-sex").show();
   }


   if($(".goods .input-select option:selected").text="针座")
   {
    $(".goods-color").show();
    $(".goods-pin").show();
    $(".goods-lock").show();
    $(".goods-weld").show();
    $(".goods-sex").show();
   }



  // Mobile Nav toggle
  $('.menu-toggle > a').on('click', function (e) {
    e.preventDefault();
    $('#responsive-nav').toggleClass('active');
  })

  // Fix cart dropdown from closing
  $('.cart-dropdown').on('click', function (e) {
    e.stopPropagation();
  });

  /////////////////////////////////////////

  // Products Slick
  $('.products-slick').each(function() {
    var $this = $(this),
        $nav = $this.attr('data-nav');

    $this.slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: true,
      infinite: true,
      speed: 300,
      dots: false,
      arrows: true,
      appendArrows: $nav ? $nav : false,
      responsive: [{
          breakpoint: 991,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        },
      ]
    });
  });

  // Products Widget Slick
  $('.products-widget-slick').each(function() {
    var $this = $(this),
        $nav = $this.attr('data-nav');

    $this.slick({
      infinite: true,
      autoplay: true,
      speed: 300,
      dots: false,
      arrows: true,
      appendArrows: $nav ? $nav : false,
    });
  });

  /////////////////////////////////////////

  // Product Main img Slick
  $('#product-main-img').slick({
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    fade: true,
    asNavFor: '#product-imgs',
  });

  // Product imgs Slick
  $('#product-imgs').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    focusOnSelect: true,
    centerPadding: 0,
    vertical: true,
    asNavFor: '#product-main-img',
    responsive: [{
        breakpoint: 991,
        settings: {
          vertical: false,
          arrows: false,
          dots: true,
        }
      },
    ]
  });

  // Product img zoom
  var zoomMainProduct = document.getElementById('product-main-img');
  if (zoomMainProduct) {
    $('#product-main-img .product-preview').zoom();
  }

  /////////////////////////////////////////

  // Input number
  $('.input-number').each(function() {
    var $this = $(this),
    $input = $this.find('input[type="number"]'),
    up = $this.find('.qty-up'),
    down = $this.find('.qty-down');

    down.on('click', function () {
      var value = parseInt($input.val()) - 1;
      value = value < 1 ? 1 : value;
      $input.val(value);
      $input.change();
      updatePriceSlider($this , value)
    })

    up.on('click', function () {
      var value = parseInt($input.val()) + 1;
      $input.val(value);
      $input.change();
      updatePriceSlider($this , value)
    })
  });

  var priceInputMax = document.getElementById('price-max'),
      priceInputMin = document.getElementById('price-min');

  

  // Price Slider
  var priceSlider = document.getElementById('price-slider');
  if (priceSlider) {
    noUiSlider.create(priceSlider, {
      start: [1, 999],
      connect: true,
      step: 1,
      range: {
        'min': 1,
        'max': 999
      }
    });

    priceSlider.noUiSlider.on('update', function( values, handle ) {
      var value = values[handle];
      handle ? priceInputMax.value = value : priceInputMin.value = value
    });
  }
    console.log("1")
   $.getJSON("http://127.0.0.1:8000/goods/2",function(goodsdata){
        var ggoods_name=goodsdata[sku_name].split('/')
        console.log(ggoods_name[0])

   })









   var skuname=[]
   var goodcount=[]
    $.getJSON("http://127.0.0.1:8000/categories/goodsdetail",function(goodsdatas){  
        $.each(goodsdatas,function(key,val){
          if(val["goods"]){
            var html=''
          
   html+='<div class="col-md-4 col-xs-6"><div class="product"><div class="product-img">'
   //html+='<img src="'++'" alt="">'
   html+='<div class="product-label"><span class="new">NEW</span><span class="new">HOT</span></div></div><div class="product-body"><p class="product-category">'
   html+=""+key+""
   html+='</p><h3 class="product-name"><a href="#">'
   html+=""+val["goods"]+""
   console.log(val["goods"])
   html+='</a></h3><h4 class="product-price">$0.01<del class="product-old-price">$0.10</del></h4><div class="product-rating"><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>'
   html+='<div class="product-btns"><button class="add-to-compare"><i class="fa fa-phone-square"></i><span class="tooltipp">联系我们</span></button><button class="quick-view"><i class="fa fa-eye"></i><span class="tooltipp">查看详情</span>'
   html+='</button></div></div><div class="add-to-cart"><button class="add-to-cart-btn"><i class="fa fa-heart-o"></i> 加入清单</button></div></div></div>'


        }
        })
      })

  $.getJSON("http://127.0.0.1:8000/categories",function(datas){  
        $.each(datas,function(i,val){
              skuname.push(val.name)
              console.log(skuname)
              $('.checkbox-filter').append('<ul id="down_'+i+'" class ="navdown"><i class="fa fa-chevron-down"></i><a href="#products" style="color:#fff;">'+val.name+'</a><div class="distance_'+i+' distance"></div></ul>');
              $.getJSON("http://127.0.0.1:8000/categories/"+val.id+"/skus/",function(data){ 
              skusku=data
              console.log(skusku)
              $.each(data,function(j,val1){
                 $.getJSON("http://127.0.0.1:8000/sku/"+val1.id+"/",function(skudata){ 
                     //$.each(skudata,function(key,value)) 
                      if(skudata['params']["间距"])
                        {console.log(skudata['params']["间距"])};
                      
                })})
               })
              


               $.getJSON("http://127.0.0.1:8000/categories/"+val.id+"/goods/",function(goodsdata){ 
                console.log(val.id)
             $.each(goodsdata,function(k,val2){
                 
                  $.each(val2,function(key,val3){
                    console.log(val.id)
                  console.log(val.name)

                })
                })

              })


              $(".distance_"+i+"").append("<li><a href='#'>2mm</a></li><li><a href='#'>2mm</a></li>");
              $(".distance_"+i+"").hide();
                 $('.checkbox-filter').on({"mouseover":function(){
                            var index = $(this).index();
                            $(".distance_"+index+"").show();
                           
                            },
                             "mouseout":function(){
                            var index = $(this).index();
                            $(".distance_"+index+"").hide();
                           
                            } 
                            },".navdown")  

          })
  })
})
