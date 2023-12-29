Fala dev's. Tudo show? 
Então, recentemente pra testar meus conhecimentos eu resolvi buscar um teste na internet e ver como me saía. Achei um utilizando Django Rest Framework(DRF). Decidi então fazer e ver no que ia dar. Ainda estou fazendo e sempre tentando melhorar ele. Então todo apoio(seja dando dicas ou seja dando alguma critica para meu crescimento) será sempre bem vinda!
Segue abaixo a problematica:


![image](https://github.com/joabe-levi/testeDetic/assets/52892525/c8be7835-d4ce-4776-acf0-a3cfbd0bb6d7)

![image](https://github.com/joabe-levi/testeDetic/assets/52892525/d201d91f-9f56-42d5-8bb7-d7dc0abfbb9b)


Entretanto, decidi incorporar novos requisitos ao projeto. A seguir, apresento as adições propostas:

**Restrição de Inclusão de Registros de Armas:**
  - A capacidade de incluir novos registros oficiais de armas deve ser restrita exclusivamente a superusuários e usuários que possuam a função de policiais.

**Reutilização de Código e Organização:**
  - Implementar estruturas de base para o reaproveitamento de código, promovendo uma abordagem modular que contribuirá para um código mais limpo, organizado e facilmente mantido.

**Introdução da Flag "Ativo" nos Modelos:**
  - Adicionar uma flag denominada "ativo" aos modelos, indicando se o registro está ativo ou inativo. Esta medida visa prevenir a exclusão acidental de dados, oferecendo uma abordagem mais segura. Nota: Os métodos all() e filter() foram adaptados para filtrar automaticamente com base nesta nova flag, proporcionando uma camada adicional de segurança, mesmo quando aplicados filtros adicionais na viewset.

**Implementação de Login e Logout com Geração de Tokens:**
  - Estabelecer funcionalidades de login e logout para os usuários, com a geração de tokens associada a cada usuário autenticado. Este mecanismo visa aprimorar a segurança e controlar o acesso ao sistema de maneira mais eficaz.

**Melhoramento do Recurso do Admin:**
  - Adicionar duas novas funções ao recurso do admin: "Ativar Registros" e "Desativar Registros". Estas funções proporcionarão uma maneira eficiente de gerenciar o estado ativo ou inativo de múltiplos registros, contribuindo para uma administração mais eficaz do sistema.
