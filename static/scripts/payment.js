import {setupAjax} from './setup.js';


$("#submit").on("click",create_payment);
$("#paymentOptions").on("change",change_options);

function create_payment(e){
    e.preventDefault();
    $(document).ready(()=>{
        console.log()
        setupAjax("/payment/create", {"type":$("#paymentOptions").val(),"name":$("#paymentName").val(), "amt":$("#paymentAmount").val()});
        $.ajax().then((data=>{

        }))
    });
}

function change_options(e){
    e.preventDefault();
    console.log(document.getElementById("paymentOptions").value)
    switch(document.getElementById("paymentOptions").value){
        case("credit"):
            document.getElementById("creditFields").style.display="block";
            document.getElementById("checkFields").style.display="none";
            document.getElementById("cashFields").style.display="none";
            break;
        case("check"):
            document.getElementById("creditFields").style.display="none";
            document.getElementById("checkFields").style.display="block";
            document.getElementById("cashFields").style.display="none";
            break;
        case("cash"):
            document.getElementById("creditFields").style.display="none";
            document.getElementById("checkFields").style.display="none";
            document.getElementById("cashFields").style.display="block";
            break;
        default:
            document.getElementById("cashFields").style.display="none";
            document.getElementById("checkFields").style.display="none"
            document.getElementById("creditFields").style.display="none";
    }
};