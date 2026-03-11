const API = "http://127.0.0.1:8000"

async function carregarTarefas(){

 let resposta = await fetch(API + "/tarefas")
 let tarefas = await resposta.json()

 let lista = document.getElementById("lista")
 lista.innerHTML = ""

 tarefas.forEach(t => {

  let item = document.createElement("li")
  item.innerHTML = t[1] + " "

  let btn = document.createElement("button")
  btn.innerText = "Excluir"

  btn.onclick = () => deletarTarefa(t[0])

  item.appendChild(btn)

  lista.appendChild(item)

 })

}

async function criarTarefa(){

 let titulo = document.getElementById("titulo").value

 await fetch(API + "/tarefas?titulo=" + titulo, {
  method: "POST"
 })

 carregarTarefas()
}

async function deletarTarefa(id){

 await fetch(API + "/tarefas/" + id,{
  method:"DELETE"
 })

 carregarTarefas()
}

carregarTarefas()
