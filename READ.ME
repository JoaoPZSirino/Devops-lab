# DevOps Lab

## Sobre o Projeto
Este projeto nasceu como uma forma de colocar em prática conhecimentos sobre **DevOps** e **SRE**. 

Nesta primeira versão, a aplicação consiste em um serviço web desenvolvido em **Python (Flask)** que consome uma API externa e renderiza a resposta em uma página HTML. Para garantir a portabilidade e o isolamento, a aplicação foi containerizada utilizando um `Dockerfile` baseado na imagem oficial do Python, gerenciando dependências via `requirements.txt` e expondo o serviço na porta `5000`.

Todo o ciclo de vida — desde a validação de código e testes automatizados até o build de imagens e a orquestração em um cluster Kubernetes local — é totalmente automatizado por meio de uma pipeline de **CI/CD** no **Azure DevOps**.

---

## Tecnologias e Ferramentas Utilizadas
* **Linguagem & Framework:** Python 3.11, Flask, Requests
* **Testes:** Pytest
* **Containerização:** Docker, Docker Hub (`joaopzsirino/devops-lab`)
* **Orquestração & Infraestrutura Local:** Kubernetes (`kubectl`), Kind (Kubernetes in Docker)
* **CI/CD:** Azure DevOps Pipelines (`ubuntu-latest`)

---

## Arquitetura do Projeto
O repositório está estruturado com os seguintes componentes essenciais:

1. Configura a versão do Python no agente do Azure DevOps:
Usa a task UsePythonVersion@0

2. Instalação de Dependências (pip):
Atualiza o gerenciador de pacotes (pip) e instala todas as bibliotecas necessárias declaradas no arquivo requirements.txt.

3. Execução de Testes Unitários (pytest):
Executa os testes unitários (pytest test_app.py -v) para garantir que o código está íntegro antes de prosseguir.

4. Build e Publicação no Docker Hub (Docker@2):
Gera a imagem containerizada da aplicação e realiza o push automatizado para o Docker Hub (joaopzsirino/devops-lab).

5. Instalação do Kubectl (KubectlInstaller@0):
Instala a ferramenta de linha de comando oficial do Kubernetes (kubectl) no agente para permitir o gerenciamento e o envio de manifestos ao cluster.

6. Instalação do Kind e Subida do Cluster:
Baixa dinamicamente o Kind (Kubernetes in Docker), provisiona um cluster Kubernetes customizado com 3 nós (1 control-plane e 2 workers) utilizando o arquivo create-cluster.yaml, e aguarda ativamente (kubectl wait) até que todos os nós estejam no estado Ready.

7. Aplicação do Manifesto do Pod (kubectl apply):
Envia o arquivo de manifesto (pod.yaml) para o cluster recém-criado, instanciando o Pod da aplicação (projeto-devops).

8. Inspeção e Validação do Cluster:
Executa comandos de diagnóstico (kubectl get pods -o wide e kubectl describe pod) para verificar a saúde do Pod, confirmar que ele saiu do estado pendente e identificar exatamente em qual nó worker a aplicação está alocada.

devops-lab/
├── app.py                # Aplicação Flask principal
├── test_app.py           # Testes unitários com Pytest
├── requirements.txt      # Dependências do projeto Python
├── Dockerfile            # Receita para containerizar a aplicação
├── create-cluster.yaml   # Configuração do Kind (1 control-plane, 2 workers)
├── pod.yaml              # Manifesto do Kubernetes para o Pod da aplicação
└── azure-pipelines.yml   # Definição completa da Pipeline de CI/CD