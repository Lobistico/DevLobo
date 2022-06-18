
function calc(sinal) {
    var operation = sinal.value;
    var n1 = parseFloat(document.getElementById("n1").value);
    var n2 = parseFloat(document.getElementById("n2").value);

    var calculo = eval(n1 + operation + n2);

    if (!isNaN(calculo)) {
        
        document.getElementById("n1").value = calculo;
        document.getElementById("n2").value = null;
        alert("O resultado é " + calculo);
    }else{
        alert("🤪 Ops! Parece que você não digitou um número válido.")
    }
}


function limpar() {
    var form = document.getElementById("form");
    var n1 = form.n1;
    var n2 = form.n2;
    n1.value = "";
    n2.value = "";
}

function calc2(sinal) {
    var operation = sinal.value;
    var n1 = parseFloat(document.getElementById("n1").value);
    var n2 = parseFloat(document.getElementById("n2").value);

    var calculo = eval(n1 + operation + n2);

    if (!isNaN(calculo)) {
        return calculo;        
    }
}