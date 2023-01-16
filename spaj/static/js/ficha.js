

var atributos = [1, 0, 0, 0, 0, 0, 0, 0]

var forca = 0
var vitalidade = 0
var luta = 0

var pontos_disponiveis = 7
var pericias_disponiveis

var vartranscicao
var vartranscicao2
var n = 0



pontos_disponiveis = atributos[0] * 7

function adição(atribId, atrib) {
    vartranscicao = window.document.getElementById(atribId)


    if (pontos_disponiveis > 0) {
        if (atributos[atrib] === 17) {
            vartranscicao.innerHTML = atributos[atrib]

        }
        else {
            atributos[atrib]++
            vartranscicao.innerHTML = atributos[atrib]

            if (atributos[atrib] <= 17) {
                pontos_disponiveis--
                vartranscicao2 = window.document.getElementById('pontos_disponiveisId')
                vartranscicao2.innerHTML = pontos_disponiveis

            }
        }

        if (atribId == 'constituicao_fisica' || atribId == 'destreza' || atribId == 'agilidade' || atribId == 'conhecimento') {

            if (atribId == 'constituicao_fisica') {
                vitalidade = atributos[5]
                vartranscicao = window.document.getElementById('vitalidadeId')
                vartranscicao.innerHTML = vitalidade

                forca = atributos[5]
                vartranscicao = window.document.getElementById('forcaId')
                vartranscicao.innerHTML = forca
            }

            if (atribId == 'destreza' || atribId == 'agilidade') {
                luta = Math.floor((atributos[3] + atributos[4]) / 2)
                vartranscicao = window.document.getElementById('lutaId')
                vartranscicao.innerHTML = Math.floor((atributos[3] + atributos[4]) / 2)
            }

            if (atribId == 'conhecimento') {

                pericias_disponiveis = atributos[2]
                vartranscicao = document.getElementById('periciasDisponiveis')
                vartranscicao.innerHTML = pericias_disponiveis
            }

        }



    }

    if (atrib == 0) {
        pontos_disponiveis = atributos[0] * 7
        vartranscicao2 = window.document.getElementById('pontos_disponiveisId')
        vartranscicao2.innerHTML = pontos_disponiveis




    }
    if (atrib == 0) {

        atributos[7] = 0
        vartranscicao = window.document.getElementById('carisma')
        vartranscicao.innerHTML = 0

        atributos[6] = 0
        vartranscicao = window.document.getElementById('percepcao')
        vartranscicao.innerHTML = 0

        atributos[5] = 0
        vartranscicao = window.document.getElementById('constituicao_fisica')
        vartranscicao.innerHTML = 0

        atributos[4] = 0
        vartranscicao = window.document.getElementById('destreza')
        vartranscicao.innerHTML = 0

        atributos[3] = 0
        vartranscicao = window.document.getElementById('agilidade')
        vartranscicao.innerHTML = 0

        atributos[2] = 0
        vartranscicao = window.document.getElementById('conhecimento')
        vartranscicao.innerHTML = 0

        atributos[1] = 0
        vartranscicao = window.document.getElementById('sabedoria')
        vartranscicao.innerHTML = 0

        forca = 0
        vartranscicao = window.document.getElementById('forcaId')
        vartranscicao.innerHTML = 0

        vitalidade = 0
        vartranscicao = window.document.getElementById('vitalidadeId')
        vartranscicao.innerHTML = 0

        luta = 0
        vartranscicao = window.document.getElementById('lutaId')
        vartranscicao.innerHTML = 0

        pericias_disponiveis = atributos[2]
        vartranscicao = document.getElementById('periciasDisponiveis')
        vartranscicao.innerHTML = pericias_disponiveis

        pontos_disponiveis = atributos[0] * 7
        vartranscicao2 = window.document.getElementById('pontos_disponiveisId')
        vartranscicao2.innerHTML = pontos_disponiveis

    }


}

function subtrair(atribId, atrib) {
    vartranscicao = window.document.getElementById(atribId)

    if (atributos[atrib] == 1 && atrib == 0) {
        vartranscicao.innerHTML = atributos[atrib]

    }

    if (atributos[atrib] == 0) {
        vartranscicao.innerHTML = atributos[atrib]
    }
    else {
        atributos[atrib]--
        vartranscicao.innerHTML = atributos[atrib]
        pontos_disponiveis++
        vartranscicao2 = window.document.getElementById('pontos_disponiveisId')
        vartranscicao2.innerHTML = pontos_disponiveis
    }
    if (atributos[atrib] == 0 && atrib == 0) {
        vartranscicao.innerHTML = 1
        atributos[atrib] = 1


    }
    if (atrib == 0) {

        atributos[7] = 0
        vartranscicao = window.document.getElementById('carisma')
        vartranscicao.innerHTML = 0

        atributos[6] = 0
        vartranscicao = window.document.getElementById('percepcao')
        vartranscicao.innerHTML = 0

        atributos[5] = 0
        vartranscicao = window.document.getElementById('constituicao_fisica')
        vartranscicao.innerHTML = 0

        atributos[4] = 0
        vartranscicao = window.document.getElementById('destreza')
        vartranscicao.innerHTML = 0

        atributos[3] = 0
        vartranscicao = window.document.getElementById('agilidade')
        vartranscicao.innerHTML = 0

        atributos[2] = 0
        vartranscicao = window.document.getElementById('conhecimento')
        vartranscicao.innerHTML = 0

        atributos[1] = 0
        vartranscicao = window.document.getElementById('sabedoria')
        vartranscicao.innerHTML = 0

        forca = 0
        vartranscicao = window.document.getElementById('forcaId')
        vartranscicao.innerHTML = 0

        vitalidade = 0
        vartranscicao = window.document.getElementById('vitalidadeId')
        vartranscicao.innerHTML = 0

        luta = 0
        vartranscicao = window.document.getElementById('lutaId')
        vartranscicao.innerHTML = 0

        pericias_disponiveis = atributos[2]
        vartranscicao = document.getElementById('periciasDisponiveis')
        vartranscicao.innerHTML = pericias_disponiveis

        pontos_disponiveis = atributos[0] * 7
        vartranscicao2 = window.document.getElementById('pontos_disponiveisId')
        vartranscicao2.innerHTML = pontos_disponiveis

    }

    if (atribId == 'constituicao_fisica' || atribId == 'destreza' || atribId == 'agilidade' || atribId == 'conhecimento') {




        if (atribId == 'constituicao_fisica') {

            vitalidade = atributos[5]
            vartranscicao = window.document.getElementById('vitalidadeId')
            vartranscicao.innerHTML = atributos[5]

            forca = atributos[5]
            vartranscicao = window.document.getElementById('forcaId')
            vartranscicao.innerHTML = atributos[5]
        }

        if (atribId == 'destreza' || atribId == 'agilidade') {

            luta = Math.floor((atributos[3] + atributos[4]) / 2)
            vartranscicao = window.document.getElementById('lutaId')
            vartranscicao.innerHTML = Math.floor((atributos[3] + atributos[4]) / 2)
        }

        if (atribId == 'conhecimento') {

            pericias_disponiveis = atributos[2]
            vartranscicao = document.getElementById('periciasDisponiveis')
            vartranscicao.innerHTML = pericias_disponiveis
        }

    }
}

function iniciarbotao() {
    window.document.getElementById('levelhtml').value = atributos[0]
    window.document.getElementById('sabedoriahtml').value = atributos[1]
    window.document.getElementById('conhecimentohtml').value = atributos[2]
    window.document.getElementById('agilidadehtml').value = atributos[3]
    window.document.getElementById('destrezahtml').value = atributos[4]
    window.document.getElementById('constfisicahtml').value = atributos[5]
    window.document.getElementById('percepcaohtml').value = atributos[6]
    window.document.getElementById('carismahtml').value = atributos[7]
    window.document.getElementById('vitalidadehtml').value = vitalidade
    window.document.getElementById('forcahtml').value = forca
    window.document.getElementById('lutahtml').value = luta
}

controlPericias()

function controlPericias() {
    let aux
    let checkboxes = document.querySelectorAll(".form-check-input")

    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener("change", bindClick(i));
    }

    function bindClick(i) {
        return function () {

            if (checkboxes[i].checked) {
                pericias_disponiveis--
                aux = document.getElementById('periciasDisponiveis')
                aux.innerHTML = pericias_disponiveis

            } else {

                pericias_disponiveis++
                aux = document.getElementById('periciasDisponiveis')
                aux.innerHTML = pericias_disponiveis

            }

            if (pericias_disponiveis <= 0) {

                for (let i = 0; i < checkboxes.length; i++) {

                    if (checkboxes[i].checked) {

                    } else {
                        checkboxes[i].disabled = true
                    }

                }
            }

            if (pericias_disponiveis != 0) {
                for (let i = 0; i < checkboxes.length; i++) {
                    checkboxes[i].disabled = false

                }
            }

        }
    }

}
