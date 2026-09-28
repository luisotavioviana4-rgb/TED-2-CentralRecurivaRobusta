TED-2-CentralRecursivaRobusta
Integrantes da dupla:

    Divivo Rafael Abade Oliveira (26.1.14744)
    Luís Otávio Viana dos Santos (26.1.18406)

Descrição do Projeto

Este projeto consiste em uma aplicação em Python desenvolvida para processar e executar operações matemáticas simples utilizando recursão. A aplicação lê um conjunto de operações via entrada padrão (CLI), interpreta se o comando é para calcular o Máximo Divisor Comum (MDC) ou a Soma dos Dígitos de um número, valida todos os dados recebidos e trata possíveis erros utilizando exceções personalizadas.

    Certifique-se de ter o Python 3.8+ instalado.
    No terminal, navegue até a pasta raiz do projeto.
    Execute o comando:
    python -m main


Descrição dos Módulos

O projeto está organizado no pacote central_recursiva, composto por:


    __init__.py: Arquivo de inicialização responsável por definir o diretório como um pacote Python e expor os elementos públicos     do módulo.
    excecoes.py: Módulo dedicado a definir as classes de exceções personalizadas do sistema (EntradaInvalidaError e OperacaoInvalidaError).
    matematica.py: Módulo que concentra a lógica matemática, contendo as implementações das funções recursivas (mdc_euclides e        soma_digitos).
    main.py (raiz): Script principal encarregado de capturar a entrada do usuário, chamar os processamentos matemáticos, validar      os dados e gerenciar erros via blocos try, except e finally.



Algoritmos Recursivos

O projeto implementa duas funções recursivas principais no módulo matematica.py:

    
    MDC Recursivo (Algoritmo de Euclides):
    A função recebe dois inteiros ($a$ e $b$). Caso $b$ seja igual a $0$, a função retorna $a$ como resultado (caso base). Caso  contrário, ela realiza uma chamada recursiva passando $b$ e o resto da divisão de $a$ por $b$ (a % b), repetindo essa etapa até encontrar o divisor comum máximo.
    Soma dos Dígitos Recursiva: A função recebe um número inteiro $n$. Se $n < 10$ (ou $n = 0$), retorna o próprio valor (caso base). Caso contrário, extrai o último dígito através do operador resto (n % 10) e o soma ao retorno da chamada recursiva com o restante do número obtido da divisão inteira por $10$ (n // 10).

Exceções Personalizadas

Para assegurar o tratamento adequado e seguro das entradas, foram desenvolvidas duas exceções personalizadas que herdam da classe nativa Exception:

    OperacaoInvalidaError: Exceção lançada quando o sistema identifica um caractere ou comando de operação diferente dos aceitos      ('M' ou 'S').

    EntradaInvalidaError: Exceção lançada quando as informações fornecidas para uma operação válida apresentam inconsistências,    tais como valores negativos, uso do número zero na operação de MDC, falta de parâmetros ou tipos numéricos inválidos.
