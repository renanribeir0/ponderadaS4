### Ponderada realizada com base na entrega do artefato da sprint 2

--- 

# 1 Dashboard de Telemetria

## 1.1 Visão Geral

O **Dashboard de Telemetria** foi desenvolvido para monitorar e analisar os logs de eventos gerados no módulo de ingestão de dados. A capacidade de visualizar dados em tempo real, acompanhar tendências e detectar problemas antes que impactem os usuários é essencial para a evolução do sistema. Com base nas análises realizadas, serão implementadas melhorias para otimizar o consumo de recursos, reduzir a latência e diminuir a quantidade de eventos desnecessários. Com isso, o Dashboard se consolida como um recurso estratégico para a gestão eficiente da ingestão de dados e garantia de qualidade dos serviços monitorados.

### Detalhamento da Compreensão dos Dados

Os dados analisados provêm de logs de eventos gerados pelos diferentes serviços de ingestão de dados no sistema. Estes logs contêm informações cruciais, como timestamps, tipos de eventos (sucesso ou erro), latência, contexto do erro, entre outros. A qualidade e precisão desses dados são garantidas através de validações nas consultas ao Supabase, onde registros incompletos ou corrompidos são descartados. A estrutura dos dados foi cuidadosamente analisada para identificar quais variáveis influenciam diretamente no desempenho e eficiência do sistema.

## 1.2 Arquitetura do Dashboard

### Fluxo de Dados
1. O Python consome os dados de logs do Supabase através de consultas otimizadas.
2. Os dados são agregados e processados em tempo real, aplicando filtros para garantir que apenas os dados relevantes sejam analisados.
3. O Streamlit exibe os resultados de forma interativa, com gráficos dinâmicos e filtros customizáveis.

### Estrutura do Projeto

bash
📂 src/dash_telemetria/
├── 📂 config/  # Configurações gerais do projeto, como estilo, variáveis etc.
├── 📂 visoes/  # Módulos de análise e agregação dos dados
├── 📂 components/  # Elementos visuais do dashboard
├── main.py  # Arquivo principal do dashboard


### Passos para Executar o Dashboard

#### 1. Configurar o .env
bash
# 1. Crie o.env na raiz do projeto e coloque as informações:
SUPABASE_URL=
SUPABASE_API_KEY=


#### 2. Instalar dependências
bash
 poetry install


#### 3. Executar o dashboard
bash
 poetry run streamlit run main.py


## 1.3 Métricas Utilizadas

### KPIs do Dashboard

- **Total de Logs** → Contagem total de eventos processados.
- **Eventos de Sucesso** → Contagem de eventos com level_type = SUCCESS.
- **Eventos com Erro** → Contagem de eventos com level_type = ERROR.
- **Latência Média** → Média de latency_ms para avaliar desempenho.
- **Eventos por Serviço** → Distribuição dos eventos por service.
- **Eventos ao Longo do Tempo** → Distribuição de logs ao longo dos dias/horas/minutos.
- **Erros por Serviço** → Identificação dos serviços que apresentam maior taxa de erro.

---

## 1.4 Design e Usabilidade

### Características do Design

- **Interface intuitiva** → Componentes bem organizados e legíveis.
- **Gráficos interativos** → Uso de Plotly para facilitar a análise.
- **Filtro de Tempo** → Permite selecionar granularidade (ano, mês, dia, hora, minuto).
- **Botão de Refresh** → Atualiza os dados sem precisar reiniciar o app.
- **Navegação Estruturada** → O dashboard está organizado em diferentes abas para facilitar a visualização das métricas.

### 1.4.1 Uso de IA para Aprimoramento do Design

Para garantir um design mais eficiente e intuitivo, utilizamos ferramentas de IA para otimizar a interface do dashboard. A IA foi utilizada para ajustar automaticamente a paleta de cores, destacando indicadores críticos em vermelho, conforme a análise de padrões de interação dos usuários no dashboard. Além disso, a disposição dos elementos do dashboard foi otimizada, garantindo que os dados mais importantes estejam sempre em destaque.

### Responsividade

O design do dashboard é responsivo, garantindo uma boa experiência tanto em desktops quanto em dispositivos móveis. O layout se adapta de forma dinâmica, ajustando a visualização dos gráficos e painéis de forma que o usuário tenha uma navegação fluída, independentemente do dispositivo.

## 1.5 Estrutura do Dashboard

Para garantir uma melhor usabilidade e experiência do usuário, o dashboard foi dividido em **quatro seções principais**:

### 1.5.1 Resumo

A seção de Resumo apresenta os principais KPIs do sistema de forma objetiva, utilizando "Big Numbers" para facilitar a visualização rápida dos indicadores mais importantes, como total de logs, eventos de sucesso, erros e latência média.

![Latencia](dash_telemetria/img/latencia.png)

### 1.5.2 Eventos no Tempo

A seção Eventos ao Longo do Tempo permite visualizar a distribuição dos logs conforme a granularidade desejada (ano, mês, dia, hora ou minuto). Essa funcionalidade é útil para identificar padrões e anomalias no processamento de eventos ao longo do tempo.

![Eventos](dash_telemetria/img/Eventos.png)

### 1.5.3 Análise por Serviço

Essa seção exibe uma visão detalhada sobre a quantidade e latência média dos eventos por serviço. A análise por serviço permite identificar quais serviços são mais demandados e quais podem estar impactando a performance geral do sistema devido a latências elevadas.

![Quantidade de eventos](dash_telemetria/img/QTDEventos.png)

![Quantidade de eventos](dash_telemetria/img/QTDEventos2.png)

### 1.5.4 Erros por Serviço

Permite identificar serviços com falhas e explorar os detalhes de cada erro reportado.

- **Visão Geral**: O dashboard apresenta um **resumo da quantidade total de erros por serviço**.
- **Seleção de Serviço**: O usuário pode selecionar um serviço específico para visualizar detalhes sobre os erros.
- **Tabela de Erros Agrupados**: Exibe os erros agrupados por service - context - error_description, permitindo identificar padrões e recorrências.
- **Tabela Detalhada de Erros**: Lista todos os erros individualmente, incluindo created_at - service - context - error_description.

Com esse dashboard, foi possível identificar que o módulo data_ingestion está enviando um número excessivo de eventos de iniciar_producer e consumer_callback. Essa descoberta gerou um insight crítico sobre desperdício de processamento, esse comportamento será otimizado para reduzir o consumo de recursos.

![Módulo](dash_telemetria/img/modulo.png)


## 1.6 Insights e Análises

A partir dos dados analisados, algumas informações valiosas foram extraídas:

- **Picos de Processamento** → Identificação dos horários de maior volume de eventos, permitindo otimizar o processamento em períodos críticos.
- **Serviços com Maior Latência** → Análise de gargalos no processamento, identificando quais serviços precisam ser otimizados para melhorar o desempenho geral.
- **Taxa de Erros** → Identificação de serviços que apresentam mais falhas, permitindo a implementação de correções mais direcionadas.
- **Tendência de Uso** → Como o volume de eventos evolui ao longo do tempo, oferecendo insights para planejamento de capacidade e alocação de recursos.