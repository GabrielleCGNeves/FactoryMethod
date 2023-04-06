<h1 align='center'><strong>🏭 Factory Method</strong></h1>

<div align='center'>
<strong>
<p><a href='https://github.com/ericksantos12'>Erick Sousa Santos</a></p>
<p><a href='https://github.com/GabrielleCGNeves'>Gabrielle Carvalho Gonçalves das Neves</a></p>
</strong>
</div>

<br>
<br>

<div align=center>
    <img src="https://refactoring.guru/images/patterns/content/factory-method/factory-method-en.png" width=400>
</div>

---
## 🧾 Descrição do Projeto
Este programa é um sistema de consulta de relação de pessoas com a instituição FATEC. Ele utiliza o padrão de design Factory Method para criar objetos que correspondem a diferentes tipos de relações, como aluno, professor, coordenador, diretor, administrativo e vestibulando.

Ao receber o nome e tipo de relação de uma pessoa, o programa cria um objeto correspondente usando a Factory e chama o método "apresentar" deste objeto, que imprime na tela uma mensagem informando a relação da pessoa com a FATEC. Se a relação não for encontrada, é exibida uma mensagem pedindo para consultar a secretaria da instituição.

O programa possui um menu com duas opções: "Consultar situação" e "Sair". O usuário pode escolher a opção desejada digitando o número correspondente no console. Se ele escolher a opção "Consultar situação", o programa pedirá o nome e o tipo de relação da pessoa que deseja consultar e, em seguida, exibirá a mensagem correspondente. Se ele escolher a opção "Sair", o programa será encerrado.

---

## 💻 Instalação
`> pip install -r requirements.txt`
