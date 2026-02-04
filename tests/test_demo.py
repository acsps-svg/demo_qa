import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://127.0.0.1:5000/")
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

    expect(page.get_by_text("300", exact=True)).to_be_visible()