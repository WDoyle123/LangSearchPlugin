from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.nav import Navigation
from mkdocs.config import config_options
import logging

log = logging.getLogger("mkdocs.plugins." + __name__)

class LangSearchPlugin(BasePlugin):
    config_scheme = (
        ('default_language', config_options.Type(str, default='en')),
    )

    def __init__(self):
        super().__init__()
        log.info("LangSearchPlugin initialized")

    def on_pre_page(self, page: Page, config, files):
        log.info(f"Processing page: {page.file.src_path}")
        # Add the language of the current page to the page context
        language = page.file.src_path.split('/')[0]
        page.meta['language'] = language
        log.debug(f"Set language for {page.file.src_path} to {language}")
        return page

    def on_nav(self, nav: Navigation, config, files):
        log.info("Modifying navigation items based on default language")
        # Filter out pages that do not match the default language
        default_language = self.config['default_language']
        nav.items = [item for item in nav.items if item.file.src_path.startswith(default_language)]
        log.debug(f"Filtered navigation items to default language: {default_language}")
        return nav

    def on_page_context(self, context, page: Page, config, nav: Navigation):
        log.info(f"Setting search index context for page: {page.file.src_path}")
        # Ensure the search only indexes pages of the current language
        default_language = self.config['default_language']
        context['search'] = {
            'index': [p for p in nav.pages if p.file.src_path.startswith(default_language)]
        }
        log.debug(f"Search context set for default language: {default_language}")
        return context

