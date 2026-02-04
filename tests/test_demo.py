import re
from playwright.sync_api import Page, expect

def test_criar_usuario_e_verificar_login(page: Page):
    # O pytest-playwright já abre o navegador e usa a base-url do .yml
    page.goto("/")

    # 1. Verifica se está na tela inicial
    expect(page.get_by_text("Quem vai beber água?")).to_contain_text("Quem vai beber água?")

    # 2. Cria um novo usuário
    # Fill: preenche o input
    page.get_by_placeholder("Nome da nova pessoa").fill("Python Tester")
    
    # Click: clica no botão "Criar"
    page.get_by_role("button", name="Criar").click()

    # 3. Validações da tela de Tracker
    # Verifica se o nome aparece nas boas-vindas
    expect(page.locator("#welcomeName")).to_contain_text("Olá, Python Tester")
    
    # Verifica se o contador começa zerado
    expect(page.locator("#currentDisplay")).to_have_text("0")

def test_fluxo_beber_agua(page: Page):
    page.goto("/")

    # Setup: Cria usuário rápido para o teste
    page.get_by_placeholder("Nome da nova pessoa").fill("DevOps User")
    page.get_by_role("button", name="Criar").click()

    # Ação: Beber água
    # Localiza o botão que contém o texto "Beber Copo"
    page.locator(".btn-drink").click()

    # Validação: O padrão do HTML é copo de 250ml
    expect(page.locator("#currentDisplay")).to_have_text("250")
    
    # Validação Visual (Opcional): Verifica se a cor mudou ou se o gráfico andou
    # Aqui verificamos apenas se o número atualizou corretamente