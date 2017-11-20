/**
 * Created by Dell on 15-11-2017.
 */
function required()
{
    var empt = document.forms["form1"]["occupant"].value;
    var empt2 = document.forms["form1"]["roll_number"].value;
    if (empt == "" || empt2 == "")
    {
        alert("Please input a value");
        return false;
    }
    else
    {
        return true;
    }
}
function radioval() {
    var radios = document.getElementsByTagName('input');
    var value;
    var flag = 0;
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].type === 'radio' && radios[i].checked) {
        // get value, set checked flag or do whatever you need to
            value = radios[i].value;
            flag = 1;
            break;
    }

}
 if (flag == 0){
            alert("Please select a room");
    }

}