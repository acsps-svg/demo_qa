import pytest
import re
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"viewport": {"width":880,"height":720}}


def test_example(page: Page) -> None:
    page.goto("http://bootswatch.com/default/")
    expect(page.get_by_role("heading",name="Default")).to_be_visible()
    page.goto("http://bootswatch.com/zephyr/")

    page.get_by_role("group", name="Ranges").click()
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_role("heading",name="Zephyr")).to_be_visible()

    # page.get_by_placeholder("Enter email").click()
    # page.get_by_placeholder("Enter email").dblclick()
    # page.get_by_placeholder("Enter email").press("ControlOrMeta+x")
    # page.get_by_placeholder("Enter email").fill("Teste123")
    # page.get_by_placeholder("Enter email").press("Enter")
    # page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(5).dblclick()
    # page.get_by_role("button", name=" Copy Code").click()

def test_new(page: Page) -> None:
    page.goto("https://andrewcesarp.github.io/")
    page.get_by_role("textbox", name="Nome da nova pessoa").click()
    page.get_by_role("textbox", name="Nome da nova pessoa").fill("Drew")
    page.get_by_role("textbox", name="Nome da nova pessoa").press("Enter")
    page.get_by_role("button", name="← Trocar Pessoa").click()
    page.get_by_text("Drew", exact=True).click()
    page.locator("#goalInput").click()
    page.locator("#goalInput").dblclick()
    page.locator("#goalInput").fill("-4000")
    page.locator("#goalInput").press("Enter")
    page.locator("#cupInput").dblclick()
    page.locator("#cupInput").fill("2500")
    page.get_by_role("button", name="Beber Copo").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Zerar meu dia").click()
    page.locator("#goalInput").click()
    page.locator("#goalInput").click()
    page.locator("#goalInput").press("ArrowLeft")
    page.locator("#goalInput").press("ArrowLeft")
    page.locator("#goalInput").press("ArrowLeft")
    page.locator("#goalInput").press("ArrowLeft")
    page.locator("#goalInput").fill("4000")
    page.locator("#goalInput").press("Enter")
    page.locator("#cupInput").highlight().click()
    page.locator("#cupInput").highlight().fill("3150")
    page.locator("#cupInput").press("Enter")
    page.get_by_role("button", name="Beber Copo").click()

    expect(page.get_by_text("Beber Copo")).to_be_visible()