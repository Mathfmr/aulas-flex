# Sua primeira tarefa é criar um aplicativo Streamlit que serve como uma página de boas-vindas. Você deve usar os conceitos de estrutura e exibição de texto que aprendeu na primeira etapa. O aplicativo deve ser simples, mas visualmente organizado. Crie um novo arquivo Python chamado boas_vindas.py. Importe a biblioteca Streamlit. Utilize st.title() para criar um título principal na sua página, como por exemplo, "Bem-vindo ao Meu Primeiro App Streamlit!". Abaixo do título, utilize st.header() para adicionar um cabeçalho de seção, como "Sobre este App". Em seguida, utilize st.write() para escrever um parágrafo que explique brevemente o objetivo da aula, como "Este aplicativo foi criado para demonstrar os conceitos básicos de Streamlit, como exibição de texto e a estrutura de um app". Adicione um divisor horizontal usando st.divider() para separar visualmente as seções. Por fim, utilize st.code() para exibir o código-fonte completo do seu próprio aplicativo. Use language='python' para garantir a formatação correta. O código deve ser idêntico ao que você escreveu para esta questão. Instruções de execução: Após salvar o arquivo, execute o aplicativo no terminal com o comando streamlit run boas_vindas.py e verifique se o layout corresponde ao que foi solicitado.

import streamlit as st


st.title('Bem-vindo ao Meu Primeiro App Streamlit!')
st.header('Sobre esse app')
st.write('Este aplicativo foi criado para demonstrar os conceitos básicos de Streamlit, como exibição de texto e a estrutura de um app')

st.code('''

for i in range (10):
    if i % 2 == 0:
        print('par')
    else:
        print('impar')


''')

st.divider()


# Agora, você vai aprimorar o aplicativo anterior para torná-lo interativo, coletando e processando entradas do usuário. Você deve usar os widgets de entrada e as funções de feedback que aprendeu na segunda etapa. No arquivo boas_vindas.py, adicione uma nova seção abaixo do divisor. Use st.header() com o título "Interação com o Usuário". Crie uma caixa de texto usando st.text_input() com o rótulo "Qual o seu nome?". Armazene a entrada do usuário em uma variável. Crie um st.button() com o texto "Cumprimentar". Utilize uma estrutura if para verificar se o botão foi clicado. Se sim: a. Exiba uma mensagem de sucesso usando st.success() com o texto "Ação realizada com sucesso!". b. Utilize st.write() para exibir um cumprimento personalizado, como "Olá, [Nome do Usuário]! É um prazer ter você aqui.". c. Crie um menu de seleção de opções (dropdown) usando st.selectbox() com o rótulo "Escolha seu status:" e as opções "Aluno", "Professor", "Visitante". Exiba o valor selecionado em um texto logo abaixo do menu
st.header('Interação com o Usuário')
nome = st.text_input('qual o seu nome: ')

if nome == '':
    st.error('ainda não digiou nenhum Nome')
else:
    st.success('Ação realizada com sucesso!')
    
st.write(f'Ola,{nome}! é um prazer ter você aqui')

opções = st.selectbox('escolha seu status',
             ('professor','aluno','visitante'))

st.write(f'você escolheu a opção {opções}')

