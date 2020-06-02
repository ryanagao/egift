



$(document).ready(function() {




    $('.btn-save-egift').on('click', function() {
        var id = $(this).data('id');

        html2canvas($('.egift-template').get(0)).then(function (canvas) {

          var base64encodedstring = canvas.toDataURL("image/png", 1);
          $.ajax({
            url: base_url + 'egift/save-preview',
            data: {
                id: id,
                base64encodedstring: base64encodedstring
            },
            method: 'post',
            success: (res => {
            })
          })
        });
    });


    $('a.nav-link').on('click', function() {
        var url = $(this).data('url');
        if(url) {
            localStorage.page_url = url;
        }
    });



    $(document).find('a[data-url="'+ localStorage.page_url +'"]').addClass('active');

    $(document).find('li.nav-item > a.active').parents('li.nav-item').addClass('open');



    $('.add-menu').on('click', function() {
        $.ajax({
            url: base_url + 'role/get-main-menu',
            dataType: 'html',
            success: (res => {
                $('.main-menu').prepend(res);
                $('.main-menu-sortable').sortable({
                    connectWith: '.sortable',
                    placeholder: 'ui-state-highlight',
                });

            })
        });
    });

    $('.collapse-menu').on('click', function() {
        $(document).find('.sub-menu').toggleClass('show');
    });

    $(document).on('click', '.btn-remove-main-menu-panel', function() {
        $(this).closest('.main-menu-panel').remove();
    });

    $(document).on('click', '.btn-remove-sub-menu-panel', function() {
        $(this).closest('.sub-menu-panel').remove();
    });

    $(document).on('click', '.btn-add-sub-menu', function() {
        var self = this;
        var main_key = $(self).closest('.main-menu-panel').data('key');


        $.ajax({
            url: base_url + 'role/get-sub-menu',
            data: {main_key: main_key},
            method: 'get',
            dataType: 'html',
            success: (res => {
                $(self).closest('.main-menu-panel').find('.sub-menu').prepend(res);

                $(self).closest('.main-menu-panel').find('.collapse').addClass('show');

                $('.sortable').sortable({
                    connectWith: '.sortable',
                    placeholder: 'ui-state-highlight',
                });
// $('select').select2();
})
        });
    });



    $('select').select2();

    $('.check-all-action').on('click', function() {
        if($(this).is(':checked')) {
            $(document).find('input[name="'+ $(this).data('key') +'"]').prop('checked', true);
        }
        else {
            $(document).find('input[name="'+ $(this).data('key') +'"]').prop('checked', false);
        }
    });


    $('#check-all-checkbox').on('click', function() {
        if($(this).is(':checked')) {
            $(document).find('input[type="checkbox"]').prop('checked', true);
        } 
        else {
            $(document).find('input[type="checkbox"]').prop('checked', false);
        }
    });




    var createChart = function(element, labels, data) {
        var cardChart1 = new Chart(element, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Registered',
                    backgroundColor: getStyle('--primary'),
                    borderColor: 'rgba(255,255,255,.55)',
                    data: data
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    xAxes: [{
                        gridLines: {
                            color: 'transparent',
                            zeroLineColor: 'transparent'
                        },
                        ticks: {
                            fontSize: 2,
                            fontColor: 'transparent'
                        }
                    }],
                    yAxes: [{
                        display: false,
                        ticks: {
                            display: false,

        }
        }]
        },
        elements: {
            line: {
                borderWidth: 1
            },
            point: {
                radius: 4,
                hitRadius: 10,
                hoverRadius: 4
            }
        }
        }
        }); 
    }

    var createEgiftCreationChart = function(element, labels, data) {
        var cardChart2 = new Chart(element, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Created Egift',
                    backgroundColor: getStyle('--info'),
                    borderColor: 'rgba(255,255,255,.55)',
                    data: data
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    xAxes: [{
                        gridLines: {
                            color: 'transparent',
                            zeroLineColor: 'transparent'
                        },
                        ticks: {
                            fontSize: 2,
                            fontColor: 'transparent'
                        }
                    }],
                    yAxes: [{
                        display: false,
                        ticks: {
                            display: false,
                            min: -4,
                            max: 39
                        }
                    }]
                },
                elements: {
                    line: {
                        tension: 0.00001,
                        borderWidth: 1
                    },
                    point: {
                        radius: 4,
                        hitRadius: 10,
                        hoverRadius: 4
                    }
                }
            }
        }); // eslint-disable-next-line no-unused-vars 
    }

    var createSaleTransactionChart = function(element, labels, data) {
        var cardChart3 = new Chart(element, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Total Sales',
                    backgroundColor: 'rgba(255,255,255,.2)',
                    borderColor: 'rgba(255,255,255,.55)',
                    data: data
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    xAxes: [{
                        display: false
                    }],
                    yAxes: [{
                        display: false
                    }]
                },
                elements: {
                    line: {
                        borderWidth: 2
                    },
                    point: {
                        radius: 0,
                        hitRadius: 10,
                        hoverRadius: 4
                    }
                }
            }
        });
    }

    var createEgiftUsage = function(element, labels, data) {
        var cardChart4 = new Chart(element, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Egift Usage',
                    backgroundColor: 'rgba(255,255,255,.2)',
                    borderColor: 'rgba(255,255,255,.55)',
                    data: data
                }]
            },
            options: {
                maintainAspectRatio: false,
                legend: {
                    display: false
                },
                scales: {
                    xAxes: [{
                        display: false,
                        barPercentage: 0.6
                    }],
                    yAxes: [{
                        display: false
                    }]
                }
            }
        });
    }



    var createLabelAndData = function(array) {
        var total = [];
        var month = [];

        array.forEach(r => {

            total.push(Number(r.total))
            month.push(r.month)
        });

        return {total: total, month: month};
    }


    if ($('#super-admin-dashboard').length) {

        $.ajax({
            url: base_url + 'dashboard/chart',
            dataType: 'json',
            success: (res => {  
                createChart($('#card-chart1'),res.merchant.month, res.merchant.total);

                if ($('#card-chart1-order').length) {
                    createChart($('#card-chart1-order'),res.order.month, res.order.total);
                }

                createEgiftCreationChart($('#card-chart2'), res.egift_creation.month, res.egift_creation.total);

                createSaleTransactionChart($('#card-chart3'), res.sale.month, res.sale.total);

                createEgiftUsage($('#card-chart4'), res.egift_usage.month, res.egift_usage.total);
            })
        })

    }

    var isPromo = function() {
        if ($('#egift-promo').is(':checked')) {
            $('#div-range').show();
        } 
        else {
            $('#div-range').hide();
        }
    }

    $('#egift-promo').on('click', function() {
        isPromo();
    })
    isPromo();




    var loadIncludedEgifts = function(merchant_id, id="") {
        $.ajax({
            url: base_url + "promo/included-egift-form" ,
            data: {merchant_id: merchant_id, id: id},
            method: 'get',
            dataType: 'html',
            success: (res => {
                $('#div-included-egifts').html(res);
            })
        });
    }


    if ($('#promo-merchant_id').length) {
        loadIncludedEgifts(
            $('#promo-merchant_id').val(),
            $('#promo-id').val()
            );
    }

    $('#promo-merchant_id').on('change', function() {
        loadIncludedEgifts($(this).val(), $('#promo-id').val());
    });


    $('.fa-spinner').hide();

    $('#deploy-to-branches').on('change', function() {
        if ($(this).is(':checked')) {
            $('.deploy-to-branches').prop('checked', true);
        } else {
            $('.deploy-to-branches').prop('checked', false);
        }
    });

    $('#included-egifts').on('change', function() {
        if ($(this).is(':checked')) {
            $('.included-egifts').prop('checked', true);
        } else {
            $('.included-egifts').prop('checked', false);
        }
    });



    $('.summernote').summernote({
        height: 300,
        tabsize: 2,
        followingToolbar: true,
    });

    $('.summernote-merchant').summernote({
        height: 650,
        tabsize: 2,
        followingToolbar: true,
    });


    $('.btn-generate-referral-code').on('click', function() {
        $(this).find('i').addClass('fa-spin');
        $('#egift-referral_code').val('....')
        $.ajax({
            url: base_url + "egift/generate-referral-code" ,
            success: (res => {
                $('#egift-referral_code').val(res)
                $('.btn-generate-referral-code').find('i').removeClass('fa-spin');
            })
        });

    })


    var freebiesDetails = function($freebies_id) {
        $.ajax({
            url: base_url + "freebies/details" ,
            dataType: 'html',
            data: {id: $freebies_id},
            method: 'get',
            success: (res => {
                $('.freebies-details').html(res);
            })
        });
    }


    $('#freebies-select').on('change', function() {
        freebiesDetails($(this).val());
    });



    $('.btn-add-freebies').on('click', function() {
        var freebies = $('#freebies-select');
        var qty = $('#freebies-qty');

        if (freebies.val() === null) {
            freebies.parent('div').removeClass('has-success');
            freebies.parent('div').addClass('has-error');
        } else {
            freebies.parent('div').removeClass('has-error');
            freebies.parent('div').addClass('has-success');
        }

        if (qty.val() === "") {
            qty.parent('div').removeClass('has-success');
            qty.parent('div').addClass('has-error');
        } else {
            qty.parent('div').removeClass('has-error');
            qty.parent('div').addClass('has-success');
        }


        if (freebies.val() !== null && qty.val() !== "") {
            var egift_id = 0;

            if ($('.freebies-table').length) {
                egift_id = $('#freebies-id').val();
            }

            var data = {
                freebies_id: freebies.val(),
                qty: qty.val(),
                egift_id:egift_id
            }


            addFreebies(data);
        }

        freebies.val(null);
        qty.val("");
        $('.freebies-details').html("");
// freebiesDetails(freebies.val());
});



    var addFreebies = function(data={}) {
        $('.loader-2').show();
        $.ajax({
            url: base_url + "egift-freebies/add-freebies" ,
            dataType: 'html',
            data: data,
            method: 'get',
            success: (res => {
                $('.freebies-table').html(res);
                $('.loader-2').hide();
            })
        });
    }


    var loadFreebies = function() {
        if ($('.freebies-table').length) {

            if ($('.egift-update').length) {
                addFreebies({egift_id: $('#freebies-id').val()})
            } else {
                addFreebies();
            }
        }
        $('.loader-2').hide();
    }

    var loadPriceVariety = function(egift_id=0) {
        $.ajax({
            url: base_url + "price-variety/load" ,
            data: {egift_id: egift_id},
            method: 'get',
            dataType: 'html',
            success: (res => {
                $('.price-variety').html(res);
                $('.loader').hide();
            })
        });
    }



    loadFreebies();
    loadPriceVariety($('#freebies-id').val());

    var validateInput = function(inputs=[]) {
        inputs.forEach(input => {
            if (input.val() === "" || input.val() === null) {
                input.parent('div').removeClass('has-success');
                input.parent('div').addClass('has-error');
            } else {
                input.parent('div').removeClass('has-error');
                input.parent('div').addClass('has-success');
            }
        }); 
    }

    $('.btn-add-price-variety').find('i').hide();

    $('#percent-discount').on('change', function() {

    });

    $('.btn-add-price-variety').on('click', function() {


        if($('#percent-discount').val() && $('#pricevariety-orig_price').val()) {

            var discounted = ($('#pricevariety-orig_price').val() / 100) * $('#percent-discount').val();

            discounted = discounted.toFixed(2);


            $('#pricevariety-sale_price').val($('#pricevariety-orig_price').val() - discounted);

            $('.loader').show();

            $(this).find('i').show();
            $(this).find('i').addClass('fa-spin');
            var orig_price = $('#pricevariety-orig_price');
            var sale_price = $('#pricevariety-sale_price');
            var egift_id = $('#freebies-id').val();

            validateInput([orig_price, sale_price]);


            if (orig_price.val() && sale_price.val()) {
                $.ajax({
                    url: base_url + "price-variety/add-variety" ,
                    data: {
                        orig_price: orig_price.val(), 
                        sale_price: sale_price.val(),
                        egift_id: egift_id
                    },
                    method: 'get',
                    success: (res => {
                        $(this).find('i').removeClass('fa-spin')
                        $(this).find('i').hide();
                        orig_price.val("");
                        sale_price.val("");
                        $('#percent-discount').val("");
                        loadPriceVariety(egift_id);
                        $('.loader').hide();
                    })
                });
            }  else {
                $(this).find('i').hide();
                $(this).closest('.loader').hide();
            }


        }
        else {
            alert('Original Price must be a number\nPlease fill out Original Price and Discount Percentage.');
        }

    });

    $(document).on('click', '.btn-remove-price-variety', function() {
        $('.loader').show();


        var id = $(this).data('id');

        $.ajax({
            url: base_url + "price-variety/remove-variety" ,
            data: {id: id},
            method: 'get',
            success: (res => {
                loadPriceVariety($('#freebies-id').val());  
            })
        });
    });



    $(document).on('click', '.btn-remove-freebies', function() {
        $('.loader-2').show();
        var id = $(this).data('id');

        $.ajax({
            url: base_url + "egift-freebies/remove-freebies" ,
            data: {id: id},
            method: 'get',
            success: (res => {
                loadFreebies();
                $('#freebies-select').val(null);
                $('#freebies-qty').val("");
                $('.freebies-details').html("");
                $('.loader-2').hide();
            })
        });
    });









    $('.natures').on('click', function() {
        if ($(this).is(':checked')) {
            $(this).parents('li').addClass('list-group-item-primary')
        } else {
            $(this).parents('li').removeClass('list-group-item-primary')
        }
    })

    $('.btn-logout').on('click', function() {
        $('#frm-logout').submit();
    });

    var showLoader = function() {
        $('.fa-spinner').addClass('fa-spin');
        $('.fa-spinner').show();
// $('#image-preview').hide();
}

$('#profile-logo_input').on("change", function() {
    showLoader();
    previewImage('profile-logo_input');
});


$('#egift-image_banner_input').on("change", function() {
    showLoader();
    previewImage('egift-image_banner_input', '#image-preview-banner');
});

$('#profile-logo_banner_input').on("change", function() {
    showLoader();
    previewImage('profile-logo_banner_input', '#image-preview-banner');
});


$('#egift-image_input').on("change", function() {
    showLoader();
    previewImage('egift-image_input');

});


$('#freebies-image_input').on("change", function() {
    showLoader();
    previewImage('freebies-image_input');
});


$('#about-logo_input').on("change", function() {
    showLoader();
    previewImage('about-logo_input');
});

$('#personnel-logo_input').on("change", function() {
    showLoader();
    previewImage('personnel-logo_input');
});





function previewImage(id, holder="") {
    var oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById(id).files[0]);

    oFReader.onload = function(oFREvent) {
        if (holder === "") {
            $('#image-preview').attr('src', oFREvent.target.result);
            $('#image-preview').show();
        }
        else {
            $(holder).attr('src', oFREvent.target.result);
            $(holder).show();
        }

        $('.fa-spinner').removeClass('fa-spin');
        $('.fa-spinner').hide();
    };
}


$(".delete").on("click", function() {
    var id = $(this).data("key");
    var page = $(this).data("page");
    var selected = $(this).data("selected");
    swal({
        title: "Are you sure?",
        text: "You are going to delete " + selected,
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, delete it!",
        closeOnConfirm: false
    }, function () {
        $.ajax({
            url: base_url + page + "/delete" ,
            method: "post",
            data: {id: id},
            success: (response => {
                swal({
                    title: "Deleted! ",
                    text: selected +" was deleted!",
                    type: "success",
                    showCancelButton: false,
                    confirmButtonColor: "#337ab7",
                    confirmButtonText: "Done",
                    closeOnConfirm: false
                }, function () {
                    window.location.href = base_url + page;
                });
            })
        });
    });
});



if ($('.profile-index').length) {
    var pos = $('th').text().search("Status");

    if (pos) {
        $('th').css('color', '#20a8d8')
    } 
}


$(document).on('mouseleave', '.sortable', function() {

    var parent_key = $(this).parent('.main-menu-panel').data('key')

    $(this).find('input').each(function() {
        var sub_menu_name = $(this).attr('name')

        var s = sub_menu_name.slice(0, 17);
        var e = sub_menu_name.slice(32);

        var new_name = s + parent_key + e

        $(this).attr('name', new_name)
    });
});



$('.sortable').sortable({
    connectWith: '.sortable',
    placeholder: 'ui-state-highlight',
}).disableSelection();

$('.main-menu-sortable').sortable({
    connectWith: '.main-menu-sortable',
    placeholder: 'ui-state-highlight',
}).disableSelection();


 

$('input[name="EgiftSearch[date_start]"]').attr('type', 'date');
$('input[name="EgiftSearch[date_end]"]').attr('type', 'date');






if ($('#main-chart').length) { 
    createMainChart();
}

$('#select-main-chart').on('change', function() {
    createMainChart($(this).val());
});


});




var createMainChart = function(year='') {
    $('#main-chart-wrapper').html("");
    $.ajax({
        url: base_url + 'dashboard/main-chart',
        dataType: 'json',
        data: {year: year},
        method: 'get',
        success: (res => { 
            $('#main-chart-wrapper').html('<canvas class="chart" id="main-chart" height="250"></canvas>');
            var mainChart = new Chart($('#main-chart'), {
                type: 'line',
                data: {
                    labels: res.egift_creation.month,
                    datasets: [{
                        label: 'Egift Creation',
                        backgroundColor: hexToRgba(getStyle('--info'), 10),
                        borderColor: getStyle('--info'),
                        pointHoverBackgroundColor: '#63c2de',
                        borderWidth: 2,
                        data: res.egift_creation.total
                    }, {
                        label: 'Egift Usage',
                        backgroundColor: 'transparent',
                        borderColor: getStyle('--success'),
                        pointHoverBackgroundColor: '#f86c6b',
                        borderWidth: 2,
                        data: res.egift_usage.total
                    }, 
                    // {
                    //     label: 'Egift Sales',
                    //     backgroundColor: 'transparent',
                    //     borderColor: getStyle('--danger'),
                    //     pointHoverBackgroundColor: '#4dbd74',
                    //     borderWidth: 1,
                    //     borderDash: [8, 5],
                    //     data: res.sale.total
                    // }
                    ]
                },
                options: {
                    maintainAspectRatio: false,
                    legend: {
                        display: false
                    },
                    scales: {
                        xAxes: [{
                            gridLines: {
                                drawOnChartArea: false
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                maxTicksLimit: 5,
                                // stepSize: Math.ceil(250 / 5),
                                // max: 250
                            }
                        }]
                    },
                    elements: {
                        point: {
                            radius: 0,
                            hitRadius: 10,
                            hoverRadius: 4,
                            hoverBorderWidth: 3
                        }
                    }
                }
            });

        })
    });
}

var createCustomChart = function(params) {

    $(params.wrapper).html("");
    $.ajax({
        url: base_url + params.url,
        dataType: 'json',
        data: params.data,
        method: 'get',
        success: (res => { 

            $('#' +params.wrapper).html('<canvas class="chart" id="chart-id" height="70"></canvas>');
            var mainChart = new Chart($('#chart-id'), {
                type: params.chart_type,
                data: {
                    labels: res.label,
                    datasets: [{
                        label: params.label,
                        backgroundColor: hexToRgba(getStyle('--info'), 10),
                        borderColor: getStyle('--info'),
                        pointHoverBackgroundColor: '#63c2de',
                        borderWidth: 2,
                        data: res.total
                    }]
                },
                options: {
                    maintainAspectRatio: true,
                    legend: {
                        display: true
                    },
                    scales: {
                        xAxes: [{
                            gridLines: {
                                drawOnChartArea: true
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                maxTicksLimit: 5,
                            }
                        }]
                    },
                    elements: {
                        point: {
                            radius: 0,
                            hitRadius: 10,
                            hoverRadius: 4,
                            hoverBorderWidth: 3
                        }
                    }
                }
            });

        })
    });
}
