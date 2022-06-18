function salvar() {
    a = document.getElementById("raca").value
    b = document.getElementById("orientacao").value
    c = document.getElementById("genero").value
    
    e = a + b + c
    return e
}

function atualizouRaca() {
    let select = document.querySelector("#raca");
    let optionValue = select.options[select.selectedIndex];
    let value = optionValue.value;
    console.log(value)
}

function atualizouOrientacao() {
    let select = document.querySelector("#orientacao");
    let optionValue = select.options[select.selectedIndex];
    let value = optionValue.value;
    console.log(value)
}

function atualizouGenero() {
    let select = document.querySelector("#genero");
    let optionValue = select.options[select.selectedIndex];
    let value = optionValue.value;
    console.log(value)
}

function persiste() {
    let va = JSON.stringify(vt);
    localStorage.setItem(nchave, va);
}

