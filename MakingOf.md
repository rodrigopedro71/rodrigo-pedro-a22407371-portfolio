# Making Of

Para começar, defini as entidades que ia precisar e os respetivos atributos. A ideia inicial era esta:

1. **UC** — nome, ano, semestre, professor, imagem, projeto, codigo_uc
2. **Projeto** — nome, descricao, tecnologia, repositorio, conceitos_aplicados, uc
3. **Licenciatura** — nome, competencia, uc, professor
4. **Tecnologia** — nome, interesse, projeto, site, descricao
5. **TFC** — nome, tecnologia, descricao, email, classificacao
6. **Competencia** — nome, descricao
7. **Formacao** — nome, empresa, descricao
8. **Making Of** — registos_trabalho, descricao_decisoes, erros_encontrados

Depois de ter as entidades definidas, fiz o diagrama ER:

![alt text](media/makingof/diagrama_1.png)

---

Quando comecei a implementar as entidades no Django apercebi-me que algumas coisas não faziam muito sentido. Havia atributos mal colocados e percebi que fazia sentido adicionar uma entidade nova — o **Professor** (que depois passei a chamar **Docente**, achei mais correto).

![alt text](media/makingof/diagrama_2.png)

A entidade Docente não estava nos requisitos mas faz todo o sentido existir — cada UC tem professores que a lecionam, e com esta entidade consigo guardar informações extra como a formação académica deles.

Aproveitei também para fazer algumas limpezas. Na entidade **Projeto** tirei o atributo `uc` porque percebi que a lógica estava invertida — é a UC que tem um Projeto, não o contrário. Na entidade **Tecnologia** mudei o atributo `interesse` para `classificacao`, que representa o quão à vontade estou com a tecnologia, e acrescentei o atributo `logo` para guardar o logótipo.

---

Na entidade **Competencia** mantive os atributos mas mudei `nome` para `tipo` — faz mais sentido falar em "tipo de competência" do que em "nome de competência". Adicionei também uma ligação entre **Projeto** e **Competencia**, já que foi através dos projetos que fui adquirindo as competências.

---

No `admin.py` fui ajustando o `list_display` à medida que achei que faltava informação. No **DocenteAdmin** acrescentei o email, no **ProjetoAdmin** o repositório, no **TecnologiaAdmin** o site oficial e no **UCAdmin** o ano e o semestre. São coisas que parecem óbvias mas que só fui reparando que faltavam depois de ver o admin em funcionamento.

---

Na entidade **Docente** mudei o atributo `email` de `CharField()` para `EmailField()`, lembrando-me que numa ficha anterior de Django tinha usado este campo e que era mais correto para guardar emails.

Na entidade **Formacao** fiz algumas alterações em relação à ideia original. Mudei `nome` para `tipo` porque nem todas as formações têm um nome propriamente dito, tirei o atributo `empresa` porque nem todas as formações são feitas por empresas, e acrescentei `data` para saber quando foi feita. Por fim liguei **Formacao** à entidade **Tecnologia**, já que podem existir formações específicas de certas tecnologias.

---

A entidade **MakingOf** também ficou bastante diferente do plano inicial. Mudei `registos_trabalho` para `fotos`, e separei a descrição em campos mais específicos — `alteracao` e `justificacao` — para estar mais organizado. Adicionei ainda um campo `llm` para registar se usei algum modelo de linguagem e de que forma ajudou.

---

Para a entidade **Tfc** fui primeiro ver o ficheiro `.json` que tinha feito na ficha 4 de web scraping e mapeei os atributos diretamente a partir daí. Os atributos ficaram: `titulo`, `aluno`, `orientador`, `licenciatura`, `pdf`, `mail`, `resumo`, `palavras_chave`, `tecnologias` e `rating`.

Aproveitei também para mudar todos os atributos `descricao` de `CharField()` para `TextField()` em todas as entidades — é mais correto quando não sabemos o tamanho do texto que vai ser inserido.

---

Para carregar os dados dos TFCs criei o `loader_tfc.py`, seguindo as instruções do professor. Criei a pasta `data/` e coloquei lá o `tfc.json` com toda a informação dos TFCs.

---

Para carregar as UCs usei o script dado pelo professor que consome uma API da Lusófona. Analisei os JSONs gerados e escolhi os atributos que achei mais relevantes: `ects`, `objetivo`, `programa` e `avaliacao`.

Quando corri o `loader_uc.py` dei com um erro num ficheiro específico — era diferente de todos os outros, tinha informação da licenciatura, dos docentes e das UCs em conjunto. O problema era que o loader tentava ler campos que não existiam nesse ficheiro. Resolvi mover esse ficheiro para a pasta `data/` diretamente e adaptar o loader para o usar como ponto de partida — primeiro vai buscar o código de cada UC nesse ficheiro geral, e depois vai ao ficheiro individual de cada UC para obter informação mais detalhada.

---

Depois de ver o JSON com mais atenção retirei o atributo `avaliacao` da entidade UC — o campo vinha com código HTML dentro, o que não era utilizável.

---

No `loader_uc.py` acrescentei também o carregamento dos **Docentes**. Para isso adicionei os atributos `card_code`, `employee_code`, `degree` e `regime` à entidade, que eram os mais relevantes no JSON. Removi o atributo `site` que tinha colocado no início — quando planeei a entidade estava a imaginar que íamos buscar os dados manualmente a algum site, mas como acabámos por usar uma API isso deixou de fazer sentido.

---

Atualizei o **DocenteAdmin** para listar mais informação: `employee_code`, `email`, `degree` e `regime` no `list_display`. No `ordering` adicionei `employee_code` para desempatar quando há nomes iguais, e no `search_fields` acrescentei `employee_code` e `email` para ter mais opções de pesquisa.

---

Ainda no `loader_uc.py` adicionei o carregamento da **Licenciatura**, usando os atributos `curso_codigo`, `semestres`, `descricao`, `objetivos` e `curso_ects`.

Durante os testes dei conta de um erro — tinha colocado os ECTS no campo `curso_codigo` por engano. Corrigi de seguida.

---

Por fim adicionei `blank=True` ao atributo `repositorio` da entidade **Projeto**, já que nem todos os projetos têm repositório, e ao atributo `docente` da entidade **UC**, porque ao criar as UCs os docentes podem ainda não estar registados na base de dados.