import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("http://127.0.0.1:5000")
    page.get_by_role("textbox", name="Nome da nova pessoa").click()
    page.get_by_role("textbox", name="Nome da nova pessoa").fill("Andrew")
    page.get_by_role("button", name="Criar").click()

    expect(page.get_by_role("button", name="Beber Copo1")).to_be_visible()