from central_recursiva.excecoes import OperacaoInvalidaError, EntradaInvalidaError
from central_recursiva.matematica import mdc_recursivo, soma_digitos_recursivo

def main():
    try:
        linha_q = input().strip()
        while not linha_q:
            linha_q = input().strip()
        q = int(linha_q)
    except (EOFError, ValueError):
        return

    for _ in range(q):
        try:
            linha = input().strip()
            while not linha:
                linha = input().strip()
        except EOFError:
            break
            
        partes = linha.split()
        if not partes:
            continue
            
        operacao = partes[0]
        
        try:
            if operacao == 'M':
                if len(partes) != 3:
                    raise EntradaInvalidaError()
                
                try:
                    a, b = int(partes[1]), int(partes[2])
                except ValueError:
                    raise EntradaInvalidaError()
                
                if a <= 0 or b <= 0:
                    raise EntradaInvalidaError()
                    
                resultado = mdc_recursivo(a, b)
                print(f"MDC={resultado}")
                
            elif operacao == 'S':
                if len(partes) != 2:
                    raise EntradaInvalidaError()
                
                try:
                    n = int(partes[1])
                except ValueError:
                    raise EntradaInvalidaError()
                
                if n < 0:
                    raise EntradaInvalidaError()
                    
                if n == 0:
                    print("SOMA=0")
                else:
                    resultado = soma_digitos_recursivo(n)
                    print(f"SOMA={resultado}")
                    
            else:
                raise OperacaoInvalidaError()
                
        except OperacaoInvalidaError:
            print("ERRO: OperacaoInvalida")
        except EntradaInvalidaError:
            print("ERRO: EntradaInvalida")
        finally:
            pass

if __name__ == '__main__':
    main()
