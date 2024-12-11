import sqlite3 

def commit_close(funcao): #Decorador para as funções que alteram valores
    def decorator(*parametros):
        con = sqlite3.connect('baseDeDados.db')
        cur = con.cursor()
        sql = funcao(*parametros)
        cur.execute(sql)
        con.commit()
        con.close()
        return sql
    return decorator

@commit_close
def cadastrar(nome, numeroConta, saldo=0.0): #Função de cadastro
    return f"""
        INSERT INTO contas_bancarias (nome, numeroConta, saldo)
        VALUES ('{nome}', '{numeroConta}', {saldo})
    """

def consultarSaldo(numeroConta): #Função de consulta
    con = sqlite3.connect('baseDeDados.db') #Conexão separada do decorador
    cur = con.cursor()
    cur.execute(f"""
            SELECT saldo
            FROM contas_bancarias
            WHERE numeroConta = '{numeroConta}'
            """)
    saldo = cur.fetchone()
    con.close()
    if saldo:
        saldo_valor = saldo[0]
        print(f"O saldo da conta é R${saldo_valor}")
        return saldo_valor
    return None

@commit_close
def depositar(numeroConta, valorDeposito): #Função de depósito
    return f"""
        UPDATE contas_bancarias
        SET saldo = saldo + {valorDeposito}
        WHERE numeroConta = '{numeroConta}'
    """

@commit_close
def sacar(numeroConta, valorSaque): #Função de Saque
    return f"""
        UPDATE contas_bancarias
        SET saldo = saldo - {valorSaque}
        WHERE numeroConta = '{numeroConta}'
    """
@commit_close
def deletar(id): #Função de deletar
    return f"""
            DELETE FROM contas_bancarias WHERE id = '{id}' """

