# META_LOGICAL_CHALLENGE

(This repo is written in Portuguese [Brazil])

Este repositório visa prover soluções para o desafio lógico
fornecido pelo META.

**OBS**: Os scripts foram escritos voltados para o **Python 3**, e não houve preocupação em fornecer
suporte ao Python 2 ([Ver referência](https://pythonclock.org/)), porém talvez os mesmos
funcionem. Todavia, não é garantido que para qualquer alteração futura os mesmos estarão funcionando
para o Python 2.

## Instalação

(Recomenda-se o uso de uma venv, para mais informações [clique aqui](https://docs.python.org/3/library/venv.html))

Faça download do Python e crie um ambiente virtual e ative-o

(O mesmo pode ser instalado através do [site oficial](https://www.python.org/downloads/).
)

```
python -m venv env
env/Scripts/activate  -- WINDOWS
source env/bin/activate -- LINUX
```

Execute o seguinte comando:

```
python -m pip install -r requirements.txt
```

Após o término da execução, o ambiente está pronto para executar os scripts.

## Execução

```
python questao<id>\questao<id>.py
```

**id**: Correspondente à questão à executar.

(Exemplo: `python questao03\questao03.py`)

## Testes

Os testes foram construídos de forma à permitir o fácil manuseio do testador.

Para executa-los, basta usar o seguinte comando:

```
nosetests -c nose.cfg
```

Para a execução de cada teste em particular, pode-se usar o *nose* ou o python em si.

* Usando Python:

```
python questao<id>\test.py
```

* Usando nose:

```
nosetests questao<id>
```