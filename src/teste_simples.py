import socket
import time

def teste_conexao():
    """Testa se a porta está disponível"""
    try:
        # Testar se a porta está livre
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.bind(('127.0.0.1', 12345))
        test_socket.close()
        print("✅ Porta 12345 está livre!")
        return True
    except OSError as e:
        if e.winerror == 10048:
            print("❌ Porta 12345 está ocupada!")
            print("   Aguarde alguns segundos ou use outra porta.")
            return False
        else:
            print(f"❌ Erro desconhecido: {e}")
            return False

def instrucoes():
    """Mostra instruções de uso"""
    print("\n" + "="*50)
    print("INSTRUÇÕES DE USO:")
    print("="*50)
    print("1. Em um terminal, execute: python teste2.py")
    print("2. Em outro terminal, execute: python cliente.py")
    print("3. Digite uma mensagem no cliente")
    print("4. Veja a resposta no servidor")
    print("="*50)

if __name__ == "__main__":
    print("🔍 Verificando se a porta está disponível...")
    
    if teste_conexao():
        instrucoes()
    else:
        print("\n💡 Dica: Aguarde 30 segundos e tente novamente!")
        print("   Ou mude a porta no código para 23456")
