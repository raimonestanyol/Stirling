google.charts.load('current', {'packages':['line']});  
  
$( function() {
var from = $( "#fromDate" )
    .datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true
    })
    .on( "change", function() {
        to.datepicker( "option", "minDate", getDate( this ) );
    }),
to = $( "#toDate" ).datepicker({
    dateFormat: "yy-mm-dd",
    changeMonth: true,
    changeYear: true
})
    .on( "change", function() {
    from.datepicker( "option", "maxDate", getDate( this ) );
    });
from.attr("autocomplete","off")
to.attr("autocomplete","off")

function getDate( element ) {
    var date;
    var dateFormat = "yy-mm-dd";
    try {
    date = $.datepicker.parseDate( dateFormat, element.value );
    } catch( error ) {
    date = null;
    }
    return date;
}

function strDate( element, addDays ) {
    var selectedDate = getDate( element )
    selectedDate.setDate(selectedDate.getDate() + addDays);
    return reprDate( selectedDate )
};
function reprDate( selectedDate ){
    var selectedDate= new Date(selectedDate)
    var month = selectedDate.getMonth() + 1
    month = month.toString().padStart(2, '0')
    var day = selectedDate.getDate().toString().padStart(2, '0')
    var year = selectedDate.getFullYear().toString()
    return year+month+day;
};//20210409
var toDate = new Date();
var fromDate = new Date();
toDate.setDate(toDate.getDate() + 1);
fromDate = reprDate(fromDate)
toDate = reprDate(toDate);

$("#fromDate").change(function() {
    fromDate = strDate(this, 0)
    retrieveData(fromDate,toDate)
});
$("#toDate").change(function() {
    toDate = strDate(this, 1)
    retrieveData(fromDate,toDate)
});

google.charts.setOnLoadCallback(drawChart);
var columns=["DATETIME","AMB_T","BOILER_T","HEAT_T_CON","HEAT_T_LIM","COOL_FLOW","COOL_T_IN","COOL_T_OUT","CURRENT","VOLTAGE","E_POWER","E_ENERGY","T_POWER","STATUS"]
columns.shift()
graphVars = {}
function addVarSelector(){
    var varCheckboxArray = columns.map(name => {
    return `
        <div class='${name}'>
        <input class="form-check-input" type="checkbox" value="${name}" id="${name}">
        <label class="form-check-label" for="${name}">${name}</label>
        </div>
    `
    })
    $('#graph-selector').html(varCheckboxArray.join(''))
}
addVarSelector()    


function checkInitial() {
    columns.forEach(name => graphVars[name]=false)
    document.getElementById("AMB_T").checked = true;
    graphVars["AMB_T"]=true
}
checkInitial()

function drawChart() {
    var materialOptions = {
    // chart: {
    //   title: 'Average Temperatures and Daylight in Iceland Throughout the Year'
    // },
    //width: 900,
    height: 500,
    series: {},
        // Gives each series an axis name that matches the Y-axis below.
    //   0: {axis: 'Temps'},
    //   1: {axis: 'Daylight'}
    // },
    axes: {
        // Adds labels to each axis; they don't have to match the axis names.
        // y: {
        //   Temps: {label: 'Temps (Celsius)'},
        //   Daylight: {label: 'Daylight'}
        // }
    }
    };

    var data = new google.visualization.DataTable();

    data.addColumn('datetime', 'Datetime');
    columns.forEach(varName => {
    if(graphVars[varName]==true){
        var newName;
        if( varName.includes("_T")){
            newName=`${varName} [??C]`
        } else if( varName.includes("POWER")){
            newName=`${varName} [W]`
        } else if ( varName.includes("FLOW")){
            newName=`${varName} [l/min]`
        } else if( varName.includes("CURRENT")){
            newName=`${varName} [A]`
        } else if ( varName.includes("VOLTAGE")){
            newName=`${varName} [V]`
        } else if ( varName.includes("ENERGY")){
            newName=`${varName} [kWh]`
        } else {
            newName=varName
        }
        data.addColumn('number',newName)                   
    }
    });
    
    function getFullArray(item) {
    varNames=Object.keys(graphVars)
    var fullArray=[new Date(item.DATETIME)]        
    columns.forEach(varName=>{
        if(graphVars[varName]==true){
        if(varName.includes("T_P")){
            fullArray.push(parseFloat(
            Math.max(0,(item["COOL_T_OUT"]-item["COOL_T_IN"])*item["COOL_FLOW"]*4184/60)
            ))} else {
        fullArray.push(parseFloat(item[varName]))}            
        }
    })
    return fullArray
    }

    function mapData() {
    return tableData.map(getFullArray);
    }

    data.addRows(mapData());
    var chartDiv = document.getElementById('chart_div');
    var materialChart = new google.charts.Line(chartDiv);
    materialChart.draw(data, google.charts.Line.convertOptions(materialOptions));
    
    google.visualization.events.addListener(materialChart, 'error', function (googleError) {
    google.visualization.errors.removeError(googleError.id);
    });
} 

function retrieveData(fromDate, toDate){
    endpoint = endpoint + fromDate + '/' + toDate +'/'  ///registriesAPI/20210409/20210410
    $.ajax({
    method: "Get",
    url: endpoint,
    success: function(data){
    tableData=data
    try{drawChart()}
    catch{}
    },error: function(error_data){
    }
    })
};
retrieveData(fromDate, toDate)  
$(".form-check-input").change(function() {
    if(this.checked) {
    graphVars[$(this).attr('id')]=true
    drawChart()
    }
    else{
    graphVars[$(this).attr('id')]=false
    drawChart()
    }
});
})