$( function() {
    $( ".dlayout" ).sortable({
      connectWith: ".dlayout",
      handle: ".col-md-6",
      cancel: ".portlet-toggle",
      placeholder: "portlet-placeholder ui-corner-all"
    });
});




// Global fields

var preEvent='';

//This function calls at drag
function drag(ev) {
    ev.dataTransfer.setData("control",ev.target.getAttribute("data-type"));
    //console.log("In Drag");
}

// this function start at drop
function allowDrop(ev) {
    ev.preventDefault();
}

function drop(ev) {
    ev.preventDefault();
    var controlType = ev.dataTransfer.getData("control");
    var tragetID=ev.target.id;
    console.log(ev.target+" ---- "+tragetID+"..."+controlType);
    if(controlType=="dButton"){
      addButtonControl(ev);
    }else if (controlType=="dLayout") {
      generateLayout(ev);
    }else if (controlType=="dInput") {
      addInputControl(ev);
    }else if (controlType=="dMenu") {
      addMenuControl(ev,tragetID);
    }else if (controlType=="dLable") {
      addLableControl(ev);
    }else if (controlType=="dParagraph") {
      addParagraphControl(ev);
    }else if (controlType=="dEColumn") {
      addEColumnControl(ev);
    }else if (controlType=="dHeader") {
      addHeaderControl(ev);
    }else if (controlType=="dDropDown") {
      addDropDownControl(ev);
    }else if (controlType=="dTabLayout") {
      generateTabLayout(ev);
    }else{
      ev.preventDefault();
    }
}


// Used this function to place the HTML

function placeHtml(ev,placehtml) {
  $(ev.target).parents().each(function(){
    if($(this).attr('data-layout')=='row'){
      if(ev.target.getAttribute('data-draggable')=='true' && ev.target.id!='MainDragLayout' ){
        $(ev.target).before(placehtml);
        $(ev.target).remove();
      }
      return false;
    }
  });
}

// Used to generate the dropdown menu

function addDropDownControl(ev){
    html="<div id="+idGen('col')+" class='col-md-6' data-Controlset='{"+'"controlType"'+":"+'"dropdown"'+"}' data-select='col' data-edit='regenerate'><div class='dcol' data-select='col' onclick='enableborderforcolumn(event)'><select disabled><option  selected>Select</option></select> <a href='#' style='float:right' id='settingElement' data-edit='remove'><span class='' data-select='colSetting'></span></a><a href='#' style='float:right' id='delElement' data-edit='remove'><span class='' data-select='coldel'></span></a></div></div> <div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div>";
    placeHtml(ev,html);
}


// This function used to generate the Tab

function generateTabLayout(ev){
    //$('div[id^="TabContainer_"]').tabs();
    if($(ev.target).attr('id')=='MainDragLayout'){
        var beginhtml="<fieldset class='fldset' data-layout-type='TabLayout'  data-edit='merge'><legend class='fldset' data-edit='remove'><span id='lngTitle'>Tab Group Layout <a href='#' style='float:right' id='delElement' data-edit='remove'><span class='glyphicon glyphicon-remove' data-select='tabcontainerdel'></span></a></span></legend><div class='container-fluid' id='"+idGen("Tablayout")+"' data-select='Tablayout' data-Controlset='{"+'"controlType"'+":"+'"Tablayout"'+","+'"layout_style"'+":"+'""'+","+'"layout_class"'+":"+'"container-fluid"'+"}' data-edit='regenerate'>";
        var tagID = idGen("Tab");
        var tabContainer = idGen("TabContainer");
        //var middlehtml="<div class='dlayout' data-edit='merge'><div class='row' data-layout='row' id='"+idGen("row")+"'><div id = '"+tabContainer+"'><ul><li><a href = '#"+tagID+"'>Tab</a><span data-draggable='true' data-edit='remove'>Drop</span></li><li><a href = '#"+tagID+"2'>Tab2</a><span data-draggable='true' data-edit='remove'>Drop</span></li></ul><div id = '"+tagID+"'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Section Here</div></div><div id = '"+tagID+"2'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div></div></div></div></div></div>";
        //var middlehtml="<div class='dlayout' data-edit='merge'><div class='row' data-layout='row' id='"+idGen("row")+"'><div id = '"+tabContainer+"'><ul><li><a href = '#"+tagID+"'><span>Tab</span></a><span data-draggable='true' data-edit='remove' onmouseover='enableborder(event)' onmouseout='disableborder(this)' style='padding-bottom: 10px;' data-tab='true' data-tabid='"+tabContainer+"'>&nbsp;&nbsp;</span></li></ul><div id = '"+tagID+"' onclick='enableborder(event)'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Section Here</div></div></div></div></div></div>";
        //var middlehtml="<div class='dlayout' data-edit='merge'><div class='row' data-layout='row' id='"+idGen("row")+"'><div id = '"+tabContainer+"'><ul data-tabid='"+tabContainer+"'><li><a href = '#"+tagID+"'><span>tagID</span></a><span data-draggable='true' data-edit='remove' onmouseover='enableborder(event)' onmouseout='disableborder(this)' style='padding-bottom: 10px;' data-tab='true' data-tabid='"+tabContainer+"'>&nbsp;&nbsp;</span></li><li><a href = '#"+tagID+"2'><span>tagID+'2'</span></a><span data-draggable='true' data-edit='remove' onmouseover='enableborder(event)' onmouseout='disableborder(this)' style='padding-bottom: 10px;' data-tab='true' data-tabid='"+tabContainer+"'>&nbsp;&nbsp;</span></li></ul><div id = '"+tagID+"' onclick='enableborder(event)'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Section Here</div></div><div id = '"+tagID+"2' onclick='enableborder(event)'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Section Here</div></div></div></div></div></div>";
        var middlehtml="<div class='dlayout' data-edit='merge'><div class='row' data-layout='row' id='"+idGen("row")+"'><div class='col-md-12'><div id = '"+tabContainer+"'><ul data-tabid='"+tabContainer+"'><li><a href = '#"+tagID+"'>Tab</a><a href='#' style='float:right' id='delElement' data-edit='remove'><span class='glyphicon glyphicon-remove' data-select='tabdel'></span></a><span data-draggable='true' data-edit='remove' onmouseover='enableborderAddTab(event)' onmouseout='disableborderAddTab(event)' ondragover='enableborderAddTab(event)' ondragleave='disableborderAddTab(event)' style='padding-bottom: 10px;' data-tab='true' data-tabid='"+tabContainer+"'>&nbsp;&nbsp;</span></li></ul><div id = '"+tagID+"' onclick='enableTabborder(event)' data-select='Tablayout' data-Controlset='{"+'"controlType"'+":"+'"Tab"'+","+'"Tab_style"'+":"+'""'+","+'"Tab_class"'+":"+'""'+"}' ><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div><p>&nbsp;&nbsp;</p></div></div></div></div></div></div>";
        //var script = "<script>$(function() {var tabs = $( '#"+tabContainer+"').tabs();tabs.find( '.ui-tabs-nav' ).sortable({ axis: 'x', stop: function() {   tabs.tabs( 'refresh' );   }    });});</script>";
        var script = "<script>$('div[id^='"+"TabContainer_"+"']').tabs();</script>";
        var fldset=document.createElement("fieldset");
        ev.target.appendChild(fldset);
        var endhtml="</div></fieldset>";
        fldset.outerHTML=beginhtml+middlehtml+endhtml+script;
        var tabs=$('div[id^="TabContainer_"]').tabs();
        tabs.tabs("option", "heightStyle", "auto");
        tabs.tabs("option", "border", "2px solid red");
        tabs.find( "ul[data-tabid='"+tabContainer+"']" ).sortable({ axis: 'x', stop: function() { tabs.tabs( 'refresh' );   }    });
    }if($(ev.target).attr('data-tab')=='true'){
        var tabs=$('#'+$(event.target).attr('data-tabid')).tabs();
        var tabContainer = $(event.target).attr('data-tabid');
        var tagID = idGen("Tab");
        li = "<li><a href = '#"+tagID+"'>Tab</a><a href='#' style='float:right' id='delElement' data-edit='remove'><span class='glyphicon glyphicon-remove' data-select='tabdel'></span></a><span data-draggable='true' data-edit='remove' onmouseover='enableborderAddTab(event)' onmouseout='disableborderAddTab(event)' ondragover='enableborderAddTab(event)' ondragleave='disableborderAddTab(event)' style='padding-bottom: 10px;' data-tab='true' data-tabid='"+tabContainer+"'>&nbsp;&nbsp;</span></li>";
        //li = "<li><a href = '#"+tagID+"'>Tab</a></li>";
        tabs.find( "ul[data-tabid='"+tabContainer+"']" ).append( li );
        tabs.append( "<div id ='"+tagID+"' onclick='enableTabborder(event)' data-select='Tablayout' data-Controlset='{"+'"controlType"'+":"+'"Tab"'+","+'"Tab_style"'+":"+'""'+","+'"Tab_class"'+":"+'""'+"}'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div><p>&nbsp;&nbsp;</p></div>" );
        tabs.tabs("refresh");
    }

}



//This function used to add empty column
function addEColumnControl(ev){
    var html="<div id="+idGen('col')+" class='col-md-6' data-Controlset='{"+'"controlType"'+":"+'"emptycontol"'+"}' data-select='col' data-edit='regenerate'><div class='dcol' data-select='col' onclick='enableborderforcolumn(event)'><span class='emptyCell'><div data-edit='remove'>Empty Cell</div></span> <a href='#' style='float:right' id='delElement' data-edit='remove'><span class='' data-select='coldel'></span></a> </div></div> <div class='col-md-6 dcol'data-draggable='true' data-edit='remove'>Drop Here</div>";
    placeHtml(ev,html);
}


//This function used to generate layout
function generateLayout(ev){
  //ev=gEvent;
  if($(ev.target).attr('id')=='MainDragLayout'){
        var beginhtml="<fieldset class='fldset' data-layout-type='Layout'  data-edit='merge'><legend class='fldset' data-edit='remove'><span id='lngTitle' onclick='enableborderforlayout(event)' data-select='layout'>Layout<a href='#' style='float:right' id='delElement' data-edit='remove'><span class='' data-select='laydel'></span></a></span></legend><div class='container-fluid' id='"+idGen("layout")+"' data-select='layout' data-Controlset='{"+'"controlType"'+":"+'"layout"'+","+'"layout_style"'+":"+'""'+","+'"layout_class"'+":"+'"container-fluid"'+"}' data-edit='regenerate'>";
        var middlehtml="<div class='dlayout' data-edit='merge'><div class='row' data-layout='row' id='"+idGen("row")+"'><div data-edit='merge' class='dragposition'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div></div></div></div>";
        var fldset=document.createElement("fieldset");
        ev.target.appendChild(fldset);
        var endhtml="</div></fieldset>";
        fldset.outerHTML=beginhtml+middlehtml+endhtml;
    }else{
      var beginhtml="<div class='col-md-6' id='"+idGen("col")+"'><fieldset class='fldset' data-layout-type='Layout' data-edit='merge'><legend class='fldset' data-edit='remove'><span id='lngTitle' data-select='layout' onclick='enableborderforlayout(event)'>Layout <a href='#' style='float:right' id='delElement' data-edit='remove'><span class='' data-select='laydel'></span></a></span></legend><div data-select='layout' data-Controlset='{"+'"controlType"'+":"+'"layout"'+","+'"layout_style"'+":"+'""'+","+'"layout_class"'+":"+'"container-fluid"'+"}' class='container-fluid' id='"+idGen("layout")+"' data-edit='regenerate'>";
      var middlehtml="<div class='dlayout' data-edit='merge'><div class='row' data-layout='row' id='"+idGen("row")+"'><div data-edit='merge' class='dragposition'><div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div></div></div></div>";
      //var fldset=document.createElement("fieldset");
      //ev.target.appendChild(fldset);
      var endhtml="</div></fieldset></div>";
      outerHTML=beginhtml+middlehtml+endhtml;
      $(ev.target).before(outerHTML);

      //$(ev.target).remove();

    }
    $( ".dragposition" ).sortable({
      connectWith: ".dragposition",
      handle: ".dcol",
      cancel: ".portlet-toggle",
      placeholder: "portlet-placeholder ui-corner-all"
    });
}
//Used to add label control to target
function addLableControl(ev){
        html="<div id="+idGen('col')+" class='col-md-6' data-Controlset='{"+'"controlType"'+":"+'"label"'+"}' data-select='col' data-edit='regenerate' ><div class='dcol' data-select='col' onclick='enableborderforcolumn(event)'><label> Text Field </label> <a href='#' style='float:right' id='delElement' data-edit='remove'><span class='' data-select='coldel'></span></a></div></div> <div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div>";
    placeHtml(ev,html);
}

//Used to add Button control to target
function addButtonControl(ev){
    html="<div id="+idGen('col')+" class='col-md-6' data-Controlset='{"+'"controlType"'+":"+'"button"'+"}' data-select='col' data-edit='regenerate'><div class='dcol' data-select='col' onclick='enableborderforcolumn(event)'><input type='button' value='Button'> <a href='#' style='float:right' id='delElement' data-edit='remove'><span class='' data-select='coldel'></span></a></div></div> <div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div>";
    placeHtml(ev,html);
}

//Used to add input control
function addInputControl(ev){
    html="<div id="+idGen('col')+" class='col-md-6' data-Controlset='{"+'"controlType"'+":"+'"input"'+"}' data-select='col' data-edit='regenerate'><div class='dcol' data-select='col' onclick='enableborderforcolumn(event)'><label for='InputText'> Input Text </label> <input name='InputText' > <a href='#' style='float:right' id='delElement' data-edit='remove' ><span class='' data-select='coldel'></span></a></div></div> <div class='col-md-6 dcol' data-draggable='true' data-edit='remove'>Drop Here</div>";
    placeHtml(ev,html);
}
//Control the Fields

$(document).on('click','#TopFieldSetID',function(e){
    if($(preEvent).attr('data-select')=='layout'){
        $(preEvent).find('.dlayout').css({border:'',display:''});
    }else{
        $(preEvent).find('.ui-tabs-panel').css({border:'',display:''});
        $(preEvent).find('.dcol').css({border:'',display:''});
        $(preEvent).find('span').removeClass('glyphicon glyphicon-remove');
    }
    var exitloop = false;
    console.log($(e.target))
    $(e.target).parents().each(function(){
        if($(this).attr('data-select')=='layout1'){
            exitloop = true;
            preEvent=$(this);
            $(this).find('.dlayout').css({display:'flow-root',border:'1px solid blue'});
            var controlData = JSON.parse($(this).attr('data-Controlset'));
            if(controlData.controlType=='layout'){
                controlData.UIElement="MM/UI_Settings_layout.html";
            }
            if(controlData.controlType=='layout_column'){
                controlData.UIElement="MM/UI_Settings_layoutcolumn.html";
            }
            controlData.id=$(this).attr('id');
                controlData.layout_class=$(this).attr('class');
                controlData.layout_style=$(this).attr('style')
                //controlData.UIElement="MM/UI_Settings_label.html";

                var controlDataString=JSON.stringify(controlData);
                $(this).attr('data-Controlset',controlDataString);
                //console.log(controlData);
                $.ajax({
                    type: "POST",
                    url: '/UIInclude',
                    data:controlData,
                    success: function(data){
                      console.log(data);
                      $("#OptionsID").html(data.html);
                    },
                     error: function (request, status, error) {
                     console.log(error);
                      }
                  });
        }
        if($(this).attr('data-select')=='col1'){
            exitloop = true
            $(this).find('.dcol').css({display:'flow-root',border:'1px solid blue'});
            $(this).find('span').addClass('glyphicon glyphicon-remove');
            preEvent=$(this);
            var controlData = JSON.parse($(this).attr('data-Controlset'));
            if(controlData.controlType=='label'){
                controlData.UIElement="MM/UI_Settings_label.html";
            }
            if(controlData.controlType=='button'){
                controlData.UIElement="MM/UI_Settings_Button.html";
            }
            if(controlData.controlType=='input'){
                controlData.UIElement="MM/UI_Settings_input.html";
            }
            if(controlData.controlType=='emptycontol'){
                controlData.UIElement="MM/UI_Settings_column.html";
            }


                controlData.id=$(this).attr('id');
                controlData.column_class=$(this).attr('class');
                controlData.column_style=$(this).attr('style')
                //controlData.UIElement="MM/UI_Settings_label.html";

                var controlDataString=JSON.stringify(controlData);
                $(this).attr('data-Controlset',controlDataString);
                //console.log(controlData);
                $.ajax({
                    type: "POST",
                    url: '/UIInclude',
                    data:controlData,
                    success: function(data){
                      console.log(data);
                      $("#OptionsID").html(data.html);
                    },
                     error: function (request, status, error) {
                     console.log(error);
                      }
                  });
                //$('#OptionsID').load('/UIInclude',controlData);
                //OptionsIDHtml='<div><label >Property: <input type="text" data-type="Propery"></label><input type="button" value="Save"></div>';
                //$('#OptionsID').html(OptionsIDHtml);
            //}
            //console.log(controlData);
        }

        if(exitloop){
            console.log(exitloop);
            return false;
        }
    });
});

$.fn.serializeObject = function() {
	var o = {};
	var a = this.serializeArray();
	$.each(a, function() {
		if (o[this.name]) {
			if (!o[this.name].push) {
				o[this.name] = [o[this.name]];
			}
			o[this.name].push(this.value || '');
		} else {
			o[this.name] = this.value || '';
		}
	});
	return o;
};

$(document).on('submit','#label_settings_form',function(e){
    e.preventDefault();
    //data = $(this).serializeObject();
       $.ajax({ data: $(this).serialize(),
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                success: function(response) {
                    var controlData = JSON.parse(response.responseData.response);
                     console.log(controlData);
                     $("#label_settings_form").html(response.html);
                     //console.log(response.responseData.controlType);
                     $("#"+controlData.id).attr('data-controlset',response.responseData.response);
                     $("#"+controlData.id).attr('class',controlData.column_class);
                     $("#"+controlData.id).attr('style',controlData.column_style);
                     if(controlData.controlType=='button'){
                        //console.log($("#"+controlData.id).find('input'))
                        $("#"+controlData.id).find('input').attr('value',controlData.button_property_value);
                     }
                     if(controlData.controlType=='label'){
                        $("#"+controlData.id).find('label').text(controlData.label_property_property);
                     }
                     if(controlData.controlType=='input'){
                        $("#"+controlData.id).find('label').text(controlData.input_property_label);
                        $("#"+controlData.id).find('label').attr('for',controlData.input_property_property);
                        $("#"+controlData.id).find('input').attr('name',controlData.input_property_property);
                        $("#"+controlData.id).find('input').attr('class',controlData.property_property_class);
                        $("#"+controlData.id).find('input').attr('style',controlData.property_property_style);
                        $("#"+controlData.id).find('label').attr('class',controlData.label_property_class);
                        $("#"+controlData.id).find('label').attr('style',controlData.label_property_style);
                     }
                     if(controlData.controlType=='layout'){
                        $("#"+controlData.id).attr('class',controlData.layout_class);
                        $("#"+controlData.id).attr('style',controlData.layout_style);
                     }if(controlData.controlType=='Tab'){
                        console.log($("#"+controlData.id))
                        $("#"+controlData.id).attr('class',controlData.tab_class);
                        $("#"+controlData.id).attr('style',controlData.tab_style);
                        $('a[href=#'+controlData.id+']').text(controlData.tab_name);
                     }
                     if(response['success']) {
                         //$("#label_settings_form").html("Hello World");
                         //$("#feedbackform").addClass("hidden");
                     }
                     if(response['error']) {
                         /*$("#feedbackmessage").html("<div class='alert alert-danger'>" +
			                   response['error']['comment'] +"</div>");*/
                     }
                },
                error: function (request, status, error) {
                     console.log(request.responseText);
                }
       });
});


$(document).on('submit','#new_form',function(e){
    event.preventDefault();
    //data = $(this).serializeObject();
       $.ajax({ data: $(this).serialize(),
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                success: function(response) {
                    //var controlData = JSON.parse(response);
                     controlData=response.response;
                     //console.log(response.response);
                     //$("#label_settings_form").html(response.html);
                     //console.log(controlData.responseData.datalocation);
                     addDynamicTab(controlData);



                     if(response['success']) {
                         //$("#label_settings_form").html("Hello World");
                         //$("#feedbackform").addClass("hidden");
                     }
                     if(response['error']) {
                         /*$("#feedbackmessage").html("<div class='alert alert-danger'>" +
			                   response['error']['comment'] +"</div>");*/
                     }
                },
                error: function (request, status, error) {
                     console.log(request.responseText);
                }
       });
});

/*$(document).keyup(function(e) {
    console.log(e.which);
});
*/

// Used to set open the properties
$(document).on('click','#settingElement',function(ev){
    console.log($(ev.target).closest('div[id^=col_]'));
    target = $(ev.target).closest('div[id^=col_]');
    var controlData = JSON.parse($(target).attr('data-Controlset'));
    if(controlData.controlType=='dropdown'){
        //controlData.UIElement="MM/UI_Settings_dropdown.html";
        controlData.UIElement="MM/DpSettings.html";
        }
     controlData.id=$(target).attr('id');
     controlData.column_class=$(target).attr('class');
     controlData.column_style=$(target).attr('style');
        //controlData.UIElement="MM/UI_Settings_label.html";
     var controlDataString=JSON.stringify(controlData);
     $(target).attr('data-Controlset',controlDataString);
    $.ajax({
            type: "POST",
            url: '/UIInclude',
            data:controlData,
            success: function(data){
              console.log(data);
              dialog = $( "#my_popup" ).dialog({
                  autoOpen: false,
                  height: "auto",
                  width: "auto",
                  modal: true,
                  buttons: {
                    Cancel: function() {
                      dialog.dialog( "close" );
                    }
                  },
                  close: function() {
                    //allFields.removeClass( "ui-state-error" );
                    dialog.dialog( "close" );
                  }
                });
              $("#my_popup").html(data.html);
              //$("#my_popup").popup('show');
              dialog.dialog( "open" );

            },
             error: function (request, status, error) {
             console.log(error);
              }
          });

});

// Used to delete the element
$(document).on('click','#delElement',function(ev){
    if($(ev.target).attr('data-select')=='coldel'){
        $(ev.target).closest('div[id^=col_]').remove();
    }if($(ev.target).attr('data-select')=='laydel'){
        $(ev.target).closest('fieldset').remove();
    }if($(ev.target).attr('data-select')=='tabcontainerdel'){
        $(ev.target).closest('fieldset').remove();
    }if($(ev.target).attr('data-select')=='tabdel'){
        //console.log($(ev.target).closest('a').prev('a[href^=#Tab_]'));
        var atag = $(ev.target).closest('a').prev('a[href^=#Tab_]');
        //var litag = $(atag).closest( "li" );
        var tabgroupid = $(atag).closest("ul").attr('data-tabid');

        if(tabsCount('#'+tabgroupid)>1){
            var tabs = $('#'+tabgroupid).tabs();
            var tabIndex=id2Index('#'+tabgroupid,$(atag).attr('href'));
            $(atag).closest( "li" ).remove();
            $($(atag).attr('href')).remove();
            tabs.tabs("refresh");

            $('#'+tabgroupid).tabs("option","active",tabIndex-1);
        }else{
            $(ev.target).closest('fieldset').remove();
        }

    }
    //console.log($(ev.target));
    //$(e.target).closest('[data-select=col]').remove();
});

function enableborderforcolumn (ev){
    disableborderPreviousEvent(ev);
    preEvent = ev;
    if($(ev.target).attr('data-select')=='col'){
        $(ev.target).css({display:'flow-root',border:'2px solid blue'});
        //$(ev.target).closest('fieldset').css({display:'flow-root',border:'2px solid blue'});
        //console.log($(ev.target).closest('legend').find('span'));
        //$(ev.target).closest('legend').find('span').addClass('glyphicon glyphicon-remove');
    $(ev.target).find('span[data-select=colSetting]').addClass('glyphicon glyphicon-cog');
    $(ev.target).find('span[data-select=coldel]').addClass('glyphicon glyphicon-remove');

    console.log($(ev.target).closest('div[id^=col_]'));
    target = $(ev.target).closest('div[id^=col_]');
    var controlData = JSON.parse($(target).attr('data-Controlset'));
    if(controlData.controlType=='label'){
                controlData.UIElement="MM/UI_Settings_label.html";
     }
     if(controlData.controlType=='button'){
        controlData.UIElement="MM/UI_Settings_Button.html";
        }
    if(controlData.controlType=='input'){
        controlData.UIElement="MM/UI_Settings_input.html";
        }
    if(controlData.controlType=='emptycontol'){
        controlData.UIElement="MM/UI_Settings_column.html";
        }
    if(controlData.controlType=='dropdown1'){
        controlData.UIElement="MM/UI_Settings_dropdown.html";
        }
     controlData.id=$(target).attr('id');
     controlData.column_class=$(target).attr('class');
     controlData.column_style=$(target).attr('style');
        //controlData.UIElement="MM/UI_Settings_label.html";
     var controlDataString=JSON.stringify(controlData);
     $(target).attr('data-Controlset',controlDataString);
    processAjaxHtmlRequest(controlData);
    //element.style.border = "2px dotted green";
    //element.style.backgroundColor = "red";
    }

}

function disableborderPreviousEvent(ev){
    if($(preEvent.target).attr('data-select')=='col'){
        $(preEvent.target).css({display:'',border:''});
        $(preEvent.target).find('span').removeClass('glyphicon glyphicon-remove glyphicon-cog');
    }if($(preEvent.target).attr('data-select')=='layout'){
        $(preEvent.target).closest('fieldset').css({display:'',border:''});
        $(preEvent.target).removeClass('glyphicon glyphicon-remove');
    }if($(preEvent.target).attr('data-select')=='Tablayout'){
        $(preEvent.target).css({display:'',border:''});
        var tabs = $(preEvent.target).closest('div[id^=Tablayout_]').tabs();
        tabs.tabs("refresh");
    }

}


function disableborder(element){
    element.style.border = "";
    element.style.backgroundColor = "";
}


function processAjaxHtmlRequest(controlData){
    $.ajax({
            type: "POST",
            url: '/UIInclude',
            data:controlData,
            success: function(data){
              console.log(data);
              $("#OptionsID").html(data.html);
            },
             error: function (request, status, error) {
             console.log(error);
              }
          });
}

function enableborderforlayout(ev){
    disableborderPreviousEvent(ev);
    preEvent = ev;
    //$(ev.target).css({display:'flow-root',border:'2px solid blue'});
    //$(ev.target).find('span').addClass('glyphicon glyphicon-remove');
    if($(ev.target).attr('data-select')=='layout'){
        $(ev.target).closest('fieldset').css({display:'flow-root',border:'2px solid blue'});
        $(ev.target).find('span').addClass('glyphicon glyphicon-remove');
        var target = $(ev.target).closest('fieldset').find('div[id^=layout_]')[0];


        var controlData = JSON.parse($(target).attr('data-Controlset'));
            if(controlData.controlType=='layout'){
                controlData.UIElement="MM/UI_Settings_layout.html";
            }
            if(controlData.controlType=='layout_column'){
                controlData.UIElement="MM/UI_Settings_layoutcolumn.html";
            }
            controlData.id=$(target).attr('id');
            controlData.layout_class=$(target).attr('class');
            controlData.layout_style=$(target).attr('style')
                //controlData.UIElement="MM/UI_Settings_label.html";

                var controlDataString=JSON.stringify(controlData);
                $(target).attr('data-Controlset',controlDataString);
                processAjaxHtmlRequest(controlData);

    }
    console.log($(ev.target));
    //target = $(ev.target).closest('[data-select=col]');
    //var controlData = JSON.parse($(target).attr('data-Controlset'));

}

function enableborderAddTab(ev){
    $(ev.target).css({display:'flow-root',border:'2px solid blue'});
    //console.log($(ev.target))
}

function disableborderAddTab(ev){
    $(ev.target).css({display:'',border:''});
}

function enableTabborder(ev){
     if($(ev.target).attr('data-select')=='Tablayout'){
         disableborderPreviousEvent(ev);
         preEvent = ev;
         $(ev.target).css({display:'flow-root',border:'2px solid blue'});
         var target = $(ev.target);
         var controlData = JSON.parse($(target).attr('data-Controlset'));
         controlData.UIElement="MM/UI_Settings_Tab.html";
         controlData.id=$(target).attr('id');
         controlData.tab_class=$(target).attr('class');
         controlData.tab_style=$(target).attr('style');
         var controlDataString=JSON.stringify(controlData);
         $(target).attr('data-Controlset',controlDataString);
         processAjaxHtmlRequest(controlData);
     }

}

function addPropertyrow(ev){
    console.log(ev);
    closerow =$(ev.target).closest('.form-row');
    hideid=idGen("hide");
    //closerow.append('<div class="form-group col-md-6"><label for="'+hideid+'">Property Name</label><input type="input" class="form-control" id="'+hideid+'" placeholder="Property Name"></div>');
    $(ev.target).closest('.form-row').find('.form-group.col-md-6').find('.form-row').append('<div class="form-group col-md-12"><input type="input" class="form-control" id="'+hideid+'" name="'+hideid+'" placeholder="Property Name" value=""></div');
}