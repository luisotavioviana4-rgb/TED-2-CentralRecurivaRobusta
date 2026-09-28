from central_recursiva.excecoes import OperacaoInvalidaError, EntradaInvalidaError
from central_recursiva.matematica import mdc_recursivo, soma_digitos_recursivo

def main():
    while True:
        try:
            linha_q = input().strip()
            if linha_q:
                q = int(linha_q)
                break
        except EOFError:
            return
        except ValueError:
            continue

    operacoes_lidas = 0

    while operacoes_lidas < q:
        try:
            linha = input().strip()

            if not linha:
                continue

        except EOFError:
            break

        operacoes_lidas += 1
        partes = linha.split()
        operacao = partes[0]

        try:
            if operacao == 'M':
                if len(partes) != 3:
                    raise EntradaInvalidaError()

                a, b = int(partes[1]), int(partes[2])

                if a <= 0 or b <= 0:
                    raise EntradaInvalidaError()

                print(f"MDC={mdc_recursivo(a, b)}")

            elif operacao == 'S':
                if len(partes) != 2:
                    raise EntradaInvalidaError()

                n = int(partes[1])

                if n < 0:
                    raise EntradaInvalidaError()

                print(f"SOMA={soma_digitos_recursivo(n)}")

            else:
                raise OperacaoInvalidaError()

        except OperacaoInvalidaError:
            print("ERRO: OperacaoInvalida")

        except (EntradaInvalidaError, ValueError):
            print("ERRO: EntradaInvalida")

        finally:
            pass

if __name__ == '__main__':
    main()
