var idade = 45.5

console.log(`Você tem ${idade} anos.`)

if (idade < 16) {
    console.log('Não vota!')
} else if (idade < 18 || idade >= 70){
        console.log('Voto opcional!')
    } else {
        console.log('Vota!')
    }