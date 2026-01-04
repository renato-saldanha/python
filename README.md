# Repositório voltado aos estudos do bootcamp Luizalabs - Back-end com Python


# 🏦 Sistema Bancário - Desafio Luizalabs

Sistema bancário em Python desenvolvido como primeiro desafio do curso **Luizalabs - Back-end com Python**. Implementa operações bancárias básicas (depósito, saque, extrato) e gestão de usuários e contas correntes.

## ✨ Funcionalidades

- **Operações Bancárias**: Depósito, saque e extrato
- **Gestão de Usuários**: Cadastro com validação de CPF (sem duplicidade)
- **Gestão de Contas**: Criação de contas correntes vinculadas aos usuários
- **Validações**: Limite de 3 saques e R$ 500,00 por saque

## 🚀 Como Executar

```bash
python desafio.py
```

## 🎯 Conceitos Aplicados

- **Modularização**: Código separado em funções reutilizáveis
- **Tipos de Argumentos**: 
  - `depositar()` - Positional only
  - `sacar()` - Keyword only
  - `ver_extrato()` - Misto (positional + keyword)
- **POO**: Classes `Usuario` e `Conta`
- **Validações**: CPF, limites e regras de negócio

## 📋 Estrutura Principal

- **Classes**: `Usuario`, `Conta`
- **Funções**: `depositar()`, `sacar()`, `ver_extrato()`, `criar_usuario()`, `criar_conta()`
- **Regras**: Agência fixa "0001", contas sequenciais, CPF apenas números

---

**Requisitos**: Python 3.6+  
**Arquivo principal**: `desafio.py`
