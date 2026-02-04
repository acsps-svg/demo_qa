import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://localhost:8000")
    page.get_by_role("textbox", name="Nome da nova pessoa").click()
    page.get_by_role("textbox", name="Nome da nova pessoa").fill("Teste 123")
    page.get_by_role("button", name="Criar").click()
    page.locator("#goalInput").dblclick()
    page.locator("#goalInput").dblclick()
    page.locator("#goalInput").press("ControlOrMeta+a")
    page.locator("#goalInput").fill("3000")
    page.locator("#goalInput").press("Tab")
    page.locator("#cupInput").fill("300")
    page.locator("#cupInput").press("Enter")
    page.get_by_role("button", name="Beber Copo").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Zerar meu dia").click()