function calcular(val1, val2, tipo){
  if (tipo == 'soma') {
    return val1 + val2
  }
  else if(tipo == 'menos'){
    return val1 - val2
  }
}


calcular(10, 5, 'soma')