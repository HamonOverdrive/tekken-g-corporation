/*!
* All functions for char_frame_page.html
*/


//start of filtering functions
function filterMoves(moveType, filter) {
    //alert(moveType + " " + filter);

    var filterArray = filter.split(';')

    //from example - for search bar
    //var input, filter
    //input = document.getElementById("myInput");
    //filter = input.value.toUpperCase();

    var table = document.getElementById("framedata_table_1");   //for now, this
    var tr = table.getElementsByTagName("tr");

    var filterColumnEnum = Object.freeze({"command":0, "hit_level":1, "damage":2, "start_up_frame":3, "block_frame":4, "hit_frame":5, "counter_hit_frame":6, "notes":7})

    var filterColumn
    if(moveType = "punish"){
       filterColumn = filterColumnEnum.start_up_frame;
    } else if (moveType = "onblock"){
        filterColumn = filterColumnEnum.block_frame;
    } else if (moveType = "other"){
        //deal with OTHER

    }

    var td;
    var i;
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[filterColumn];
        if (td) {
            //td.innerHTML.toUpperCase().indexOf(filter) > -1
            if (compareToFilterArray(td.innerHTML, filterArray)){
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function compareToFilterArray(value, filterArray){

    var returnValue = true;
    var logicalOperators = ["<", ">", "<=", ">=", "="];
    //remember to trim value so it could follow logical operators or could be compared with "==" to OTHER

    filterArray.forEach(function(fil){

        var filterValue;

        if (new RegExp(logicalOperators.join("|")).test(fil)) {

            //trim everything to the first number
            var filterValue = fil.replace( /^\D+/g, '');

            switch(fil.replace(filterValue, '')) {  //check the operator
                case "=":
                    returnValue = returnValue && (value == filterValue);
                    break;
                case ">":
                    returnValue = returnValue && (value > filterValue);
                    break;
                case "<":
                    returnValue = returnValue && (value < filterValue);
                    break;
                case ">=":
                    returnValue = returnValue && (value >= filterValue);
                    break;
                case "<=":
                    returnValue = returnValue && (value <= filterValue);
                    break;
                default:
                    break;
            }

        } else {
            returnValue = returnValue && (value == fil)
        }

    });

    return returnValue;
}
//end of filtering functions

//start of sorting functions
function sort(ele){

    var columnElement = ele.parentElement.parentElement;
    var tableElement = columnElement.parentElement.parentElement.parentElement;

    var columnName = "";
    var tableName = tableElement.id;
    var headerElement = columnElement.getElementsByTagName("P")[0];

    if(!(headerElement == null)){
        columnName = headerElement.innerHTML.toLowerCase();
    } else {
        console.log("column name undefined");
    }

    /*Get search column id*/
    var columnId;
    for (var i = 0; i < tableElement.rows[0].cells.length; i++) {
        if (columnName === tableElement.rows[0].cells[i].getElementsByTagName("P")[0].innerHTML.toLowerCase()){
            columnId = i;
            break;
        }
    }

    var sortType;
    var otherArrowClassName;
    if(ele.className === "arrow-up"){
        sortType = "ASC";
    } else if (ele.className === "arrow-down"){
        sortType = "DESC";
    }

    toggleSortArrows(ele);
    sortTable_Inner(tableName, columnId, sortType);

}

function toggleSortArrows(arrowEle) {

    //reset all other arrows in the table
    var tableEle = arrowEle.parentElement.parentElement.parentElement.parentElement;
    for(var i=0; i < tableEle.rows[0].cells.length;i++){
        var thEle = tableEle.rows[0].cells[i];
        thEle.getElementsByClassName("arrow-up")[0].style.display = "block";
        thEle.getElementsByClassName("arrow-down")[0].style.display = "block";
    };

    //hide the arrow pressed
    arrowEle.style.display = "none";

    //show the arrow not pressed
    var otherArrowClassName;
    if(arrowEle.className === "arrow-up"){
        otherArrowClassName = "arrow-down";
    } else if (arrowEle.className === "arrow-down"){
        otherArrowClassName = "arrow-up";
    }

    var otherArrowEle = arrowEle.parentElement.getElementsByClassName(otherArrowClassName)[0];
    otherArrowEle.style.display = "block";

}

function sortTable_Inner(tableName, columnId, sortType) {

    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById(tableName);
    switching = true;

    /*Make a loop that will continue until no switching has been done:*/
    while (switching) {

        //start by saying: no switching is done:
        switching = false;
        rows = table.getElementsByTagName("TR");

        /*Loop through all table rows (except the first, which contains table headers):*/
        for (i = 1; i < (rows.length - 1); i++) {

            //start by saying there should be no switching:
            shouldSwitch = false;

            /*Get the two elements you want to compare, one from current row and one from the next:*/
            x = rows[i].getElementsByTagName("TD")[columnId];
            y = rows[i + 1].getElementsByTagName("TD")[columnId];

            x = normaliseSortElement(x);
            y = normaliseSortElement(y);

            //check if the two rows should switch place:
            if (sortType === "ASC"){
                if (x > y) {
                    //if so, mark as a switch and break the loop:
                    shouldSwitch= true;
                    break;
                }
            } else if (sortType === "DESC"){
                if (x < y) {
                    //if so, mark as a switch and break the loop:
                    shouldSwitch= true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            /*If a switch has been marked, make the switch and mark that a switch has been done:*/
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function normaliseSortElement(ele){

    var retValue = ele.innerHTML.toLowerCase();

    return retValue;
}
//end of sorting functions

