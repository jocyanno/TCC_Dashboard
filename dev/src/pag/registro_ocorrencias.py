import datetime
import streamlit as st
from config_db_ocorrencias import create_connection_tendencia_Ocorrencias

def registro_ocorrencias():
    st.title("Registro de Ocorrências")
    
    # Inicializar o estado da sessão para os inputs
    if 'data' not in st.session_state:
        st.session_state['data'] = None
    if 'origem' not in st.session_state:
        st.session_state['origem'] = ''
    if 'processo' not in st.session_state:
        st.session_state['processo'] = ''
    if 'endereco' not in st.session_state:
        st.session_state['endereco'] = ''
    if 'localidade' not in st.session_state:
        st.session_state['localidade'] = ''
    if 'referencia' not in st.session_state:
        st.session_state['referencia'] = ''
    if 'tipo_solicitacao' not in st.session_state:
        st.session_state['tipo_solicitacao'] = ''
    if 'atendimento' not in st.session_state:
        st.session_state['atendimento'] = ''
    if 'quant_moradores' not in st.session_state:
        st.session_state['quant_moradores'] = 0
    if 'hora' not in st.session_state:
        st.session_state['hora'] = datetime.datetime.now().time()
    if 'scaner' not in st.session_state:
        st.session_state['scaner'] = ''
    if 'nome' not in st.session_state:
        st.session_state['nome'] = ''
    if 'fone' not in st.session_state:
        st.session_state['fone'] = ''
    if 'bairro' not in st.session_state:
        st.session_state['bairro'] = ''
    if 'reg' not in st.session_state:
        st.session_state['reg'] = ''
    if 'descricao_ocorrencia' not in st.session_state:
        st.session_state['descricao_ocorrencia'] = 'Alagamento'
    if 'monitoramento' not in st.session_state:
        st.session_state['monitoramento'] = ''
    if 'cep' not in st.session_state:
        st.session_state['cep'] = ''
    if 'observacoes' not in st.session_state:
        st.session_state['observacoes'] = ''

    # Campos de entrada
    col1, col2 = st.columns(2)
    with col1:
        st.session_state['data'] = st.date_input("DATA", value=st.session_state['data'])
        st.session_state['origem'] = st.text_input("ORIGEM", value=st.session_state['origem'])
        st.session_state['processo'] = st.text_input("PROCESSO", value=st.session_state['processo'])
        st.session_state['endereco'] = st.text_input("ENDEREÇO", value=st.session_state['endereco'])
        st.session_state['localidade'] = st.text_input("LOCALIDADE", value=st.session_state['localidade'])
        st.session_state['referencia'] = st.text_input("REFERENCIA", value=st.session_state['referencia'])
        st.session_state['tipo_solicitacao'] = st.text_input("TIPO DE SOLICITAÇÃO", value=st.session_state['tipo_solicitacao'])
        st.session_state['atendimento'] = st.text_input("ATENDIMENTO", value=st.session_state['atendimento'])
        st.session_state['quant_moradores'] = st.number_input("QUANT. DE MORADORES", min_value=0, step=1, value=st.session_state['quant_moradores'])
    with col2:
        st.session_state['hora'] = st.time_input("HORA", value=st.session_state['hora'])
        st.session_state['scaner'] = st.text_input("SCANER", value=st.session_state['scaner'])
        st.session_state['nome'] = st.text_input("NOME", value=st.session_state['nome'])
        st.session_state['fone'] = st.text_input("FONE", value=st.session_state['fone'])
        st.session_state['bairro'] = st.text_input("BAIRRO", value=st.session_state['bairro'])
        st.session_state['reg'] = st.text_input("REG", value=st.session_state['reg'])
        st.session_state['descricao_ocorrencia'] = st.selectbox("DESCRIÇÃO DA OCORRÊNCIA", ["Alagamento", "Deslizamento", "Outros"], index=["Alagamento", "Deslizamento", "Outros"].index(st.session_state['descricao_ocorrencia']))
        st.session_state['monitoramento'] = st.text_input("MONITORAMENTO", value=st.session_state['monitoramento'])
        st.session_state['cep'] = st.text_input("CEP", value=st.session_state['cep'])
    st.session_state['observacoes'] = st.text_area("OBSERVAÇÕES", value=st.session_state['observacoes'])
    
    if st.button("Registrar Ocorrência"):
        connection = create_connection_tendencia_Ocorrencias()
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ocorrencias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data DATE,
            origem VARCHAR(255),
            hora TIME,
            scaner VARCHAR(255),
            processo VARCHAR(255),
            nome VARCHAR(255),
            endereco VARCHAR(255),
            fone VARCHAR(255),
            localidade VARCHAR(255),
            bairro VARCHAR(255),
            referencia VARCHAR(255),
            reg VARCHAR(255),
            tipo_solicitacao VARCHAR(255),
            descricao_ocorrencia TEXT,
            atendimento VARCHAR(255),
            observacoes TEXT,
            monitoramento VARCHAR(255),
            quant_moradores INT,
            cep VARCHAR(255)
        """
        cursor.execute(create_table_query)
        
        query = """
          INSERT INTO ocorrencias (data, origem, hora, scaner, processo, nome, endereco, fone, localidade, bairro, referencia, reg, tipo_solicitacao, descricao_ocorrencia, atendimento, observacoes, monitoramento, quant_moradores, cep)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (st.session_state['data'], st.session_state['origem'], st.session_state['hora'], st.session_state['scaner'], st.session_state['processo'], st.session_state['nome'], st.session_state['endereco'], st.session_state['fone'], st.session_state['localidade'], st.session_state['bairro'], st.session_state['referencia'], st.session_state['reg'], st.session_state['tipo_solicitacao'], st.session_state['descricao_ocorrencia'], st.session_state['atendimento'], st.session_state['observacoes'], st.session_state['monitoramento'], st.session_state['quant_moradores'], st.session_state['cep'])
        
        cursor.execute(query, values)
        connection.commit()
        
        # Inserir na tabela deslizamentos
        if st.session_state['descricao_ocorrencia'] == 'Deslizamento' or st.session_state['descricao_ocorrencia'] == 'Alagamento':
            deslizamento_query = """
            INSERT INTO deslizamentos (date, count)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE count=VALUES(count)
            """
            deslizamento_values = (st.session_state['data'], 1)
            cursor.execute(deslizamento_query, deslizamento_values)
            connection.commit()
        
        st.success("Ocorrência registrada com sucesso!")
        
        cursor.close()
        connection.close()
        
        st.session_state['data'] = None
        st.session_state['origem'] = ''
        st.session_state['processo'] = ''
        st.session_state['endereco'] = ''
        st.session_state['localidade'] = ''
        st.session_state['referencia'] = ''
        st.session_state['tipo_solicitacao'] = ''
        st.session_state['atendimento'] = ''
        st.session_state['quant_moradores'] = 0
        st.session_state['hora'] = datetime.datetime.now().time()
        st.session_state['scaner'] = ''
        st.session_state['nome'] = ''
        st.session_state['fone'] = ''
        st.session_state['bairro'] = ''
        st.session_state['reg'] = ''
        st.session_state['descricao_ocorrencia'] = 'Alagamento'
        st.session_state['monitoramento'] = ''
        st.session_state['cep'] = '' 
        st.session_state['observacoes'] = ''

        st.experimental_rerun()